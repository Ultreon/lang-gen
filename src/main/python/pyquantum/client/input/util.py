from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
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
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.input.util.Joystick as _Joystick
_Joystick = _Joystick
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Joystick():
    """dev.ultreon.quantum.client.input.util.Joystick"""
 
    @staticmethod
    def _wrap(java_value: _Joystick) -> 'Joystick':
        return Joystick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Joystick):
        """
        Dynamic initializer for Joystick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Joystick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Joystick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).set(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isPerpendicular(arg0))

    @overload
    def set(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).set(arg0))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float._wrap(super(_math.Vector2, self).dst2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setAngleDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngleDeg(_float.valueOf(arg0)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool._wrap(super(math.Vector2, self).isZero())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setToRandomDirection(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).setToRandomDirection())

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).interpolate(arg0, _float.valueOf(arg1), arg2))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).sub(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float._wrap(_Vector2.dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = _Joystick()
        self.__wrapper = val

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float._wrap(super(_math.Vector2, self).crs(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool._wrap(super(_math.Vector2, self).isUnit(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(_float.valueOf(arg0)))

    @overload
    def setAngle(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngle(_float.valueOf(arg0)))

    @override
    @overload
    def nor(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).nor())

    @overload
    def sub(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).sub(arg0))

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).crs(arg0))

    @override
    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float._wrap(super(math.Vector2, self).angleRad())

    @override
    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float._wrap(super(math.Vector2, self).angleDeg())

    @overload
    def rotateDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateDeg(_float.valueOf(arg0)))

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isCollinear(arg0, _float.valueOf(arg1)))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isOnLine(arg0))

    @overload
    def limit2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).limit2(_float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mul(arg0))

    @overload
    def fromString(self, arg0: str) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).fromString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool._wrap(super(_math.Vector2, self).equals(arg0))

    @overload
    def rotate(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotate(_float.valueOf(arg0)))

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angleRad(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isCollinearOpposite(arg0))

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAround(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def cpy(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).cpy())

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isOnLine(arg0, _float.valueOf(arg1)))

    @overload
    def setAngleRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngleRad(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = _Joystick()
        self.__wrapper = val

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAroundRad(arg0, _float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mulAdd(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str._wrap(super(math.Vector2, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int._wrap(super(math.Vector2, self).hashCode())

    @overload
    def scl(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def rotate90(self, arg0: int) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotate90(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len2(float,float)"""
        return float._wrap(_Vector2.len2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dst2(arg0))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def add(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).add(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isCollinear(arg0))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float._wrap(super(math.Vector2, self).len())

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float._wrap(super(_math.Vector2, self).dst(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mulAdd(arg0, _float.valueOf(arg1)))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).clamp(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def limit(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).limit(_float.valueOf(arg0)))

    @overload
    def rotateRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateRad(_float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isPerpendicular(arg0, _float.valueOf(arg1)))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).hasSameDirection(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).hasOppositeDirection(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float._wrap(super(_math.Vector2, self).dot(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isCollinearOpposite(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool._wrap(super(math.Vector2, self).isUnit())

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAroundDeg(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dot(arg0))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool._wrap(super(_math.Vector2, self).isZero(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float._wrap(_Vector2.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).add(arg0))

    @overload
    def setLength(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setLength(_float.valueOf(arg0)))

    @override
    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float._wrap(super(math.Vector2, self).angle())

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).idt(arg0))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float._wrap(_Vector2.len(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setZero(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).setZero())

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angleDeg(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angle(arg0))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float._wrap(super(math.Vector2, self).len2())

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dst(arg0))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float._wrap(_Vector2.dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setLength2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setLength2(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Joystick
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
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
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.input.util.Joystick as _Joystick
_Joystick = _Joystick
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Joystick():
    """dev.ultreon.quantum.client.input.util.Joystick"""
 
    @staticmethod
    def _wrap(java_value: _Joystick) -> 'Joystick':
        return Joystick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Joystick):
        """
        Dynamic initializer for Joystick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Joystick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Joystick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).set(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isPerpendicular(arg0))

    @overload
    def set(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).set(arg0))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float._wrap(super(_math.Vector2, self).dst2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setAngleDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngleDeg(_float.valueOf(arg0)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool._wrap(super(math.Vector2, self).isZero())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setToRandomDirection(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).setToRandomDirection())

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).interpolate(arg0, _float.valueOf(arg1), arg2))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).sub(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float._wrap(_Vector2.dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = _Joystick()
        self.__wrapper = val

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float._wrap(super(_math.Vector2, self).crs(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool._wrap(super(_math.Vector2, self).isUnit(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(_float.valueOf(arg0)))

    @overload
    def setAngle(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngle(_float.valueOf(arg0)))

    @override
    @overload
    def nor(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).nor())

    @overload
    def sub(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).sub(arg0))

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).crs(arg0))

    @override
    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float._wrap(super(math.Vector2, self).angleRad())

    @override
    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float._wrap(super(math.Vector2, self).angleDeg())

    @overload
    def rotateDeg(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateDeg(_float.valueOf(arg0)))

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isCollinear(arg0, _float.valueOf(arg1)))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isOnLine(arg0))

    @overload
    def limit2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).limit2(_float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mul(arg0))

    @overload
    def fromString(self, arg0: str) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).fromString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool._wrap(super(_math.Vector2, self).equals(arg0))

    @overload
    def rotate(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotate(_float.valueOf(arg0)))

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angleRad(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isCollinearOpposite(arg0))

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAround(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def cpy(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).cpy())

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isOnLine(arg0, _float.valueOf(arg1)))

    @overload
    def setAngleRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setAngleRad(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Joystick()"""
        val = _Joystick()
        self.__wrapper = val

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAroundRad(arg0, _float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mulAdd(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str._wrap(super(math.Vector2, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int._wrap(super(math.Vector2, self).hashCode())

    @overload
    def scl(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def rotate90(self, arg0: int) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotate90(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len2(float,float)"""
        return float._wrap(_Vector2.len2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dst2(arg0))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def add(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).add(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).isCollinear(arg0))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float._wrap(super(math.Vector2, self).len())

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float._wrap(super(_math.Vector2, self).dst(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).mulAdd(arg0, _float.valueOf(arg1)))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).clamp(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def limit(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).limit(_float.valueOf(arg0)))

    @overload
    def rotateRad(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateRad(_float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isPerpendicular(arg0, _float.valueOf(arg1)))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).hasSameDirection(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).hasOppositeDirection(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float._wrap(super(_math.Vector2, self).dot(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).isCollinearOpposite(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool._wrap(super(math.Vector2, self).isUnit())

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).rotateAroundDeg(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dot(arg0))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool._wrap(super(_math.Vector2, self).isZero(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float._wrap(_Vector2.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_math.Vector2, self).epsilonEquals(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).add(arg0))

    @overload
    def setLength(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setLength(_float.valueOf(arg0)))

    @override
    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float._wrap(super(math.Vector2, self).angle())

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_math.Vector2, self).idt(arg0))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float._wrap(_Vector2.len(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setZero(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'math.Vector2'._wrap(super(math.Vector2, self).setZero())

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angleDeg(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).angle(arg0))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float._wrap(super(math.Vector2, self).len2())

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_math.Vector2, self).dst(arg0))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float._wrap(_Vector2.dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setLength2(self, arg0: float) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).setLength2(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_math.Vector2, self).scl(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Joystick 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.JoystickType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.quantum.client.input.util.JoystickType as _JoystickType
_JoystickType = _JoystickType
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JoystickType():
    """dev.ultreon.quantum.client.input.util.JoystickType"""
 
    @staticmethod
    def _wrap(java_value: _JoystickType) -> 'JoystickType':
        return JoystickType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JoystickType):
        """
        Dynamic initializer for JoystickType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JoystickType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JoystickType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['JoystickType']:
        """public static dev.ultreon.quantum.client.input.util.JoystickType[] dev.ultreon.quantum.client.input.util.JoystickType.values()"""
        return List[JoystickType]._wrap(_JoystickType.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JoystickType':
        """public static dev.ultreon.quantum.client.input.util.JoystickType dev.ultreon.quantum.client.input.util.JoystickType.valueOf(java.lang.String)"""
        return JoystickType._wrap(_JoystickType.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


JoystickType.RIGHT = JoystickType._wrap(_RIGHT.RIGHT)

JoystickType.LEFT = JoystickType._wrap(_LEFT.LEFT) 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.TriggerType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.input.util.TriggerType as _TriggerType
_TriggerType = _TriggerType
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TriggerType():
    """dev.ultreon.quantum.client.input.util.TriggerType"""
 
    @staticmethod
    def _wrap(java_value: _TriggerType) -> 'TriggerType':
        return TriggerType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriggerType):
        """
        Dynamic initializer for TriggerType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriggerType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriggerType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['TriggerType']:
        """public static dev.ultreon.quantum.client.input.util.TriggerType[] dev.ultreon.quantum.client.input.util.TriggerType.values()"""
        return List[TriggerType]._wrap(_TriggerType.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TriggerType':
        """public static dev.ultreon.quantum.client.input.util.TriggerType dev.ultreon.quantum.client.input.util.TriggerType.valueOf(java.lang.String)"""
        return TriggerType._wrap(_TriggerType.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


TriggerType.RIGHT = TriggerType._wrap(_RIGHT.RIGHT)

TriggerType.LEFT = TriggerType._wrap(_LEFT.LEFT) 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.ControllerButton
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.input.util.ControllerButton as _ControllerButton
_ControllerButton = _ControllerButton
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
try:
    from pygdx import controllers
except ImportError:
    controllers = _import_once("pygdx.controllers")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ControllerButton():
    """dev.ultreon.quantum.client.input.util.ControllerButton"""
 
    @staticmethod
    def _wrap(java_value: _ControllerButton) -> 'ControllerButton':
        return ControllerButton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerButton):
        """
        Dynamic initializer for ControllerButton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerButton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerButton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ControllerButton':
        """public static dev.ultreon.quantum.client.input.util.ControllerButton dev.ultreon.quantum.client.input.util.ControllerButton.valueOf(java.lang.String)"""
        return ControllerButton._wrap(_ControllerButton.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @overload
    def get(self, arg0: 'ControllerMapping') -> int:
        """public int dev.ultreon.quantum.client.input.util.ControllerButton.get(com.badlogic.gdx.controllers.ControllerMapping)"""
        return int._wrap(super(_ControllerButton, self).get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['ControllerButton']:
        """public static dev.ultreon.quantum.client.input.util.ControllerButton[] dev.ultreon.quantum.client.input.util.ControllerButton.values()"""
        return List[ControllerButton]._wrap(_ControllerButton.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


ControllerButton.DPAD_DOWN = ControllerButton._wrap(_DPAD_DOWN.DPAD_DOWN)

ControllerButton.DPAD_RIGHT = ControllerButton._wrap(_DPAD_RIGHT.DPAD_RIGHT)

ControllerButton.RIGHT_STICK = ControllerButton._wrap(_RIGHT_STICK.RIGHT_STICK)

ControllerButton.LEFT_BUTTON = ControllerButton._wrap(_LEFT_BUTTON.LEFT_BUTTON)

ControllerButton.A = ControllerButton._wrap(_A.A)

ControllerButton.X = ControllerButton._wrap(_X.X)

ControllerButton.Y = ControllerButton._wrap(_Y.Y)

ControllerButton.LEFT_STICK = ControllerButton._wrap(_LEFT_STICK.LEFT_STICK)

ControllerButton.B = ControllerButton._wrap(_B.B)

ControllerButton.DPAD_UP = ControllerButton._wrap(_DPAD_UP.DPAD_UP)

ControllerButton.RIGHT_BUTTON = ControllerButton._wrap(_RIGHT_BUTTON.RIGHT_BUTTON)

ControllerButton.DPAD_LEFT = ControllerButton._wrap(_DPAD_LEFT.DPAD_LEFT) 
 
 
# CLASS: dev.ultreon.quantum.client.input.util.Trigger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.client.input.util.Trigger as _Trigger
_Trigger = _Trigger
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Trigger():
    """dev.ultreon.quantum.client.input.util.Trigger"""
 
    @staticmethod
    def _wrap(java_value: _Trigger) -> 'Trigger':
        return Trigger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Trigger):
        """
        Dynamic initializer for Trigger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Trigger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Trigger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.input.util.Trigger()"""
        val = _Trigger()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def cpy(self) -> 'Trigger':
        """public dev.ultreon.quantum.client.input.util.Trigger dev.ultreon.quantum.client.input.util.Trigger.cpy()"""
        return 'Trigger'._wrap(super(Trigger, self).cpy())

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
    def __init__(self):
        """public dev.ultreon.quantum.client.input.util.Trigger()"""
        val = _Trigger()
        self.__wrapper = val