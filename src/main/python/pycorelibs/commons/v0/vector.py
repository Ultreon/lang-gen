from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Double as _double
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class Vec3d():
    """dev.ultreon.libs.commons.v0.vector.Vec3d"""
 
    @staticmethod
    def _wrap(java_value: _Vec3d) -> 'Vec3d':
        return Vec3d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec3d):
        """
        Dynamic initializer for Vec3d.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec3d__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec3d__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getY()"""
        return float._wrap(super(Vec3d, self).getY())

    @overload
    def nor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.nor()"""
        return 'Vec3d'._wrap(super(Vec3d, self).nor())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getX()"""
        return float._wrap(super(Vec3d, self).getX())

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getZ()"""
        return float._wrap(super(Vec3d, self).getZ())

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setZ(double)"""
        super(_Vec3d, self).setZ(_double.valueOf(arg0))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3d', arg1: 'Vec3d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(_Vec3d.dot(arg0, arg1))

    @overload
    def pow(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(_double.valueOf(arg0)))

    @overload
    def mul(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(_double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def pow(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(arg0))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3d.toString()"""
        return str._wrap(super(Vec3d, self).toString())

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3d.f()"""
        return 'Vec3f'._wrap(super(Vec3d, self).f())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d(double,double,double)"""
        val = _Vec3d(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec3d, self).writeExternal(arg0)

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.len2()"""
        return float._wrap(super(Vec3d, self).len2())

    @overload
    def div(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(arg0))

    @overload
    def add(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.div(arg0, arg1))

    @overload
    def cpy(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.cpy()"""
        return 'Vec3d'._wrap(super(Vec3d, self).cpy())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec3d, self).readExternal(arg0)

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.pow(arg0, arg1))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setX(double)"""
        super(_Vec3d, self).setX(_double.valueOf(arg0))

    @overload
    def dst(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(super(_Vec3d, self).dst(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.mul(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.add(arg0, arg1))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double,double,double)"""
        return float._wrap(super(_Vec3d, self).dot(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setY(double)"""
        super(_Vec3d, self).setY(_double.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mod(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(arg0))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(double,double,double)"""
        return float._wrap(super(_Vec3d, self).dst(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.sub(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = _Vec3d()
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(_double.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = _Vec3d()
        self.__wrapper = val

    @overload
    def floor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.floor()"""
        return 'Vec3d'._wrap(super(Vec3d, self).floor())

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double)"""
        return float._wrap(super(_Vec3d, self).dot(_double.valueOf(arg0)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.d()"""
        return 'Vec3d'._wrap(super(Vec3d, self).d())

    @overload
    def dec(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.dec()"""
        return 'Vec3d'._wrap(super(Vec3d, self).dec())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3d.hashCode()"""
        return int._wrap(super(Vec3d, self).hashCode())

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3d.i()"""
        return 'Vec3i'._wrap(super(Vec3d, self).i())

    @overload
    def set(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(_double.valueOf(arg0)))

    @overload
    def clone(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.clone()"""
        return 'Vec3d'._wrap(super(Vec3d, self).clone())

    @overload
    def dot(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(super(_Vec3d, self).dot(arg0))

    @overload
    def div(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(_double.valueOf(arg0)))

    @overload
    def mod(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(_double.valueOf(arg0)))

    @overload
    def neg(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.neg()"""
        return 'Vec3d'._wrap(super(Vec3d, self).neg())

    @overload
    def mul(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3d.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec3d, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def inc(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.inc()"""
        return 'Vec3d'._wrap(super(Vec3d, self).inc())

    @overload
    def ceil(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.ceil()"""
        return 'Vec3d'._wrap(super(Vec3d, self).ceil())

    @overload
    def sub(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(arg0))

    @overload
    def abs(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.abs()"""
        return 'Vec3d'._wrap(super(Vec3d, self).abs())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3d
from builtins import str
import java.lang.Double as _double
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class Vec3d():
    """dev.ultreon.libs.commons.v0.vector.Vec3d"""
 
    @staticmethod
    def _wrap(java_value: _Vec3d) -> 'Vec3d':
        return Vec3d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec3d):
        """
        Dynamic initializer for Vec3d.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec3d__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec3d__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getY()"""
        return float._wrap(super(Vec3d, self).getY())

    @overload
    def nor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.nor()"""
        return 'Vec3d'._wrap(super(Vec3d, self).nor())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getX()"""
        return float._wrap(super(Vec3d, self).getX())

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getZ()"""
        return float._wrap(super(Vec3d, self).getZ())

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setZ(double)"""
        super(_Vec3d, self).setZ(_double.valueOf(arg0))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3d', arg1: 'Vec3d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(_Vec3d.dot(arg0, arg1))

    @overload
    def pow(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(_double.valueOf(arg0)))

    @overload
    def mul(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(_double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def pow(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(arg0))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3d.toString()"""
        return str._wrap(super(Vec3d, self).toString())

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3d.f()"""
        return 'Vec3f'._wrap(super(Vec3d, self).f())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d(double,double,double)"""
        val = _Vec3d(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).pow(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec3d, self).writeExternal(arg0)

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.len2()"""
        return float._wrap(super(Vec3d, self).len2())

    @overload
    def div(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(arg0))

    @overload
    def add(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.div(arg0, arg1))

    @overload
    def cpy(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.cpy()"""
        return 'Vec3d'._wrap(super(Vec3d, self).cpy())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec3d, self).readExternal(arg0)

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.pow(arg0, arg1))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setX(double)"""
        super(_Vec3d, self).setX(_double.valueOf(arg0))

    @overload
    def dst(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(super(_Vec3d, self).dst(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.mul(arg0, arg1))

    @staticmethod
    @overload
    def add(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.add(arg0, arg1))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double,double,double)"""
        return float._wrap(super(_Vec3d, self).dot(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setY(double)"""
        super(_Vec3d, self).setY(_double.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mod(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(arg0))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(double,double,double)"""
        return float._wrap(super(_Vec3d, self).dst(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d._wrap(_Vec3d.sub(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = _Vec3d()
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(_double.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = _Vec3d()
        self.__wrapper = val

    @overload
    def floor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.floor()"""
        return 'Vec3d'._wrap(super(Vec3d, self).floor())

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double)"""
        return float._wrap(super(_Vec3d, self).dot(_double.valueOf(arg0)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.d()"""
        return 'Vec3d'._wrap(super(Vec3d, self).d())

    @overload
    def dec(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.dec()"""
        return 'Vec3d'._wrap(super(Vec3d, self).dec())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double,double,double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3d.hashCode()"""
        return int._wrap(super(Vec3d, self).hashCode())

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3d.i()"""
        return 'Vec3i'._wrap(super(Vec3d, self).i())

    @overload
    def set(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).set(_double.valueOf(arg0)))

    @overload
    def clone(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.clone()"""
        return 'Vec3d'._wrap(super(Vec3d, self).clone())

    @overload
    def dot(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float._wrap(super(_Vec3d, self).dot(arg0))

    @overload
    def div(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).div(_double.valueOf(arg0)))

    @overload
    def mod(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mod(_double.valueOf(arg0)))

    @overload
    def neg(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.neg()"""
        return 'Vec3d'._wrap(super(Vec3d, self).neg())

    @overload
    def mul(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).mul(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3d.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec3d, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def inc(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.inc()"""
        return 'Vec3d'._wrap(super(Vec3d, self).inc())

    @overload
    def ceil(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.ceil()"""
        return 'Vec3d'._wrap(super(Vec3d, self).ceil())

    @overload
    def sub(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'._wrap(super(_Vec3d, self).sub(arg0))

    @overload
    def abs(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.abs()"""
        return 'Vec3d'._wrap(super(Vec3d, self).abs())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3d 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import java.lang.Class as _Class
_Class = _Class
 
class Vec3i():
    """dev.ultreon.libs.commons.v0.vector.Vec3i"""
 
    @staticmethod
    def _wrap(java_value: _Vec3i) -> 'Vec3i':
        return Vec3i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec3i):
        """
        Dynamic initializer for Vec3i.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec3i__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec3i__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pow(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).pow(arg0))

    @overload
    def add(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).add(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def dec(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.dec()"""
        return 'Vec3i'._wrap(super(Vec3i, self).dec())

    @staticmethod
    @overload
    def sub(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i._wrap(_Vec3i.sub(arg0, arg1))

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.i()"""
        return 'Vec3i'._wrap(super(Vec3i, self).i())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i(int,int,int)"""
        val = _Vec3i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec3i, self).writeExternal(arg0)

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(int)"""
        return int._wrap(super(_Vec3i, self).dot(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).set(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).set(arg0))

    @overload
    def neg(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.neg()"""
        return 'Vec3i'._wrap(super(Vec3i, self).neg())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def mod(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mod(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def pow(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3i.pow(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3d._wrap(_Vec3i.pow(arg0, arg1))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3i', arg1: 'Vec3i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(_Vec3i.dot(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.hashCode()"""
        return int._wrap(super(Vec3i, self).hashCode())

    @overload
    def mul(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mul(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mod(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mod(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def div(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i._wrap(_Vec3i.div(arg0, arg1))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i._wrap(_Vec3i.mul(arg0, arg1))

    @overload
    def cpy(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.cpy()"""
        return 'Vec3i'._wrap(super(Vec3i, self).cpy())

    @overload
    def pow(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).pow(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def mul(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mul(_int.valueOf(arg0)))

    @overload
    def setZ(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setZ(int)"""
        super(_Vec3i, self).setZ(_int.valueOf(arg0))

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).sub(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def div(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).div(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def add(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i._wrap(_Vec3i.add(arg0, arg1))

    @overload
    def div(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).div(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i()"""
        val = _Vec3i()
        self.__wrapper = val

    @overload
    def clone(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.clone()"""
        return 'Vec3i'._wrap(super(Vec3i, self).clone())

    @overload
    def mod(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mod(_int.valueOf(arg0)))

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3i.f()"""
        return 'Vec3f'._wrap(super(Vec3i, self).f())

    @overload
    def pow(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).pow(_int.valueOf(arg0)))

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3i.dst(int,int,int)"""
        return float._wrap(super(_Vec3i, self).dst(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3i.toString()"""
        return str._wrap(super(Vec3i, self).toString())

    @overload
    def sub(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).sub(_int.valueOf(arg0)))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setY(int)"""
        super(_Vec3i, self).setY(_int.valueOf(arg0))

    @overload
    def add(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).add(arg0))

    @overload
    def mul(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).mul(arg0))

    @overload
    def sub(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).sub(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i()"""
        val = _Vec3i()
        self.__wrapper = val

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getX()"""
        return int._wrap(super(Vec3i, self).getX())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def add(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).add(_int.valueOf(arg0)))

    @overload
    def dst(self, arg0: 'Vec3i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3i.dst(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return float._wrap(super(_Vec3i, self).dst(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3i.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec3i, self).equals(arg0))

    @overload
    def inc(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.inc()"""
        return 'Vec3i'._wrap(super(Vec3i, self).inc())

    @overload
    def div(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(int,int,int)"""
        return 'Vec3i'._wrap(super(_Vec3i, self).div(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getY()"""
        return int._wrap(super(Vec3i, self).getY())

    @overload
    def abs(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.abs()"""
        return 'Vec3i'._wrap(super(Vec3i, self).abs())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec3i, self).readExternal(arg0)

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setX(int)"""
        super(_Vec3i, self).setX(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getZ(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getZ()"""
        return int._wrap(super(Vec3i, self).getZ())

    @overload
    def dot(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int._wrap(super(_Vec3i, self).dot(arg0))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3i.d()"""
        return 'Vec3d'._wrap(super(Vec3i, self).d())

    @overload
    def dot(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(int,int,int)"""
        return int._wrap(super(_Vec3i, self).dot(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.commons.v0.vector.Vec4i as _Vec4i
_Vec4i = _Vec4i
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec4f as _Vec4f
_Vec4f = _Vec4f
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec4d as _Vec4d
_Vec4d = _Vec4d
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec4i():
    """dev.ultreon.libs.commons.v0.vector.Vec4i"""
 
    @staticmethod
    def _wrap(java_value: _Vec4i) -> 'Vec4i':
        return Vec4i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec4i):
        """
        Dynamic initializer for Vec4i.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec4i__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec4i__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pow(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).pow(arg0))

    @overload
    def set(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).set(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec4i, self).readExternal(arg0)

    @overload
    def mod(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mod(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec4i, self).writeExternal(arg0)

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).sub(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getY()"""
        return int._wrap(super(Vec4i, self).getY())

    @staticmethod
    @overload
    def pow(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4i.pow(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4d._wrap(_Vec4i.pow(arg0, arg1))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setY(int)"""
        super(_Vec4i, self).setY(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4i.toString()"""
        return str._wrap(super(Vec4i, self).toString())

    @overload
    def getZ(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getZ()"""
        return int._wrap(super(Vec4i, self).getZ())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(int)"""
        return int._wrap(super(_Vec4i, self).dot(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def mul(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i._wrap(_Vec4i.mul(arg0, arg1))

    @overload
    def pow(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).pow(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.i()"""
        return 'Vec4i'._wrap(super(Vec4i, self).i())

    @staticmethod
    @overload
    def add(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i._wrap(_Vec4i.add(arg0, arg1))

    @overload
    def mod(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mod(arg0))

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4i.dst(int,int,int,int)"""
        return float._wrap(super(_Vec4i, self).dst(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mul(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mul(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setX(int)"""
        super(_Vec4i, self).setX(_int.valueOf(arg0))

    @overload
    def inc(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.inc()"""
        return 'Vec4i'._wrap(super(Vec4i, self).inc())

    @overload
    def clone(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.clone()"""
        return 'Vec4i'._wrap(super(Vec4i, self).clone())

    @overload
    def dot(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(int,int,int,int)"""
        return int._wrap(super(_Vec4i, self).dot(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4i.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec4i, self).equals(arg0))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getX()"""
        return int._wrap(super(Vec4i, self).getX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getW(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getW()"""
        return int._wrap(super(Vec4i, self).getW())

    @overload
    def abs(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.abs()"""
        return 'Vec4i'._wrap(super(Vec4i, self).abs())

    @staticmethod
    @overload
    def dot(arg0: 'Vec4i', arg1: 'Vec4i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return int._wrap(_Vec4i.dot(arg0, arg1))

    @overload
    def setW(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setW(int)"""
        super(_Vec4i, self).setW(_int.valueOf(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i._wrap(_Vec4i.div(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i()"""
        val = _Vec4i()
        self.__wrapper = val

    @overload
    def add(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).add(_int.valueOf(arg0)))

    @overload
    def dec(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.dec()"""
        return 'Vec4i'._wrap(super(Vec4i, self).dec())

    @overload
    def div(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).div(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.hashCode()"""
        return int._wrap(super(Vec4i, self).hashCode())

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).add(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4i.f()"""
        return 'Vec4f'._wrap(super(Vec4i, self).f())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i()"""
        val = _Vec4i()
        self.__wrapper = val

    @overload
    def dst(self, arg0: 'Vec4i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4i.dst(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return float._wrap(super(_Vec4i, self).dst(arg0))

    @overload
    def sub(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).sub(arg0))

    @overload
    def neg(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.neg()"""
        return 'Vec4i'._wrap(super(Vec4i, self).neg())

    @overload
    def pow(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).pow(_int.valueOf(arg0)))

    @overload
    def add(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).add(arg0))

    @overload
    def mul(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mul(arg0))

    @overload
    def div(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(int,int,int,int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).div(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mul(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mul(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dot(self, arg0: 'Vec4i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return int._wrap(super(_Vec4i, self).dot(arg0))

    @overload
    def div(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).div(arg0))

    @overload
    def cpy(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.cpy()"""
        return 'Vec4i'._wrap(super(Vec4i, self).cpy())

    @staticmethod
    @overload
    def sub(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i._wrap(_Vec4i.sub(arg0, arg1))

    @overload
    def setZ(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setZ(int)"""
        super(_Vec4i, self).setZ(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def mod(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).mod(_int.valueOf(arg0)))

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4i.d()"""
        return 'Vec4d'._wrap(super(Vec4i, self).d())

    @overload
    def sub(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).sub(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(int)"""
        return 'Vec4i'._wrap(super(_Vec4i, self).set(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i(int,int,int,int)"""
        val = _Vec4i(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2d
from builtins import str
import java.lang.Double as _double
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec2d():
    """dev.ultreon.libs.commons.v0.vector.Vec2d"""
 
    @staticmethod
    def _wrap(java_value: _Vec2d) -> 'Vec2d':
        return Vec2d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec2d):
        """
        Dynamic initializer for Vec2d.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec2d__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec2d__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).add(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(double)"""
        return float._wrap(super(_Vec2d, self).dot(_double.valueOf(arg0)))

    @overload
    def mul(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mul(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2d.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec2d, self).equals(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).set(_double.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mod(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mod(_double.valueOf(arg0)))

    @overload
    def pow(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).pow(arg0))

    @overload
    def add(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).add(_double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def add(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d._wrap(_Vec2d.add(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).set(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d._wrap(_Vec2d.mul(arg0, arg1))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.setY(double)"""
        super(_Vec2d, self).setY(_double.valueOf(arg0))

    @staticmethod
    @overload
    def dot(arg0: 'Vec2d', arg1: 'Vec2d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float._wrap(_Vec2d.dot(arg0, arg1))

    @overload
    def dec(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.dec()"""
        return 'Vec2d'._wrap(super(Vec2d, self).dec())

    @overload
    def div(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).div(arg0))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec2d, self).writeExternal(arg0)

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2d.f()"""
        return 'Vec2f'._wrap(super(Vec2d, self).f())

    @overload
    def inc(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.inc()"""
        return 'Vec2d'._wrap(super(Vec2d, self).inc())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2d.hashCode()"""
        return int._wrap(super(Vec2d, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d(double,double)"""
        val = _Vec2d(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val

    @overload
    def sub(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).sub(arg0))

    @overload
    def add(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).add(arg0))

    @overload
    def neg(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.neg()"""
        return 'Vec2d'._wrap(super(Vec2d, self).neg())

    @overload
    def mul(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mul(arg0))

    @staticmethod
    @overload
    def sub(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d._wrap(_Vec2d.sub(arg0, arg1))

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.d()"""
        return 'Vec2d'._wrap(super(Vec2d, self).d())

    @overload
    def sub(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).sub(_double.valueOf(arg0)))

    @overload
    def ceil(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.ceil()"""
        return 'Vec2d'._wrap(super(Vec2d, self).ceil())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.clone()"""
        return 'Vec2d'._wrap(super(Vec2d, self).clone())

    @overload
    def pow(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).pow(_double.valueOf(arg0)))

    @overload
    def mod(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mod(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def dst(self, arg0: 'Vec2d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dst(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float._wrap(super(_Vec2d, self).dst(arg0))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).sub(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d()"""
        val = _Vec2d()
        self.__wrapper = val

    @staticmethod
    @overload
    def pow(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d._wrap(_Vec2d.pow(arg0, arg1))

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.getY()"""
        return float._wrap(super(Vec2d, self).getY())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.getX()"""
        return float._wrap(super(Vec2d, self).getX())

    @staticmethod
    @overload
    def div(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d._wrap(_Vec2d.div(arg0, arg1))

    @overload
    def abs(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.abs()"""
        return 'Vec2d'._wrap(super(Vec2d, self).abs())

    @overload
    def dot(self, arg0: 'Vec2d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float._wrap(super(_Vec2d, self).dot(arg0))

    @overload
    def nor(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.nor()"""
        return 'Vec2d'._wrap(super(Vec2d, self).nor())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec2d, self).readExternal(arg0)

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.setX(double)"""
        super(_Vec2d, self).setX(_double.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d()"""
        val = _Vec2d()
        self.__wrapper = val

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).set(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def pow(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).pow(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def mul(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mul(_double.valueOf(arg0)))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dst(double,double)"""
        return float._wrap(super(_Vec2d, self).dst(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.len2()"""
        return float._wrap(super(Vec2d, self).len2())

    @overload
    def div(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(double,double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).div(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2d.toString()"""
        return str._wrap(super(Vec2d, self).toString())

    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2d.i()"""
        return 'Vec2i'._wrap(super(Vec2d, self).i())

    @overload
    def mod(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).mod(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cpy(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.cpy()"""
        return 'Vec2d'._wrap(super(Vec2d, self).cpy())

    @overload
    def floor(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.floor()"""
        return 'Vec2d'._wrap(super(Vec2d, self).floor())

    @overload
    def div(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(double)"""
        return 'Vec2d'._wrap(super(_Vec2d, self).div(_double.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(double,double)"""
        return float._wrap(super(_Vec2d, self).dot(_double.valueOf(arg0), _double.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec2f():
    """dev.ultreon.libs.commons.v0.vector.Vec2f"""
 
    @staticmethod
    def _wrap(java_value: _Vec2f) -> 'Vec2f':
        return Vec2f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec2f):
        """
        Dynamic initializer for Vec2f.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec2f__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec2f__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec2f, self).writeExternal(arg0)

    @overload
    def dst(self, arg0: 'Vec2f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2f.dst(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float._wrap(super(_Vec2f, self).dst(arg0))

    @overload
    def mod(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mod(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def pow(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2f.pow(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2d._wrap(_Vec2f.pow(arg0, arg1))

    @overload
    def div(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).div(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f._wrap(_Vec2f.div(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dot(self, arg0: 'Vec2f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float._wrap(super(_Vec2f, self).dot(arg0))

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.getX()"""
        return float._wrap(super(Vec2f, self).getX())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f()"""
        val = _Vec2f()
        self.__wrapper = val

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.setY(float)"""
        super(_Vec2f, self).setY(_float.valueOf(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).set(_float.valueOf(arg0)))

    @overload
    def ceil(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.ceil()"""
        return 'Vec2f'._wrap(super(Vec2f, self).ceil())

    @overload
    def dec(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.dec()"""
        return 'Vec2f'._wrap(super(Vec2f, self).dec())

    @staticmethod
    @overload
    def sub(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f._wrap(_Vec2f.sub(arg0, arg1))

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.f()"""
        return 'Vec2f'._wrap(super(Vec2f, self).f())

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.getY()"""
        return float._wrap(super(Vec2f, self).getY())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2f.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec2f, self).equals(arg0))

    @overload
    def pow(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).pow(_float.valueOf(arg0)))

    @overload
    def inc(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.inc()"""
        return 'Vec2f'._wrap(super(Vec2f, self).inc())

    @overload
    def mul(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mul(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2f.toString()"""
        return str._wrap(super(Vec2f, self).toString())

    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2f.i()"""
        return 'Vec2i'._wrap(super(Vec2f, self).i())

    @overload
    def neg(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.neg()"""
        return 'Vec2f'._wrap(super(Vec2f, self).neg())

    @overload
    def abs(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.abs()"""
        return 'Vec2f'._wrap(super(Vec2f, self).abs())

    @overload
    def add(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).add(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec2f', arg1: 'Vec2f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float._wrap(_Vec2f.dot(arg0, arg1))

    @overload
    def mod(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mod(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.len2()"""
        return float._wrap(super(Vec2f, self).len2())

    @staticmethod
    @overload
    def add(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f._wrap(_Vec2f.add(arg0, arg1))

    @staticmethod
    @overload
    def mul(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f._wrap(_Vec2f.mul(arg0, arg1))

    @overload
    def floor(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.floor()"""
        return 'Vec2f'._wrap(super(Vec2f, self).floor())

    @overload
    def pow(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).pow(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def add(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).add(_float.valueOf(arg0)))

    @overload
    def pow(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).pow(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec2f, self).readExternal(arg0)

    @overload
    def set(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).set(arg0))

    @overload
    def clone(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.clone()"""
        return 'Vec2f'._wrap(super(Vec2f, self).clone())

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2f.dst(float,float)"""
        return float._wrap(super(_Vec2f, self).dst(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def div(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).div(_float.valueOf(arg0)))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(float,float)"""
        return float._wrap(super(_Vec2f, self).dot(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def div(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).div(arg0))

    @overload
    def sub(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).sub(_float.valueOf(arg0)))

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2f.d()"""
        return 'Vec2d'._wrap(super(Vec2f, self).d())

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).set(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).sub(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mul(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mul(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).add(arg0))

    @overload
    def nor(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.nor()"""
        return 'Vec2f'._wrap(super(Vec2f, self).nor())

    @overload
    def cpy(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.cpy()"""
        return 'Vec2f'._wrap(super(Vec2f, self).cpy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2f.hashCode()"""
        return int._wrap(super(Vec2f, self).hashCode())

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(float)"""
        return float._wrap(super(_Vec2f, self).dot(_float.valueOf(arg0)))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.setX(float)"""
        super(_Vec2f, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f()"""
        val = _Vec2f()
        self.__wrapper = val

    @overload
    def sub(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).sub(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f(float,float)"""
        val = _Vec2f(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def mod(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(float,float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mod(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mul(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(float)"""
        return 'Vec2f'._wrap(super(_Vec2f, self).mul(_float.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.vector.Vec4i as _Vec4i
_Vec4i = _Vec4i
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec4f as _Vec4f
_Vec4f = _Vec4f
import java.lang.Float as _float
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec4d as _Vec4d
_Vec4d = _Vec4d
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec4f():
    """dev.ultreon.libs.commons.v0.vector.Vec4f"""
 
    @staticmethod
    def _wrap(java_value: _Vec4f) -> 'Vec4f':
        return Vec4f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec4f):
        """
        Dynamic initializer for Vec4f.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec4f__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec4f__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sub(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).sub(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f()"""
        val = _Vec4f()
        self.__wrapper = val

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mod(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def floor(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.floor()"""
        return 'Vec4f'._wrap(super(Vec4f, self).floor())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f()"""
        val = _Vec4f()
        self.__wrapper = val

    @overload
    def add(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).add(_float.valueOf(arg0)))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4f.dst(float,float,float,float)"""
        return float._wrap(super(_Vec4f, self).dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec4f', arg1: 'Vec4f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float._wrap(_Vec4f.dot(arg0, arg1))

    @overload
    def div(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).div(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getX()"""
        return float._wrap(super(Vec4f, self).getX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4f.toString()"""
        return str._wrap(super(Vec4f, self).toString())

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).pow(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def pow(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).pow(_float.valueOf(arg0)))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec4f, self).writeExternal(arg0)

    @staticmethod
    @overload
    def mul(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f._wrap(_Vec4f.mul(arg0, arg1))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setY(float)"""
        super(_Vec4f, self).setY(_float.valueOf(arg0))

    @overload
    def clone(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.clone()"""
        return 'Vec4f'._wrap(super(Vec4f, self).clone())

    @staticmethod
    @overload
    def add(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f._wrap(_Vec4f.add(arg0, arg1))

    @overload
    def ceil(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.ceil()"""
        return 'Vec4f'._wrap(super(Vec4f, self).ceil())

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getY()"""
        return float._wrap(super(Vec4f, self).getY())

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(float)"""
        return float._wrap(super(_Vec4f, self).dot(_float.valueOf(arg0)))

    @overload
    def dec(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.dec()"""
        return 'Vec4f'._wrap(super(Vec4f, self).dec())

    @overload
    def dot(self, arg0: 'Vec4f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float._wrap(super(_Vec4f, self).dot(arg0))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mul(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setZ(float)"""
        super(_Vec4f, self).setZ(_float.valueOf(arg0))

    @overload
    def setW(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setW(float)"""
        super(_Vec4f, self).setW(_float.valueOf(arg0))

    @overload
    def abs(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.abs()"""
        return 'Vec4f'._wrap(super(Vec4f, self).abs())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mod(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mod(arg0))

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4f.i()"""
        return 'Vec4i'._wrap(super(Vec4f, self).i())

    @overload
    def inc(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.inc()"""
        return 'Vec4f'._wrap(super(Vec4f, self).inc())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec4f, self).readExternal(arg0)

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.f()"""
        return 'Vec4f'._wrap(super(Vec4f, self).f())

    @staticmethod
    @overload
    def div(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f._wrap(_Vec4f.div(arg0, arg1))

    @overload
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.len2()"""
        return float._wrap(super(Vec4f, self).len2())

    @overload
    def getZ(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getZ()"""
        return float._wrap(super(Vec4f, self).getZ())

    @overload
    def div(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).div(arg0))

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4f.d()"""
        return 'Vec4d'._wrap(super(Vec4f, self).d())

    @overload
    def mod(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mod(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f._wrap(_Vec4f.sub(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4f.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec4f, self).equals(arg0))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).sub(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def pow(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).pow(arg0))

    @overload
    def mul(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mul(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4f.pow(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4d._wrap(_Vec4f.pow(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4f.hashCode()"""
        return int._wrap(super(Vec4f, self).hashCode())

    @overload
    def neg(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.neg()"""
        return 'Vec4f'._wrap(super(Vec4f, self).neg())

    @overload
    def mul(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).mul(arg0))

    @overload
    def add(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).add(arg0))

    @overload
    def cpy(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.cpy()"""
        return 'Vec4f'._wrap(super(Vec4f, self).cpy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dst(self, arg0: 'Vec4f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4f.dst(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float._wrap(super(_Vec4f, self).dst(arg0))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setX(float)"""
        super(_Vec4f, self).setX(_float.valueOf(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(float,float,float,float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).set(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f(float,float,float,float)"""
        val = _Vec4f(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getW(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getW()"""
        return float._wrap(super(Vec4f, self).getW())

    @overload
    def div(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).div(_float.valueOf(arg0)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(float,float,float,float)"""
        return float._wrap(super(_Vec4f, self).dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def sub(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).sub(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(float)"""
        return 'Vec4f'._wrap(super(_Vec4f, self).set(_float.valueOf(arg0)))

    @overload
    def nor(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.nor()"""
        return 'Vec4f'._wrap(super(Vec4f, self).nor()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3f as _Vec3f
_Vec3f = _Vec3f
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.libs.commons.v0.vector.Vec3d as _Vec3d
_Vec3d = _Vec3d
import dev.ultreon.libs.commons.v0.vector.Vec3i as _Vec3i
_Vec3i = _Vec3i
import java.lang.Class as _Class
_Class = _Class
 
class Vec3f():
    """dev.ultreon.libs.commons.v0.vector.Vec3f"""
 
    @staticmethod
    def _wrap(java_value: _Vec3f) -> 'Vec3f':
        return Vec3f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec3f):
        """
        Dynamic initializer for Vec3f.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec3f__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec3f__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f(float,float,float)"""
        val = _Vec3f(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec3f, self).writeExternal(arg0)

    @overload
    def nor(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.nor()"""
        return 'Vec3f'._wrap(super(Vec3f, self).nor())

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).pow(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f()"""
        val = _Vec3f()
        self.__wrapper = val

    @overload
    def getZ(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getZ()"""
        return float._wrap(super(Vec3f, self).getZ())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f()"""
        val = _Vec3f()
        self.__wrapper = val

    @overload
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.len2()"""
        return float._wrap(super(Vec3f, self).len2())

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setY(float)"""
        super(_Vec3f, self).setY(_float.valueOf(arg0))

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
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).div(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def mod(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mod(_float.valueOf(arg0)))

    @overload
    def add(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).add(arg0))

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3f.i()"""
        return 'Vec3i'._wrap(super(Vec3f, self).i())

    @overload
    def mul(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mul(arg0))

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getY()"""
        return float._wrap(super(Vec3f, self).getY())

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.f()"""
        return 'Vec3f'._wrap(super(Vec3f, self).f())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec3f, self).readExternal(arg0)

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).set(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).set(_float.valueOf(arg0)))

    @overload
    def mul(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mul(_float.valueOf(arg0)))

    @overload
    def floor(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.floor()"""
        return 'Vec3f'._wrap(super(Vec3f, self).floor())

    @overload
    def sub(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).sub(_float.valueOf(arg0)))

    @overload
    def cpy(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.cpy()"""
        return 'Vec3f'._wrap(super(Vec3f, self).cpy())

    @staticmethod
    @overload
    def sub(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f._wrap(_Vec3f.sub(arg0, arg1))

    @overload
    def div(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).div(_float.valueOf(arg0)))

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mod(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sub(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).sub(arg0))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3f', arg1: 'Vec3f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float._wrap(_Vec3f.dot(arg0, arg1))

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setZ(float)"""
        super(_Vec3f, self).setZ(_float.valueOf(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(float,float,float)"""
        return float._wrap(super(_Vec3f, self).dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def dec(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.dec()"""
        return 'Vec3f'._wrap(super(Vec3f, self).dec())

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).sub(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3f.d()"""
        return 'Vec3d'._wrap(super(Vec3f, self).d())

    @overload
    def div(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).div(arg0))

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getX()"""
        return float._wrap(super(Vec3f, self).getX())

    @overload
    def pow(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).pow(arg0))

    @overload
    def ceil(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.ceil()"""
        return 'Vec3f'._wrap(super(Vec3f, self).ceil())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3f.toString()"""
        return str._wrap(super(Vec3f, self).toString())

    @overload
    def dot(self, arg0: 'Vec3f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float._wrap(super(_Vec3f, self).dot(arg0))

    @overload
    def add(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).add(_float.valueOf(arg0)))

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(float)"""
        return float._wrap(super(_Vec3f, self).dot(_float.valueOf(arg0)))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(float,float,float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mul(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def inc(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.inc()"""
        return 'Vec3f'._wrap(super(Vec3f, self).inc())

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setX(float)"""
        super(_Vec3f, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3f.hashCode()"""
        return int._wrap(super(Vec3f, self).hashCode())

    @overload
    def neg(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.neg()"""
        return 'Vec3f'._wrap(super(Vec3f, self).neg())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3f.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec3f, self).equals(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f._wrap(_Vec3f.div(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def pow(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3f.pow(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3d._wrap(_Vec3f.pow(arg0, arg1))

    @overload
    def pow(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(float)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).pow(_float.valueOf(arg0)))

    @overload
    def dst(self, arg0: 'Vec3f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3f.dst(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float._wrap(super(_Vec3f, self).dst(arg0))

    @staticmethod
    @overload
    def add(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f._wrap(_Vec3f.add(arg0, arg1))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3f.dst(float,float,float)"""
        return float._wrap(super(_Vec3f, self).dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def abs(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.abs()"""
        return 'Vec3f'._wrap(super(Vec3f, self).abs())

    @staticmethod
    @overload
    def mul(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f._wrap(_Vec3f.mul(arg0, arg1))

    @overload
    def clone(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.clone()"""
        return 'Vec3f'._wrap(super(Vec3f, self).clone())

    @overload
    def mod(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'._wrap(super(_Vec3f, self).mod(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.awt.Point as _Point
_Point = _Point
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.vector.Vec2d as _Vec2d
_Vec2d = _Vec2d
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import java.awt.Point as Point
import dev.ultreon.libs.commons.v0.vector.Vec2i as _Vec2i
_Vec2i = _Vec2i
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec2f as _Vec2f
_Vec2f = _Vec2f
import java.awt.Dimension as _Dimension
_Dimension = _Dimension
import java.awt.Dimension as Dimension
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec2i():
    """dev.ultreon.libs.commons.v0.vector.Vec2i"""
 
    @staticmethod
    def _wrap(java_value: _Vec2i) -> 'Vec2i':
        return Vec2i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec2i):
        """
        Dynamic initializer for Vec2i.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec2i__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec2i__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.i()"""
        return 'Vec2i'._wrap(super(Vec2i, self).i())

    @overload
    def set(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).set(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i._wrap(_Vec2i.div(arg0, arg1))

    @overload
    def pow(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).pow(arg0))

    @overload
    def add(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).add(_int.valueOf(arg0)))

    @overload
    def pow(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).pow(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def inc(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.inc()"""
        return 'Vec2i'._wrap(super(Vec2i, self).inc())

    @overload
    def div(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).div(_int.valueOf(arg0)))

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
    def sub(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).sub(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2i.toString()"""
        return str._wrap(super(Vec2i, self).toString())

    @overload
    def __init__(self, arg0: 'Point'):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i(java.awt.Point)"""
        val = _Vec2i(arg0)
        self.__wrapper = val

    @overload
    def mod(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mod(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i(int,int)"""
        val = _Vec2i(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.hashCode()"""
        return int._wrap(super(Vec2i, self).hashCode())

    @staticmethod
    @overload
    def sub(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i._wrap(_Vec2i.sub(arg0, arg1))

    @overload
    def abs(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.abs()"""
        return 'Vec2i'._wrap(super(Vec2i, self).abs())

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(int)"""
        return int._wrap(super(_Vec2i, self).dot(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i()"""
        val = _Vec2i()
        self.__wrapper = val

    @overload
    def dot(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(int,int)"""
        return int._wrap(super(_Vec2i, self).dot(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2i.pow(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2d._wrap(_Vec2i.pow(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.setY(int)"""
        super(_Vec2i, self).setY(_int.valueOf(arg0))

    @overload
    def pow(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).pow(_int.valueOf(arg0)))

    @overload
    def mul(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mul(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2i.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec2i, self).equals(arg0))

    @overload
    def toAwtPoint(self) -> 'Point':
        """public java.awt.Point dev.ultreon.libs.commons.v0.vector.Vec2i.toAwtPoint()"""
        return 'Point'._wrap(super(Vec2i, self).toAwtPoint())

    @staticmethod
    @overload
    def dot(arg0: 'Vec2i', arg1: 'Vec2i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return int._wrap(_Vec2i.dot(arg0, arg1))

    @overload
    def add(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).add(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def toAwtDimension(self) -> 'Dimension':
        """public java.awt.Dimension dev.ultreon.libs.commons.v0.vector.Vec2i.toAwtDimension()"""
        return 'Dimension'._wrap(super(Vec2i, self).toAwtDimension())

    @overload
    def add(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).add(arg0))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.getX()"""
        return int._wrap(super(Vec2i, self).getX())

    @overload
    def neg(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.neg()"""
        return 'Vec2i'._wrap(super(Vec2i, self).neg())

    @overload
    def mul(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mul(_int.valueOf(arg0)))

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2i.f()"""
        return 'Vec2f'._wrap(super(Vec2i, self).f())

    @overload
    def div(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).div(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def add(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i._wrap(_Vec2i.add(arg0, arg1))

    @overload
    def dot(self, arg0: 'Vec2i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return int._wrap(super(_Vec2i, self).dot(arg0))

    @overload
    def dec(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.dec()"""
        return 'Vec2i'._wrap(super(Vec2i, self).dec())

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.getY()"""
        return int._wrap(super(Vec2i, self).getY())

    @overload
    def sub(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).sub(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def mul(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mul(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec2i, self).readExternal(arg0)

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.setX(int)"""
        super(_Vec2i, self).setX(_int.valueOf(arg0))

    @overload
    def set(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).set(_int.valueOf(arg0)))

    @overload
    def sub(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).sub(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i()"""
        val = _Vec2i()
        self.__wrapper = val

    @overload
    def dst(self, arg0: int, arg1: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2i.dst(int,int)"""
        return float._wrap(super(_Vec2i, self).dst(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i._wrap(_Vec2i.mul(arg0, arg1))

    @overload
    def mod(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mod(_int.valueOf(arg0)))

    @overload
    def clone(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.clone()"""
        return 'Vec2i'._wrap(super(Vec2i, self).clone())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec2i, self).writeExternal(arg0)

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2i.d()"""
        return 'Vec2d'._wrap(super(Vec2i, self).d())

    @overload
    def mod(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).mod(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def dst(self, arg0: 'Vec2i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2i.dst(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return float._wrap(super(_Vec2i, self).dst(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(int,int)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def div(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'._wrap(super(_Vec2i, self).div(arg0))

    @overload
    def cpy(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.cpy()"""
        return 'Vec2i'._wrap(super(Vec2i, self).cpy()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4d
from builtins import str
import java.lang.Double as _double
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.commons.v0.vector.Vec4i as _Vec4i
_Vec4i = _Vec4i
from builtins import type
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.vector.Vec4f as _Vec4f
_Vec4f = _Vec4f
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.vector.Vec4d as _Vec4d
_Vec4d = _Vec4d
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vec4d():
    """dev.ultreon.libs.commons.v0.vector.Vec4d"""
 
    @staticmethod
    def _wrap(java_value: _Vec4d) -> 'Vec4d':
        return Vec4d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vec4d):
        """
        Dynamic initializer for Vec4d.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vec4d__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vec4d__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d(double,double,double,double)"""
        val = _Vec4d(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3))
        self.__wrapper = val

    @staticmethod
    @overload
    def pow(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d._wrap(_Vec4d.pow(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setX(double)"""
        super(_Vec4d, self).setX(_double.valueOf(arg0))

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4d.f()"""
        return 'Vec4f'._wrap(super(Vec4d, self).f())

    @overload
    def div(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).div(_double.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4d.hashCode()"""
        return int._wrap(super(Vec4d, self).hashCode())

    @overload
    def pow(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).pow(arg0))

    @overload
    def set(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).set(arg0))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(_Vec4d, self).writeExternal(arg0)

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
    def sub(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).sub(_double.valueOf(arg0)))

    @overload
    def div(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).div(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mul(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def div(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).div(arg0))

    @overload
    def dst(self, arg0: 'Vec4d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dst(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float._wrap(super(_Vec4d, self).dst(arg0))

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setZ(double)"""
        super(_Vec4d, self).setZ(_double.valueOf(arg0))

    @overload
    def floor(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.floor()"""
        return 'Vec4d'._wrap(super(Vec4d, self).floor())

    @overload
    def add(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).add(arg0))

    @staticmethod
    @overload
    def dot(arg0: 'Vec4d', arg1: 'Vec4d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float._wrap(_Vec4d.dot(arg0, arg1))

    @overload
    def dec(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.dec()"""
        return 'Vec4d'._wrap(super(Vec4d, self).dec())

    @staticmethod
    @overload
    def add(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d._wrap(_Vec4d.add(arg0, arg1))

    @overload
    def add(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).add(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d._wrap(_Vec4d.mul(arg0, arg1))

    @overload
    def inc(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.inc()"""
        return 'Vec4d'._wrap(super(Vec4d, self).inc())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4d.equals(java.lang.Object)"""
        return bool._wrap(super(_Vec4d, self).equals(arg0))

    @overload
    def abs(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.abs()"""
        return 'Vec4d'._wrap(super(Vec4d, self).abs())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(_Vec4d, self).readExternal(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d()"""
        val = _Vec4d()
        self.__wrapper = val

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(double)"""
        return float._wrap(super(_Vec4d, self).dot(_double.valueOf(arg0)))

    @overload
    def ceil(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.ceil()"""
        return 'Vec4d'._wrap(super(Vec4d, self).ceil())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mul(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mul(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d._wrap(_Vec4d.div(arg0, arg1))

    @overload
    def sub(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).sub(arg0))

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getX()"""
        return float._wrap(super(Vec4d, self).getX())

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getY()"""
        return float._wrap(super(Vec4d, self).getY())

    @overload
    def getW(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getW()"""
        return float._wrap(super(Vec4d, self).getW())

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getZ()"""
        return float._wrap(super(Vec4d, self).getZ())

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4d.i()"""
        return 'Vec4i'._wrap(super(Vec4d, self).i())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4d.toString()"""
        return str._wrap(super(Vec4d, self).toString())

    @overload
    def mod(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mod(_double.valueOf(arg0)))

    @overload
    def set(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).set(_double.valueOf(arg0)))

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mod(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).sub(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def neg(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.neg()"""
        return 'Vec4d'._wrap(super(Vec4d, self).neg())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d()"""
        val = _Vec4d()
        self.__wrapper = val

    @overload
    def cpy(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.cpy()"""
        return 'Vec4d'._wrap(super(Vec4d, self).cpy())

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setY(double)"""
        super(_Vec4d, self).setY(_double.valueOf(arg0))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).add(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.d()"""
        return 'Vec4d'._wrap(super(Vec4d, self).d())

    @overload
    def pow(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).pow(_double.valueOf(arg0)))

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.len2()"""
        return float._wrap(super(Vec4d, self).len2())

    @staticmethod
    @overload
    def sub(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d._wrap(_Vec4d.sub(arg0, arg1))

    @overload
    def dot(self, arg0: 'Vec4d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float._wrap(super(_Vec4d, self).dot(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).set(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(double,double,double,double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).pow(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dst(double,double,double,double)"""
        return float._wrap(super(_Vec4d, self).dst(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @overload
    def mul(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(double)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mul(_double.valueOf(arg0)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(double,double,double,double)"""
        return float._wrap(super(_Vec4d, self).dot(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def clone(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.clone()"""
        return 'Vec4d'._wrap(super(Vec4d, self).clone())

    @overload
    def nor(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.nor()"""
        return 'Vec4d'._wrap(super(Vec4d, self).nor())

    @overload
    def mod(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'._wrap(super(_Vec4d, self).mod(arg0))

    @overload
    def setW(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setW(double)"""
        super(_Vec4d, self).setW(_double.valueOf(arg0))