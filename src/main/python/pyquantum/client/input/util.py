from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.client.input.util.Joystick as __Joystick
__Joystick = __Joystick
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Joystick(pygdx.__Vector2, math.Vector2):
    """dev.ultreon.quantum.client.input.util.Joystick"""
 
    @staticmethod
    def __wrap(java_value: __Joystick) -> 'Joystick':
        return Joystick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Joystick):
        """
        Dynamic initializer for Joystick.
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
    def rotateDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateDeg(__float.valueOf(arg0)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mulAdd(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool.__wrap(super(math.Vector2, self).isZero())

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isOnLine(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float.__wrap(__Vector2.len(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def sub(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).sub(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = __Joystick()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scl(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(__float.valueOf(arg0)))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dst(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setLength(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setLength(__float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mul(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).hasOppositeDirection(arg0))

    @override
    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float.__wrap(super(math.Vector2, self).angleRad())

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angle(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).add(arg0))

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAroundRad(arg0, __float.valueOf(arg1)))

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angleRad(arg0))

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).interpolate(arg0, __float.valueOf(arg1), arg2))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).hasSameDirection(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str.__wrap(super(math.Vector2, self).toString())

    @overload
    def rotateRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateRad(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setZero(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).setZero())

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinearOpposite(arg0))

    @overload
    def setAngleDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngleDeg(__float.valueOf(arg0)))

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinear(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isOnLine(arg0))

    @overload
    def scl(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isPerpendicular(arg0, __float.valueOf(arg1)))

    @overload
    def rotate90(self, arg0: int) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotate90(__int.valueOf(arg0)))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float.__wrap(super(math.Vector2, self).len2())

    @override
    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float.__wrap(super(math.Vector2, self).angle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def cpy(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).cpy())

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinearOpposite(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def nor(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).nor())

    @overload
    def setAngle(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngle(__float.valueOf(arg0)))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dst2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dst(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = __Joystick()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).idt(arg0))

    @overload
    def set(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).set(arg0))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dot(arg0))

    @overload
    def add(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).add(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def scl(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(arg0))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).clamp(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).set(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).lerp(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float.__wrap(__Vector2.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int.__wrap(super(math.Vector2, self).hashCode())

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dst2(arg0))

    @overload
    def fromString(self, arg0: str) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).fromString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool.__wrap(super(__math.Vector2, self).equals(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dot(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len2(float,float)"""
        return float.__wrap(__Vector2.len2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setLength2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setLength2(__float.valueOf(arg0)))

    @overload
    def limit2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).limit2(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float.__wrap(__Vector2.dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAroundDeg(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float.__wrap(super(__math.Vector2, self).crs(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mulAdd(arg0, arg1))

    @override
    @overload
    def setToRandomDirection(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).setToRandomDirection())

    @override
    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float.__wrap(super(math.Vector2, self).angleDeg())

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angleDeg(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool.__wrap(super(math.Vector2, self).isUnit())

    @overload
    def sub(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).sub(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool.__wrap(super(__math.Vector2, self).isZero(__float.valueOf(arg0)))

    @overload
    def setAngleRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngleRad(__float.valueOf(arg0)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool.__wrap(super(__math.Vector2, self).isUnit(__float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isPerpendicular(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float.__wrap(super(math.Vector2, self).len())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAround(arg0, __float.valueOf(arg1)))

    @overload
    def limit(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).limit(__float.valueOf(arg0)))

    @overload
    def rotate(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotate(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float.__wrap(__Vector2.dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).crs(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinear(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Joystick
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.quantum.client.input.util.Joystick as __Joystick
__Joystick = __Joystick
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Joystick(pygdx.__Vector2, math.Vector2):
    """dev.ultreon.quantum.client.input.util.Joystick"""
 
    @staticmethod
    def __wrap(java_value: __Joystick) -> 'Joystick':
        return Joystick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Joystick):
        """
        Dynamic initializer for Joystick.
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
    def rotateDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateDeg(__float.valueOf(arg0)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mulAdd(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool.__wrap(super(math.Vector2, self).isZero())

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isOnLine(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float.__wrap(__Vector2.len(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def sub(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).sub(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = __Joystick()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scl(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(__float.valueOf(arg0)))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dst(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setLength(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setLength(__float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mul(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).hasOppositeDirection(arg0))

    @override
    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float.__wrap(super(math.Vector2, self).angleRad())

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angle(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).add(arg0))

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAroundRad(arg0, __float.valueOf(arg1)))

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angleRad(arg0))

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).interpolate(arg0, __float.valueOf(arg1), arg2))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).hasSameDirection(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str.__wrap(super(math.Vector2, self).toString())

    @overload
    def rotateRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateRad(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setZero(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).setZero())

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinearOpposite(arg0))

    @overload
    def setAngleDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngleDeg(__float.valueOf(arg0)))

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinear(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isOnLine(arg0))

    @overload
    def scl(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isPerpendicular(arg0, __float.valueOf(arg1)))

    @overload
    def rotate90(self, arg0: int) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotate90(__int.valueOf(arg0)))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float.__wrap(super(math.Vector2, self).len2())

    @override
    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float.__wrap(super(math.Vector2, self).angle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def cpy(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).cpy())

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinearOpposite(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def nor(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).nor())

    @overload
    def setAngle(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngle(__float.valueOf(arg0)))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dst2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dst(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = __Joystick()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).idt(arg0))

    @overload
    def set(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).set(arg0))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dot(arg0))

    @overload
    def add(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).add(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def scl(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).scl(arg0))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).clamp(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).set(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).lerp(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float.__wrap(__Vector2.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int.__wrap(super(math.Vector2, self).hashCode())

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).dst2(arg0))

    @overload
    def fromString(self, arg0: str) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).fromString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool.__wrap(super(__math.Vector2, self).equals(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float.__wrap(super(__math.Vector2, self).dot(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len2(float,float)"""
        return float.__wrap(__Vector2.len2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setLength2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setLength2(__float.valueOf(arg0)))

    @overload
    def limit2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).limit2(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float.__wrap(__Vector2.dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAroundDeg(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool.__wrap(super(__math.Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float.__wrap(super(__math.Vector2, self).crs(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).mulAdd(arg0, arg1))

    @override
    @overload
    def setToRandomDirection(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'math.Vector2'.__wrap(super(math.Vector2, self).setToRandomDirection())

    @override
    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float.__wrap(super(math.Vector2, self).angleDeg())

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).angleDeg(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool.__wrap(super(math.Vector2, self).isUnit())

    @overload
    def sub(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).sub(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool.__wrap(super(__math.Vector2, self).isZero(__float.valueOf(arg0)))

    @overload
    def setAngleRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).setAngleRad(__float.valueOf(arg0)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool.__wrap(super(__math.Vector2, self).isUnit(__float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isPerpendicular(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float.__wrap(super(math.Vector2, self).len())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotateAround(arg0, __float.valueOf(arg1)))

    @overload
    def limit(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).limit(__float.valueOf(arg0)))

    @overload
    def rotate(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'math.Vector2'.__wrap(super(__math.Vector2, self).rotate(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float.__wrap(__Vector2.dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__math.Vector2, self).crs(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Vector2, self).isCollinear(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Joystick 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.JoystickType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.input.util.JoystickType as __JoystickType
__JoystickType = __JoystickType
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
from builtins import int
 
class JoystickType(__Enum, Enum):
    """dev.ultreon.quantum.client.input.util.JoystickType"""
 
    @staticmethod
    def __wrap(java_value: __JoystickType) -> 'JoystickType':
        return JoystickType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JoystickType):
        """
        Dynamic initializer for JoystickType.
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
 
    # public static final dev.ultreon.quantum.client.input.util.JoystickType dev.ultreon.quantum.client.input.util.JoystickType.RIGHT
    RIGHT: 'JoystickType' = __wrap(__JoystickType.RIGHT)

    # public static final dev.ultreon.quantum.client.input.util.JoystickType dev.ultreon.quantum.client.input.util.JoystickType.LEFT
    LEFT: 'JoystickType' = __wrap(__JoystickType.LEFT)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @staticmethod
    @overload
    def values() -> List['JoystickType']:
        """public static dev.ultreon.quantum.client.input.util.JoystickType[] dev.ultreon.quantum.client.input.util.JoystickType.values()"""
        return List[JoystickType].__wrap(__JoystickType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JoystickType':
        """public static dev.ultreon.quantum.client.input.util.JoystickType dev.ultreon.quantum.client.input.util.JoystickType.valueOf(java.lang.String)"""
        return JoystickType.__wrap(__JoystickType.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.input.util.TriggerType
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
import dev.ultreon.quantum.client.input.util.TriggerType as __TriggerType
__TriggerType = __TriggerType
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class TriggerType(__Enum, Enum):
    """dev.ultreon.quantum.client.input.util.TriggerType"""
 
    @staticmethod
    def __wrap(java_value: __TriggerType) -> 'TriggerType':
        return TriggerType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriggerType):
        """
        Dynamic initializer for TriggerType.
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
 
    # public static final dev.ultreon.quantum.client.input.util.TriggerType dev.ultreon.quantum.client.input.util.TriggerType.RIGHT
    RIGHT: 'TriggerType' = __wrap(__TriggerType.RIGHT)

    # public static final dev.ultreon.quantum.client.input.util.TriggerType dev.ultreon.quantum.client.input.util.TriggerType.LEFT
    LEFT: 'TriggerType' = __wrap(__TriggerType.LEFT)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @staticmethod
    @overload
    def values() -> List['TriggerType']:
        """public static dev.ultreon.quantum.client.input.util.TriggerType[] dev.ultreon.quantum.client.input.util.TriggerType.values()"""
        return List[TriggerType].__wrap(__TriggerType.values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TriggerType':
        """public static dev.ultreon.quantum.client.input.util.TriggerType dev.ultreon.quantum.client.input.util.TriggerType.valueOf(java.lang.String)"""
        return TriggerType.__wrap(__TriggerType.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.input.util.ControllerButton
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.input.util.ControllerButton as __ControllerButton
__ControllerButton = __ControllerButton
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
try:
    from pygdx import controllers
except ImportError:
    controllers = __import_once__("pygdx.controllers")

from builtins import int
 
class ControllerButton(__Enum, Enum):
    """dev.ultreon.quantum.client.input.util.ControllerButton"""
 
    @staticmethod
    def __wrap(java_value: __ControllerButton) -> 'ControllerButton':
        return ControllerButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerButton):
        """
        Dynamic initializer for ControllerButton.
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
 
    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.LEFT_STICK
    LEFT_STICK: 'ControllerButton' = __wrap(__ControllerButton.LEFT_STICK)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.Y
    Y: 'ControllerButton' = __wrap(__ControllerButton.Y)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.DPAD_DOWN
    DPAD_DOWN: 'ControllerButton' = __wrap(__ControllerButton.DPAD_DOWN)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.DPAD_RIGHT
    DPAD_RIGHT: 'ControllerButton' = __wrap(__ControllerButton.DPAD_RIGHT)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.X
    X: 'ControllerButton' = __wrap(__ControllerButton.X)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.DPAD_UP
    DPAD_UP: 'ControllerButton' = __wrap(__ControllerButton.DPAD_UP)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.RIGHT_STICK
    RIGHT_STICK: 'ControllerButton' = __wrap(__ControllerButton.RIGHT_STICK)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.B
    B: 'ControllerButton' = __wrap(__ControllerButton.B)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.DPAD_LEFT
    DPAD_LEFT: 'ControllerButton' = __wrap(__ControllerButton.DPAD_LEFT)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.LEFT_BUTTON
    LEFT_BUTTON: 'ControllerButton' = __wrap(__ControllerButton.LEFT_BUTTON)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.RIGHT_BUTTON
    RIGHT_BUTTON: 'ControllerButton' = __wrap(__ControllerButton.RIGHT_BUTTON)

    # public static final dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.A
    A: 'ControllerButton' = __wrap(__ControllerButton.A)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ControllerButton':
        """public static dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.valueOf(java.lang.String)"""
        return ControllerButton.__wrap(__ControllerButton.valueOf(arg0))

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

    @overload
    def get(self, arg0: 'ControllerMapping') -> int:
        """public int dev.ultreon.quantum.client.input.util.ControllerButton.get(com.badlogic.gdx.controllers.ControllerMapping)"""
        return int.__wrap(super(__ControllerButton, self).get(arg0))

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
    def values() -> List['ControllerButton']:
        """public static dev.ultreon.quantum.client.input.util.ControllerButton[] dev.ultreon.quantum.client.input.util.ControllerButton.values()"""
        return List[ControllerButton].__wrap(__ControllerButton.values()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Trigger
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.input.util.Trigger as __Trigger
__Trigger = __Trigger
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Trigger():
    """dev.ultreon.quantum.client.input.util.Trigger"""
 
    @staticmethod
    def __wrap(java_value: __Trigger) -> 'Trigger':
        return Trigger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Trigger):
        """
        Dynamic initializer for Trigger.
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
    def cpy(self) -> 'Trigger':
        """public dev.ultreon.quantum.client.input.util.Trigger dev.ultreon.quantum.client.input.util.Trigger.cpy()"""
        return 'Trigger'.__wrap(super(Trigger, self).cpy())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Trigger()"""
        val = __Trigger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Trigger()"""
        val = __Trigger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))