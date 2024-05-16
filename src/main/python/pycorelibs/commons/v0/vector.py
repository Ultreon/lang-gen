from __future__ import annotations
from overload import overload


 
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
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
 
class Vec3d(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec3d"""
 
    @staticmethod
    def __wrap(java_value: __Vec3d) -> 'Vec3d':
        return Vec3d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec3d):
        """
        Dynamic initializer for Vec3d.
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
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec3d, self).writeExternal(arg0)

    @overload
    def nor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.nor()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).nor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3d.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec3d, self).equals(arg0))

    @overload
    def neg(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.neg()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).neg())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def pow(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(__double.valueOf(arg0)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double,double,double)"""
        return float.__wrap(super(__Vec3d, self).dot(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.mul(arg0, arg1))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def abs(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.abs()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).abs())

    @overload
    def sub(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(arg0))

    @overload
    def dot(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(super(__Vec3d, self).dot(arg0))

    @overload
    def floor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.floor()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).floor())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d(double,double,double)"""
        val = __Vec3d(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(double,double,double)"""
        return float.__wrap(super(__Vec3d, self).dst(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.sub(arg0, arg1))

    @overload
    def dec(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.dec()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).dec())

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getY()"""
        return float.__wrap(super(Vec3d, self).getY())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3d.hashCode()"""
        return int.__wrap(super(Vec3d, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = __Vec3d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getZ()"""
        return float.__wrap(super(Vec3d, self).getZ())

    @overload
    def add(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(__double.valueOf(arg0)))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.d()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).d())

    @overload
    def mod(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(arg0))

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getX()"""
        return float.__wrap(super(Vec3d, self).getX())

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.len2()"""
        return float.__wrap(super(Vec3d, self).len2())

    @staticmethod
    @overload
    def add(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.add(arg0, arg1))

    @overload
    def inc(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.inc()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).inc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3d.i()"""
        return 'Vec3i'.__wrap(super(Vec3d, self).i())

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setX(double)"""
        super(__Vec3d, self).setX(__double.valueOf(arg0))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.pow(arg0, arg1))

    @overload
    def mul(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mod(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(__double.valueOf(arg0)))

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double)"""
        return float.__wrap(super(__Vec3d, self).dot(__double.valueOf(arg0)))

    @overload
    def div(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(__double.valueOf(arg0)))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec3d, self).readExternal(arg0)

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setZ(double)"""
        super(__Vec3d, self).setZ(__double.valueOf(arg0))

    @overload
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def add(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(arg0))

    @overload
    def clone(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.clone()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).clone())

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3d.f()"""
        return 'Vec3f'.__wrap(super(Vec3d, self).f())

    @overload
    def pow(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = __Vec3d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ceil(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.ceil()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).ceil())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def div(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.div(arg0, arg1))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3d.toString()"""
        return str.__wrap(super(Vec3d, self).toString())

    @overload
    def dst(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(super(__Vec3d, self).dst(arg0))

    @overload
    def set(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(arg0))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setY(double)"""
        super(__Vec3d, self).setY(__double.valueOf(arg0))

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
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3d', arg1: 'Vec3d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(__Vec3d.dot(arg0, arg1))

    @overload
    def div(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(arg0))

    @overload
    def mul(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(arg0))

    @overload
    def cpy(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.cpy()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).cpy())

    @overload
    def set(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(__double.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3d
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
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
 
class Vec3d(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec3d"""
 
    @staticmethod
    def __wrap(java_value: __Vec3d) -> 'Vec3d':
        return Vec3d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec3d):
        """
        Dynamic initializer for Vec3d.
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
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec3d, self).writeExternal(arg0)

    @overload
    def nor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.nor()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).nor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3d.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec3d, self).equals(arg0))

    @overload
    def neg(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.neg()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).neg())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def pow(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(__double.valueOf(arg0)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double,double,double)"""
        return float.__wrap(super(__Vec3d, self).dot(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def sub(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.mul(arg0, arg1))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def abs(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.abs()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).abs())

    @overload
    def sub(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).sub(arg0))

    @overload
    def dot(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(super(__Vec3d, self).dot(arg0))

    @overload
    def floor(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.floor()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).floor())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d(double,double,double)"""
        val = __Vec3d(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(double,double,double)"""
        return float.__wrap(super(__Vec3d, self).dst(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.sub(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.sub(arg0, arg1))

    @overload
    def dec(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.dec()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).dec())

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getY()"""
        return float.__wrap(super(Vec3d, self).getY())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3d.hashCode()"""
        return int.__wrap(super(Vec3d, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = __Vec3d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getZ()"""
        return float.__wrap(super(Vec3d, self).getZ())

    @overload
    def add(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(__double.valueOf(arg0)))

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.d()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).d())

    @overload
    def mod(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(arg0))

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.getX()"""
        return float.__wrap(super(Vec3d, self).getX())

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.len2()"""
        return float.__wrap(super(Vec3d, self).len2())

    @staticmethod
    @overload
    def add(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.add(arg0, arg1))

    @overload
    def inc(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.inc()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).inc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3d.i()"""
        return 'Vec3i'.__wrap(super(Vec3d, self).i())

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setX(double)"""
        super(__Vec3d, self).setX(__double.valueOf(arg0))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.pow(arg0, arg1))

    @overload
    def mul(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mod(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(__double.valueOf(arg0)))

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(double)"""
        return float.__wrap(super(__Vec3d, self).dot(__double.valueOf(arg0)))

    @overload
    def div(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(__double.valueOf(arg0)))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec3d, self).readExternal(arg0)

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setZ(double)"""
        super(__Vec3d, self).setZ(__double.valueOf(arg0))

    @overload
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def add(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(arg0))

    @overload
    def clone(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.clone()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).clone())

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3d.f()"""
        return 'Vec3f'.__wrap(super(Vec3d, self).f())

    @overload
    def pow(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3d()"""
        val = __Vec3d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ceil(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.ceil()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).ceil())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mod(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mod(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def div(arg0: 'Vec3d', arg1: 'Vec3d') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return Vec3d.__wrap(__Vec3d.div(arg0, arg1))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.add(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).add(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3d.toString()"""
        return str.__wrap(super(Vec3d, self).toString())

    @overload
    def dst(self, arg0: 'Vec3d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3d.dst(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(super(__Vec3d, self).dst(arg0))

    @overload
    def set(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(arg0))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3d.setY(double)"""
        super(__Vec3d, self).setY(__double.valueOf(arg0))

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
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.pow(double,double,double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).pow(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3d', arg1: 'Vec3d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec3d.dot(dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return float.__wrap(__Vec3d.dot(arg0, arg1))

    @overload
    def div(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.div(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).div(arg0))

    @overload
    def mul(self, arg0: 'Vec3d') -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.mul(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).mul(arg0))

    @overload
    def cpy(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.cpy()"""
        return 'Vec3d'.__wrap(super(Vec3d, self).cpy())

    @overload
    def set(self, arg0: float) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3d.set(double)"""
        return 'Vec3d'.__wrap(super(__Vec3d, self).set(__double.valueOf(arg0)))

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3d 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
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
 
class Vec3i(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec3i"""
 
    @staticmethod
    def __wrap(java_value: __Vec3i) -> 'Vec3i':
        return Vec3i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec3i):
        """
        Dynamic initializer for Vec3i.
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
    def clone(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.clone()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).clone())

    @overload
    def sub(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).sub(__int.valueOf(arg0)))

    @overload
    def mul(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mul(__int.valueOf(arg0)))

    @overload
    def mod(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mod(arg0))

    @overload
    def dst(self, arg0: 'Vec3i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3i.dst(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return float.__wrap(super(__Vec3i, self).dst(arg0))

    @overload
    def div(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).div(__int.valueOf(arg0)))

    @overload
    def sub(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).sub(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).set(arg0))

    @overload
    def add(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).add(__int.valueOf(arg0)))

    @overload
    def getZ(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getZ()"""
        return int.__wrap(super(Vec3i, self).getZ())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mod(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mod(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i()"""
        val = __Vec3i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getY()"""
        return int.__wrap(super(Vec3i, self).getY())

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3i.dst(int,int,int)"""
        return float.__wrap(super(__Vec3i, self).dst(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i()"""
        val = __Vec3i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).add(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def pow(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).pow(arg0))

    @overload
    def dec(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.dec()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).dec())

    @overload
    def dot(self, arg0: int, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(int,int,int)"""
        return int.__wrap(super(__Vec3i, self).dot(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(int)"""
        return int.__wrap(super(__Vec3i, self).dot(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).set(__int.valueOf(arg0)))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.getX()"""
        return int.__wrap(super(Vec3i, self).getX())

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setY(int)"""
        super(__Vec3i, self).setY(__int.valueOf(arg0))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3i.pow(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3d.__wrap(__Vec3i.pow(arg0, arg1))

    @overload
    def div(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).div(arg0))

    @overload
    def mod(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mod(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mod(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def inc(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.inc()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).inc())

    @staticmethod
    @overload
    def div(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i.__wrap(__Vec3i.div(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.set(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def pow(self, arg0: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).pow(__int.valueOf(arg0)))

    @overload
    def setZ(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setZ(int)"""
        super(__Vec3i, self).setZ(__int.valueOf(arg0))

    @overload
    def mul(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mul(arg0))

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3i.f()"""
        return 'Vec3f'.__wrap(super(Vec3i, self).f())

    @overload
    def abs(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.abs()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).abs())

    @staticmethod
    @overload
    def add(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i.__wrap(__Vec3i.add(arg0, arg1))

    @overload
    def dot(self, arg0: 'Vec3i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(super(__Vec3i, self).dot(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec3i, self).readExternal(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec3i(int,int,int)"""
        val = __Vec3i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3i.toString()"""
        return str.__wrap(super(Vec3i, self).toString())

    @overload
    def add(self, arg0: 'Vec3i') -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.add(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).add(arg0))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i.__wrap(__Vec3i.sub(arg0, arg1))

    @staticmethod
    @overload
    def dot(arg0: 'Vec3i', arg1: 'Vec3i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec3i.dot(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return int.__wrap(__Vec3i.dot(arg0, arg1))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec3i, self).writeExternal(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3i.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec3i, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3i.hashCode()"""
        return int.__wrap(super(Vec3i, self).hashCode())

    @overload
    def mul(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).mul(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def div(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.div(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).div(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def pow(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.pow(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).pow(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3i', arg1: 'Vec3i') -> 'Vec3i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.mul(dev.ultreon.libs.commons.v0.vector.Vec3i,dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return Vec3i.__wrap(__Vec3i.mul(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3i.d()"""
        return 'Vec3d'.__wrap(super(Vec3i, self).d())

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3i.setX(int)"""
        super(__Vec3i, self).setX(__int.valueOf(arg0))

    @overload
    def neg(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.neg()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).neg())

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.i()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).i())

    @overload
    def cpy(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.cpy()"""
        return 'Vec3i'.__wrap(super(Vec3i, self).cpy())

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3i.sub(int,int,int)"""
        return 'Vec3i'.__wrap(super(__Vec3i, self).sub(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec4i as __Vec4i
__Vec4i = __Vec4i
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec4f as __Vec4f
__Vec4f = __Vec4f
import dev.ultreon.libs.commons.v0.vector.Vec4d as __Vec4d
__Vec4d = __Vec4d
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
 
class Vec4i(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec4i"""
 
    @staticmethod
    def __wrap(java_value: __Vec4i) -> 'Vec4i':
        return Vec4i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec4i):
        """
        Dynamic initializer for Vec4i.
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
    def neg(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.neg()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).neg())

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.i()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).i())

    @staticmethod
    @overload
    def pow(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4i.pow(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4d.__wrap(__Vec4i.pow(arg0, arg1))

    @overload
    def dot(self, arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(int,int,int,int)"""
        return int.__wrap(super(__Vec4i, self).dot(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4i.d()"""
        return 'Vec4d'.__wrap(super(Vec4i, self).d())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4i.dst(int,int,int,int)"""
        return float.__wrap(super(__Vec4i, self).dst(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setY(int)"""
        super(__Vec4i, self).setY(__int.valueOf(arg0))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getY()"""
        return int.__wrap(super(Vec4i, self).getY())

    @staticmethod
    @overload
    def dot(arg0: 'Vec4i', arg1: 'Vec4i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return int.__wrap(__Vec4i.dot(arg0, arg1))

    @overload
    def pow(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).pow(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setX(int)"""
        super(__Vec4i, self).setX(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def abs(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.abs()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).abs())

    @overload
    def dot(self, arg0: 'Vec4i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return int.__wrap(super(__Vec4i, self).dot(arg0))

    @overload
    def pow(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).pow(arg0))

    @overload
    def mul(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mul(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getX()"""
        return int.__wrap(super(Vec4i, self).getX())

    @overload
    def mod(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mod(arg0))

    @overload
    def pow(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.pow(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).pow(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i.__wrap(__Vec4i.sub(arg0, arg1))

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.dot(int)"""
        return int.__wrap(super(__Vec4i, self).dot(__int.valueOf(arg0)))

    @overload
    def setW(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setW(int)"""
        super(__Vec4i, self).setW(__int.valueOf(arg0))

    @overload
    def setZ(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.setZ(int)"""
        super(__Vec4i, self).setZ(__int.valueOf(arg0))

    @overload
    def dst(self, arg0: 'Vec4i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4i.dst(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return float.__wrap(super(__Vec4i, self).dst(arg0))

    @overload
    def getW(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getW()"""
        return int.__wrap(super(Vec4i, self).getW())

    @overload
    def add(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).add(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i()"""
        val = __Vec4i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def cpy(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.cpy()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).cpy())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4i.toString()"""
        return str.__wrap(super(Vec4i, self).toString())

    @overload
    def div(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).div(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i.__wrap(__Vec4i.mul(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def add(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i.__wrap(__Vec4i.add(arg0, arg1))

    @overload
    def add(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).add(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).set(__int.valueOf(arg0)))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec4i, self).readExternal(arg0)

    @overload
    def div(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).div(arg0))

    @overload
    def mod(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mod(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def clone(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.clone()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).clone())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i(int,int,int,int)"""
        val = __Vec4i(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mul(__int.valueOf(arg0)))

    @overload
    def sub(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).sub(__int.valueOf(arg0)))

    @overload
    def inc(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.inc()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).inc())

    @overload
    def set(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.set(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).set(arg0))

    @overload
    def mul(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mul(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mul(arg0))

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4i.f()"""
        return 'Vec4f'.__wrap(super(Vec4i, self).f())

    @overload
    def div(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).div(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4i()"""
        val = __Vec4i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.add(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).add(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def div(arg0: 'Vec4i', arg1: 'Vec4i') -> 'Vec4i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.div(dev.ultreon.libs.commons.v0.vector.Vec4i,dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return Vec4i.__wrap(__Vec4i.div(arg0, arg1))

    @overload
    def sub(self, arg0: 'Vec4i') -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).sub(arg0))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.hashCode()"""
        return int.__wrap(super(Vec4i, self).hashCode())

    @overload
    def mod(self, arg0: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.mod(int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).mod(__int.valueOf(arg0)))

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.sub(int,int,int,int)"""
        return 'Vec4i'.__wrap(super(__Vec4i, self).sub(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def getZ(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4i.getZ()"""
        return int.__wrap(super(Vec4i, self).getZ())

    @overload
    def dec(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4i.dec()"""
        return 'Vec4i'.__wrap(super(Vec4i, self).dec())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4i.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec4i, self).equals(arg0))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec4i, self).writeExternal(arg0) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2d
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vec2d(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec2d"""
 
    @staticmethod
    def __wrap(java_value: __Vec2d) -> 'Vec2d':
        return Vec2d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec2d):
        """
        Dynamic initializer for Vec2d.
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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d()"""
        val = __Vec2d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mul(__double.valueOf(arg0)))

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).set(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.len2()"""
        return float.__wrap(super(Vec2d, self).len2())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).set(__double.valueOf(arg0)))

    @overload
    def dot(self, arg0: 'Vec2d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float.__wrap(super(__Vec2d, self).dot(arg0))

    @overload
    def mul(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mul(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2d.hashCode()"""
        return int.__wrap(super(Vec2d, self).hashCode())

    @staticmethod
    @overload
    def sub(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d.__wrap(__Vec2d.sub(arg0, arg1))

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec2d, self).writeExternal(arg0)

    @overload
    def mod(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mod(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2d.toString()"""
        return str.__wrap(super(Vec2d, self).toString())

    @overload
    def pow(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).pow(arg0))

    @overload
    def cpy(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.cpy()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).cpy())

    @overload
    def add(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).add(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.setY(double)"""
        super(__Vec2d, self).setY(__double.valueOf(arg0))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).sub(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.d()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).d())

    @overload
    def abs(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.abs()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).abs())

    @overload
    def add(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).add(arg0))

    @overload
    def div(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).div(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2d.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec2d, self).equals(arg0))

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.getY()"""
        return float.__wrap(super(Vec2d, self).getY())

    @overload
    def ceil(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.ceil()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).ceil())

    @staticmethod
    @overload
    def div(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d.__wrap(__Vec2d.div(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.clone()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).clone())

    @overload
    def add(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).add(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec2d', arg1: 'Vec2d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float.__wrap(__Vec2d.dot(arg0, arg1))

    @overload
    def sub(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).sub(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(double)"""
        return float.__wrap(super(__Vec2d, self).dot(__double.valueOf(arg0)))

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.getX()"""
        return float.__wrap(super(Vec2d, self).getX())

    @overload
    def nor(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.nor()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).nor())

    @overload
    def set(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.set(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).set(arg0))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.setX(double)"""
        super(__Vec2d, self).setX(__double.valueOf(arg0))

    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2d.i()"""
        return 'Vec2i'.__wrap(super(Vec2d, self).i())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec2d, self).readExternal(arg0)

    @overload
    def dst(self, arg0: 'Vec2d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dst(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return float.__wrap(super(__Vec2d, self).dst(arg0))

    @overload
    def mod(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mod(__double.valueOf(arg0)))

    @overload
    def div(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).div(arg0))

    @overload
    def mod(self, arg0: 'Vec2d') -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mod(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mod(arg0))

    @overload
    def neg(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.neg()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).neg())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d()"""
        val = __Vec2d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def pow(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d.__wrap(__Vec2d.pow(arg0, arg1))

    @overload
    def floor(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.floor()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).floor())

    @overload
    def dec(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.dec()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).dec())

    @overload
    def div(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.div(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).div(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def add(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.add(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d.__wrap(__Vec2d.add(arg0, arg1))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec2d(double,double)"""
        val = __Vec2d(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.sub(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).sub(__double.valueOf(arg0)))

    @overload
    def mul(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).mul(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def inc(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.inc()"""
        return 'Vec2d'.__wrap(super(Vec2d, self).inc())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def pow(self, arg0: float, arg1: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(double,double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).pow(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dst(double,double)"""
        return float.__wrap(super(__Vec2d, self).dst(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2d.f()"""
        return 'Vec2f'.__wrap(super(Vec2d, self).f())

    @overload
    def pow(self, arg0: float) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.pow(double)"""
        return 'Vec2d'.__wrap(super(__Vec2d, self).pow(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def mul(arg0: 'Vec2d', arg1: 'Vec2d') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2d.mul(dev.ultreon.libs.commons.v0.vector.Vec2d,dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        return Vec2d.__wrap(__Vec2d.mul(arg0, arg1))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2d.dot(double,double)"""
        return float.__wrap(super(__Vec2d, self).dot(__double.valueOf(arg0), __double.valueOf(arg1))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec3f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.io.ObjectOutput as ObjectOutput
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vec3f(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec3f"""
 
    @staticmethod
    def __wrap(java_value: __Vec3f) -> 'Vec3f':
        return Vec3f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec3f):
        """
        Dynamic initializer for Vec3f.
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
    def pow(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).pow(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def sub(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).sub(__float.valueOf(arg0)))

    @overload
    def mul(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mul(__float.valueOf(arg0)))

    @overload
    def nor(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.nor()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).nor())

    @overload
    def add(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).add(__float.valueOf(arg0)))

    @overload
    def neg(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.neg()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).neg())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mod(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mod(__float.valueOf(arg0)))

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setZ(float)"""
        super(__Vec3f, self).setZ(__float.valueOf(arg0))

    @overload
    def dot(self, arg0: 'Vec3f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float.__wrap(super(__Vec3f, self).dot(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).set(__float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mul(arg0))

    @overload
    def i(self) -> 'Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.libs.commons.v0.vector.Vec3f.i()"""
        return 'Vec3i'.__wrap(super(Vec3f, self).i())

    @overload
    def abs(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.abs()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).abs())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def d(self) -> 'Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3f.d()"""
        return 'Vec3d'.__wrap(super(Vec3f, self).d())

    @overload
    def clone(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.clone()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).clone())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mod(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.len2()"""
        return float.__wrap(super(Vec3f, self).len2())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec3f.toString()"""
        return str.__wrap(super(Vec3f, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec3f.hashCode()"""
        return int.__wrap(super(Vec3f, self).hashCode())

    @overload
    def dst(self, arg0: 'Vec3f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3f.dst(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float.__wrap(super(__Vec3f, self).dst(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f.__wrap(__Vec3f.div(arg0, arg1))

    @overload
    def pow(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).pow(__float.valueOf(arg0)))

    @overload
    def div(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).div(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(float)"""
        return float.__wrap(super(__Vec3f, self).dot(__float.valueOf(arg0)))

    @overload
    def getZ(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getZ()"""
        return float.__wrap(super(Vec3f, self).getZ())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def dec(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.dec()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).dec())

    @staticmethod
    @overload
    def dot(arg0: 'Vec3f', arg1: 'Vec3f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return float.__wrap(__Vec3f.dot(arg0, arg1))

    @staticmethod
    @overload
    def pow(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.libs.commons.v0.vector.Vec3f.pow(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3d.__wrap(__Vec3f.pow(arg0, arg1))

    @overload
    def f(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.f()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).f())

    @overload
    def inc(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.inc()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).inc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getX()"""
        return float.__wrap(super(Vec3f, self).getX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ceil(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.ceil()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).ceil())

    @overload
    def sub(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).sub(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f()"""
        val = __Vec3f()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def floor(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.floor()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).floor())

    @overload
    def mod(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mod(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mod(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f.__wrap(__Vec3f.mul(arg0, arg1))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).sub(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.set(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).set(arg0))

    @overload
    def div(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).div(arg0))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setY(float)"""
        super(__Vec3f, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec3f, self).readExternal(arg0)

    @overload
    def pow(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.pow(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).pow(arg0))

    @overload
    def div(self, arg0: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.div(float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).div(__float.valueOf(arg0)))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.setX(float)"""
        super(__Vec3f, self).setX(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f(float,float,float)"""
        val = __Vec3f(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec3f.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec3f, self).equals(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.dot(float,float,float)"""
        return float.__wrap(super(__Vec3f, self).dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Vec3f') -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).add(arg0))

    @staticmethod
    @overload
    def add(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f.__wrap(__Vec3f.add(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec3f.dst(float,float,float)"""
        return float.__wrap(super(__Vec3f, self).dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec3f.getY()"""
        return float.__wrap(super(Vec3f, self).getY())

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec3f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec3f, self).writeExternal(arg0)

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.mul(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).mul(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def sub(arg0: 'Vec3f', arg1: 'Vec3f') -> 'Vec3f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.sub(dev.ultreon.libs.commons.v0.vector.Vec3f,dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        return Vec3f.__wrap(__Vec3f.sub(arg0, arg1))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.add(float,float,float)"""
        return 'Vec3f'.__wrap(super(__Vec3f, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def cpy(self) -> 'Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.libs.commons.v0.vector.Vec3f.cpy()"""
        return 'Vec3f'.__wrap(super(Vec3f, self).cpy())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec3f()"""
        val = __Vec3f()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec4i as __Vec4i
__Vec4i = __Vec4i
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec4f as __Vec4f
__Vec4f = __Vec4f
import dev.ultreon.libs.commons.v0.vector.Vec4d as __Vec4d
__Vec4d = __Vec4d
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vec4f(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec4f"""
 
    @staticmethod
    def __wrap(java_value: __Vec4f) -> 'Vec4f':
        return Vec4f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec4f):
        """
        Dynamic initializer for Vec4f.
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
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.len2()"""
        return float.__wrap(super(Vec4f, self).len2())

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4f.dst(float,float,float,float)"""
        return float.__wrap(super(__Vec4f, self).dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setX(float)"""
        super(__Vec4f, self).setX(__float.valueOf(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f.__wrap(__Vec4f.div(arg0, arg1))

    @staticmethod
    @overload
    def mul(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f.__wrap(__Vec4f.mul(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sub(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f.__wrap(__Vec4f.sub(arg0, arg1))

    @overload
    def div(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).div(arg0))

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.f()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).f())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f()"""
        val = __Vec4f()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def pow(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4f.pow(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4d.__wrap(__Vec4f.pow(arg0, arg1))

    @overload
    def sub(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).sub(arg0))

    @overload
    def getZ(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getZ()"""
        return float.__wrap(super(Vec4f, self).getZ())

    @staticmethod
    @overload
    def add(arg0: 'Vec4f', arg1: 'Vec4f') -> 'Vec4f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return Vec4f.__wrap(__Vec4f.add(arg0, arg1))

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(float)"""
        return float.__wrap(super(__Vec4f, self).dot(__float.valueOf(arg0)))

    @overload
    def dst(self, arg0: 'Vec4f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4f.dst(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float.__wrap(super(__Vec4f, self).dst(arg0))

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).pow(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def clone(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.clone()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).clone())

    @overload
    def mul(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mul(arg0))

    @overload
    def set(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).set(arg0))

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getX()"""
        return float.__wrap(super(Vec4f, self).getX())

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mod(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def cpy(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.cpy()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).cpy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4f.hashCode()"""
        return int.__wrap(super(Vec4f, self).hashCode())

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).sub(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def sub(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.sub(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).sub(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def nor(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.nor()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).nor())

    @overload
    def div(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).div(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f(float,float,float,float)"""
        val = __Vec4f(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mod(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mod(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mul(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mul(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.set(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).set(__float.valueOf(arg0)))

    @overload
    def add(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).add(arg0))

    @overload
    def neg(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.neg()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).neg())

    @overload
    def pow(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).pow(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(float,float,float,float)"""
        return float.__wrap(super(__Vec4f, self).dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4f()"""
        val = __Vec4f()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def div(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.div(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).div(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setW(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setW(float)"""
        super(__Vec4f, self).setW(__float.valueOf(arg0))

    @overload
    def abs(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.abs()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).abs())

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec4f, self).writeExternal(arg0)

    @overload
    def inc(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.inc()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).inc())

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4f.i()"""
        return 'Vec4i'.__wrap(super(Vec4f, self).i())

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getY()"""
        return float.__wrap(super(Vec4f, self).getY())

    @overload
    def ceil(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.ceil()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).ceil())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec4f, self).readExternal(arg0)

    @overload
    def pow(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.pow(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).pow(__float.valueOf(arg0)))

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4f.d()"""
        return 'Vec4d'.__wrap(super(Vec4f, self).d())

    @overload
    def mod(self, arg0: 'Vec4f') -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mod(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mod(arg0))

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setZ(float)"""
        super(__Vec4f, self).setZ(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def dot(self, arg0: 'Vec4f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float.__wrap(super(__Vec4f, self).dot(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def floor(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.floor()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).floor())

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.mul(float,float,float,float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).mul(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec4f', arg1: 'Vec4f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec4f.dot(dev.ultreon.libs.commons.v0.vector.Vec4f,dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        return float.__wrap(__Vec4f.dot(arg0, arg1))

    @overload
    def dec(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.dec()"""
        return 'Vec4f'.__wrap(super(Vec4f, self).dec())

    @overload
    def getW(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec4f.getW()"""
        return float.__wrap(super(Vec4f, self).getW())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4f.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec4f, self).equals(arg0))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4f.setY(float)"""
        super(__Vec4f, self).setY(__float.valueOf(arg0))

    @overload
    def add(self, arg0: float) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4f.add(float)"""
        return 'Vec4f'.__wrap(super(__Vec4f, self).add(__float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4f.toString()"""
        return str.__wrap(super(Vec4f, self).toString()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2i
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
from builtins import float
import java.awt.Point as Point
import java.awt.Point as __Point
__Point = __Point
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Dimension as __Dimension
__Dimension = __Dimension
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import java.awt.Dimension as Dimension
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vec2i(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec2i"""
 
    @staticmethod
    def __wrap(java_value: __Vec2i) -> 'Vec2i':
        return Vec2i(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec2i):
        """
        Dynamic initializer for Vec2i.
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
    def add(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i.__wrap(__Vec2i.add(arg0, arg1))

    @overload
    def mod(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mod(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.hashCode()"""
        return int.__wrap(super(Vec2i, self).hashCode())

    @staticmethod
    @overload
    def mul(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i.__wrap(__Vec2i.mul(arg0, arg1))

    @overload
    def mul(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mul(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Point'):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i(java.awt.Point)"""
        val = __Vec2i(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).set(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2i.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec2i, self).equals(arg0))

    @staticmethod
    @overload
    def div(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i.__wrap(__Vec2i.div(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i()"""
        val = __Vec2i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dst(self, arg0: int, arg1: int) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2i.dst(int,int)"""
        return float.__wrap(super(__Vec2i, self).dst(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def abs(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.abs()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).abs())

    @overload
    def add(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).add(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec2i', arg1: 'Vec2i') -> int:
        """public static int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return int.__wrap(__Vec2i.dot(arg0, arg1))

    @overload
    def sub(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).sub(arg0))

    @overload
    def cpy(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.cpy()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).cpy())

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.getY()"""
        return int.__wrap(super(Vec2i, self).getY())

    @overload
    def set(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def div(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).div(__int.valueOf(arg0)))

    @overload
    def dot(self, arg0: 'Vec2i') -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return int.__wrap(super(__Vec2i, self).dot(arg0))

    @overload
    def sub(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).sub(__int.valueOf(arg0)))

    @overload
    def div(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).div(arg0))

    @overload
    def dot(self, arg0: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(int)"""
        return int.__wrap(super(__Vec2i, self).dot(__int.valueOf(arg0)))

    @overload
    def neg(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.neg()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).neg())

    @overload
    def dot(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.dot(int,int)"""
        return int.__wrap(super(__Vec2i, self).dot(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mul(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mul(arg0))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2i.getX()"""
        return int.__wrap(super(Vec2i, self).getX())

    @overload
    def div(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.div(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).div(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def mul(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mul(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mul(__int.valueOf(arg0)))

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2i.f()"""
        return 'Vec2f'.__wrap(super(Vec2i, self).f())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.clone()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).clone())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def pow(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).pow(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i()"""
        val = __Vec2i()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.set(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).set(arg0))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.setY(int)"""
        super(__Vec2i, self).setY(__int.valueOf(arg0))

    @overload
    def pow(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).pow(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.setX(int)"""
        super(__Vec2i, self).setX(__int.valueOf(arg0))

    @overload
    def mod(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mod(arg0))

    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.i()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).i())

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec2i, self).writeExternal(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.vector.Vec2i(int,int)"""
        val = __Vec2i(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pow(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.pow(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).pow(__int.valueOf(arg0)))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2i.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec2i, self).readExternal(arg0)

    @overload
    def mod(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.mod(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).mod(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2i.d()"""
        return 'Vec2d'.__wrap(super(Vec2i, self).d())

    @overload
    def sub(self, arg0: int, arg1: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(int,int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).sub(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def toAwtDimension(self) -> 'Dimension':
        """public java.awt.Dimension dev.ultreon.libs.commons.v0.vector.Vec2i.toAwtDimension()"""
        return 'Dimension'.__wrap(super(Vec2i, self).toAwtDimension())

    @overload
    def add(self, arg0: int) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(int)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).add(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2i.pow(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2d.__wrap(__Vec2i.pow(arg0, arg1))

    @overload
    def dec(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.dec()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).dec())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toAwtPoint(self) -> 'Point':
        """public java.awt.Point dev.ultreon.libs.commons.v0.vector.Vec2i.toAwtPoint()"""
        return 'Point'.__wrap(super(Vec2i, self).toAwtPoint())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: 'Vec2i') -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.add(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return 'Vec2i'.__wrap(super(__Vec2i, self).add(arg0))

    @overload
    def dst(self, arg0: 'Vec2i') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2i.dst(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return float.__wrap(super(__Vec2i, self).dst(arg0))

    @staticmethod
    @overload
    def sub(arg0: 'Vec2i', arg1: 'Vec2i') -> 'Vec2i':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.sub(dev.ultreon.libs.commons.v0.vector.Vec2i,dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        return Vec2i.__wrap(__Vec2i.sub(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2i.toString()"""
        return str.__wrap(super(Vec2i, self).toString())

    @overload
    def inc(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2i.inc()"""
        return 'Vec2i'.__wrap(super(Vec2i, self).inc()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec4d
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec4i as __Vec4i
__Vec4i = __Vec4i
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec4f as __Vec4f
__Vec4f = __Vec4f
import dev.ultreon.libs.commons.v0.vector.Vec4d as __Vec4d
__Vec4d = __Vec4d
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
 
class Vec4d(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec4d"""
 
    @staticmethod
    def __wrap(java_value: __Vec4d) -> 'Vec4d':
        return Vec4d(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec4d):
        """
        Dynamic initializer for Vec4d.
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
    def mod(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mod(arg0))

    @overload
    def i(self) -> 'Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.libs.commons.v0.vector.Vec4d.i()"""
        return 'Vec4i'.__wrap(super(Vec4d, self).i())

    @overload
    def d(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.d()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).d())

    @overload
    def setZ(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setZ(double)"""
        super(__Vec4d, self).setZ(__double.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dst(self, arg0: 'Vec4d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dst(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float.__wrap(super(__Vec4d, self).dst(arg0))

    @overload
    def sub(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).sub(__double.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d(double,double,double,double)"""
        val = __Vec4d(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).set(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def pow(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).pow(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @staticmethod
    @overload
    def pow(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d.__wrap(__Vec4d.pow(arg0, arg1))

    @overload
    def clone(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.clone()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).clone())

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dst(double,double,double,double)"""
        return float.__wrap(super(__Vec4d, self).dst(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def getZ(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getZ()"""
        return float.__wrap(super(Vec4d, self).getZ())

    @overload
    def len2(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.len2()"""
        return float.__wrap(super(Vec4d, self).len2())

    @overload
    def getX(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getX()"""
        return float.__wrap(super(Vec4d, self).getX())

    @overload
    def f(self) -> 'Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.libs.commons.v0.vector.Vec4d.f()"""
        return 'Vec4f'.__wrap(super(Vec4d, self).f())

    @overload
    def getY(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getY()"""
        return float.__wrap(super(Vec4d, self).getY())

    @overload
    def mul(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mul(__double.valueOf(arg0)))

    @overload
    def mod(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mod(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def getW(self) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.getW()"""
        return float.__wrap(super(Vec4d, self).getW())

    @overload
    def sub(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).sub(arg0))

    @overload
    def cpy(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.cpy()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).cpy())

    @overload
    def dot(self, arg0: 'Vec4d') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float.__wrap(super(__Vec4d, self).dot(arg0))

    @overload
    def nor(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.nor()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).nor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dot(self, arg0: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(double)"""
        return float.__wrap(super(__Vec4d, self).dot(__double.valueOf(arg0)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).sub(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def setW(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setW(double)"""
        super(__Vec4d, self).setW(__double.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d()"""
        val = __Vec4d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mul(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def neg(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.neg()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).neg())

    @overload
    def mul(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mul(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).set(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec4d.toString()"""
        return str.__wrap(super(Vec4d, self).toString())

    @staticmethod
    @overload
    def mul(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mul(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d.__wrap(__Vec4d.mul(arg0, arg1))

    @staticmethod
    @overload
    def sub(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.sub(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d.__wrap(__Vec4d.sub(arg0, arg1))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).add(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def floor(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.floor()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).floor())

    @staticmethod
    @overload
    def div(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d.__wrap(__Vec4d.div(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec4d.hashCode()"""
        return int.__wrap(super(Vec4d, self).hashCode())

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(double,double,double,double)"""
        return float.__wrap(super(__Vec4d, self).dot(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def div(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).div(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: 'Vec4d', arg1: 'Vec4d') -> float:
        """public static double dev.ultreon.libs.commons.v0.vector.Vec4d.dot(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return float.__wrap(__Vec4d.dot(arg0, arg1))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setY(double)"""
        super(__Vec4d, self).setY(__double.valueOf(arg0))

    @overload
    def set(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.set(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).set(__double.valueOf(arg0)))

    @overload
    def add(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).add(__double.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec4d.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec4d, self).equals(arg0))

    @overload
    def abs(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.abs()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).abs())

    @staticmethod
    @overload
    def add(arg0: 'Vec4d', arg1: 'Vec4d') -> 'Vec4d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(dev.ultreon.libs.commons.v0.vector.Vec4d,dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return Vec4d.__wrap(__Vec4d.add(arg0, arg1))

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec4d, self).readExternal(arg0)

    @overload
    def pow(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).pow(__double.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec4d()"""
        val = __Vec4d()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.setX(double)"""
        super(__Vec4d, self).setX(__double.valueOf(arg0))

    @overload
    def add(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.add(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).add(arg0))

    @overload
    def dec(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.dec()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).dec())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def div(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).div(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def pow(self, arg0: 'Vec4d') -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.pow(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).pow(arg0))

    @overload
    def ceil(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.ceil()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).ceil())

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec4d.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec4d, self).writeExternal(arg0)

    @overload
    def div(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.div(double,double,double,double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).div(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def mod(self, arg0: float) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.mod(double)"""
        return 'Vec4d'.__wrap(super(__Vec4d, self).mod(__double.valueOf(arg0)))

    @overload
    def inc(self) -> 'Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.libs.commons.v0.vector.Vec4d.inc()"""
        return 'Vec4d'.__wrap(super(Vec4d, self).inc()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.vector.Vec2f
from builtins import str
import java.io.ObjectInput as ObjectInput
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
import java.io.ObjectOutput as ObjectOutput
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vec2f(__Externalizable, Externalizable, __Cloneable, Cloneable):
    """dev.ultreon.libs.commons.v0.vector.Vec2f"""
 
    @staticmethod
    def __wrap(java_value: __Vec2f) -> 'Vec2f':
        return Vec2f(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vec2f):
        """
        Dynamic initializer for Vec2f.
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
    def add(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).add(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def mul(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mul(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dst(self, arg0: 'Vec2f') -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2f.dst(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float.__wrap(super(__Vec2f, self).dst(arg0))

    @overload
    def floor(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.floor()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).floor())

    @overload
    def add(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def div(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).div(__float.valueOf(arg0)))

    @overload
    def mod(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mod(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f(float,float)"""
        val = __Vec2f(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def mul(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f.__wrap(__Vec2f.mul(arg0, arg1))

    @overload
    def abs(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.abs()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).abs())

    @overload
    def sub(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).sub(arg0))

    @overload
    def cpy(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.cpy()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).cpy())

    @overload
    def pow(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).pow(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def len2(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.len2()"""
        return float.__wrap(super(Vec2f, self).len2())

    @overload
    def dot(self, arg0: 'Vec2f') -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float.__wrap(super(__Vec2f, self).dot(arg0))

    @staticmethod
    @overload
    def add(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f.__wrap(__Vec2f.add(arg0, arg1))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.libs.commons.v0.vector.Vec2f.dst(float,float)"""
        return float.__wrap(super(__Vec2f, self).dst(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f()"""
        val = __Vec2f()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dot(self, arg0: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(float)"""
        return float.__wrap(super(__Vec2f, self).dot(__float.valueOf(arg0)))

    @overload
    def setY(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.setY(float)"""
        super(__Vec2f, self).setY(__float.valueOf(arg0))

    @overload
    def mod(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mod(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ceil(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.ceil()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).ceil())

    @overload
    def d(self) -> 'Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2f.d()"""
        return 'Vec2d'.__wrap(super(Vec2f, self).d())

    @overload
    def getX(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.getX()"""
        return float.__wrap(super(Vec2f, self).getX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def sub(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).sub(__float.valueOf(arg0)))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).sub(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.vector.Vec2f.toString()"""
        return str.__wrap(super(Vec2f, self).toString())

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).set(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setX(self, arg0: float):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.setX(float)"""
        super(__Vec2f, self).setX(__float.valueOf(arg0))

    @overload
    def i(self) -> 'Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.libs.commons.v0.vector.Vec2f.i()"""
        return 'Vec2i'.__wrap(super(Vec2f, self).i())

    @overload
    def mul(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mul(__float.valueOf(arg0)))

    @overload
    def clone(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.clone()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).clone())

    @overload
    def add(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.add(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).add(__float.valueOf(arg0)))

    @overload
    def nor(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.nor()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).nor())

    @staticmethod
    @overload
    def sub(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.sub(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f.__wrap(__Vec2f.sub(arg0, arg1))

    @overload
    def set(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).set(__float.valueOf(arg0)))

    @overload
    def neg(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.neg()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).neg())

    @overload
    def mod(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mod(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mod(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.vector.Vec2f.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vec2f, self).equals(arg0))

    @overload
    def f(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.f()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).f())

    @overload
    def pow(self, arg0: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).pow(__float.valueOf(arg0)))

    @overload
    def div(self, arg0: float, arg1: float) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(float,float)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).div(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def dec(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.dec()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).dec())

    @staticmethod
    @overload
    def pow(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2d':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.libs.commons.v0.vector.Vec2f.pow(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2d.__wrap(__Vec2f.pow(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.vector.Vec2f()"""
        val = __Vec2f()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def dot(arg0: 'Vec2f', arg1: 'Vec2f') -> float:
        """public static float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return float.__wrap(__Vec2f.dot(arg0, arg1))

    @overload
    def inc(self) -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.inc()"""
        return 'Vec2f'.__wrap(super(Vec2f, self).inc())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def writeExternal(self, arg0: 'ObjectOutput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.writeExternal(java.io.ObjectOutput) throws java.io.IOException"""
        super(__Vec2f, self).writeExternal(arg0)

    @overload
    def pow(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.pow(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).pow(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.dot(float,float)"""
        return float.__wrap(super(__Vec2f, self).dot(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.set(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).set(arg0))

    @overload
    def mul(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.mul(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).mul(arg0))

    @overload
    def div(self, arg0: 'Vec2f') -> 'Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return 'Vec2f'.__wrap(super(__Vec2f, self).div(arg0))

    @overload
    def getY(self) -> float:
        """public float dev.ultreon.libs.commons.v0.vector.Vec2f.getY()"""
        return float.__wrap(super(Vec2f, self).getY())

    @staticmethod
    @overload
    def div(arg0: 'Vec2f', arg1: 'Vec2f') -> 'Vec2f':
        """public static dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.libs.commons.v0.vector.Vec2f.div(dev.ultreon.libs.commons.v0.vector.Vec2f,dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        return Vec2f.__wrap(__Vec2f.div(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.vector.Vec2f.hashCode()"""
        return int.__wrap(super(Vec2f, self).hashCode())

    @override
    @overload
    def readExternal(self, arg0: 'ObjectInput'):
        """public void dev.ultreon.libs.commons.v0.vector.Vec2f.readExternal(java.io.ObjectInput) throws java.io.IOException"""
        super(__Vec2f, self).readExternal(arg0)