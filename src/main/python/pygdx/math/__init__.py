from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

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
import com.badlogic.gdx.math.Bezier as __Bezier
__Bezier = __Bezier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
from builtins import int
 
class Bezier():
    """com.badlogic.gdx.math.Bezier"""
 
    @staticmethod
    def __wrap(java_value: __Bezier) -> 'Bezier':
        return Bezier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bezier):
        """
        Dynamic initializer for Bezier.
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
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.derivativeAt(T,float)"""
        return 'Vector'.__wrap(super(__Bezier, self).derivativeAt(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.valueAt(T,float)"""
        return 'Vector'.__wrap(super(__Bezier, self).valueAt(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, *arg0: 'Vector') -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T...)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0))

    @staticmethod
    @overload
    def linear(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear(T,float,T,T,T)"""
        return Vector.__wrap(__Bezier.linear(arg0, __float.valueOf(arg1), arg2, arg3, arg4))

    @overload
    def __init__(self, *arg0: 'Vector'):
        """public com.badlogic.gdx.math.Bezier(T...)"""
        val = __Bezier(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def quadratic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic(T,float,T,T,T,T)"""
        return Vector.__wrap(__Bezier.quadratic(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic_derivative(T,float,T,T,T,T,T)"""
        return Vector.__wrap(__Bezier.cubic_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def set(self, arg0: 'Array', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(com.badlogic.gdx.utils.Array<T>,int,int)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.Bezier.approxLength(int)"""
        return float.__wrap(super(__Bezier, self).approxLength(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def linear_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear_derivative(T,float,T,T,T)"""
        return Vector.__wrap(__Bezier.linear_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4))

    @overload
    def __init__(self, arg0: 'Array', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(com.badlogic.gdx.utils.Array<T>,int,int)"""
        val = __Bezier(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.locate(T)"""
        return float.__wrap(super(__Bezier, self).locate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Bezier()"""
        val = __Bezier()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.approximate(T)"""
        return float.__wrap(super(__Bezier, self).approximate(arg0))

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
    def __init__(self, arg0: 'Vector', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(T[],int,int)"""
        val = __Bezier(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def quadratic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic_derivative(T,float,T,T,T,T)"""
        return Vector.__wrap(__Bezier.quadratic_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic(T,float,T,T,T,T,T)"""
        return Vector.__wrap(__Bezier.cubic(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Bezier()"""
        val = __Bezier()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T[],int,int)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: com.badlogic.gdx.math.Bezier
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

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
import com.badlogic.gdx.math.Bezier as __Bezier
__Bezier = __Bezier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
from builtins import int
 
class Bezier():
    """com.badlogic.gdx.math.Bezier"""
 
    @staticmethod
    def __wrap(java_value: __Bezier) -> 'Bezier':
        return Bezier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bezier):
        """
        Dynamic initializer for Bezier.
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
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.derivativeAt(T,float)"""
        return 'Vector'.__wrap(super(__Bezier, self).derivativeAt(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.valueAt(T,float)"""
        return 'Vector'.__wrap(super(__Bezier, self).valueAt(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, *arg0: 'Vector') -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T...)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0))

    @staticmethod
    @overload
    def linear(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear(T,float,T,T,T)"""
        return Vector.__wrap(__Bezier.linear(arg0, __float.valueOf(arg1), arg2, arg3, arg4))

    @overload
    def __init__(self, *arg0: 'Vector'):
        """public com.badlogic.gdx.math.Bezier(T...)"""
        val = __Bezier(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def quadratic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic(T,float,T,T,T,T)"""
        return Vector.__wrap(__Bezier.quadratic(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic_derivative(T,float,T,T,T,T,T)"""
        return Vector.__wrap(__Bezier.cubic_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def set(self, arg0: 'Array', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(com.badlogic.gdx.utils.Array<T>,int,int)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.Bezier.approxLength(int)"""
        return float.__wrap(super(__Bezier, self).approxLength(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def linear_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear_derivative(T,float,T,T,T)"""
        return Vector.__wrap(__Bezier.linear_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4))

    @overload
    def __init__(self, arg0: 'Array', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(com.badlogic.gdx.utils.Array<T>,int,int)"""
        val = __Bezier(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.locate(T)"""
        return float.__wrap(super(__Bezier, self).locate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Bezier()"""
        val = __Bezier()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.approximate(T)"""
        return float.__wrap(super(__Bezier, self).approximate(arg0))

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
    def __init__(self, arg0: 'Vector', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(T[],int,int)"""
        val = __Bezier(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def quadratic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic_derivative(T,float,T,T,T,T)"""
        return Vector.__wrap(__Bezier.quadratic_derivative(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic(T,float,T,T,T,T,T)"""
        return Vector.__wrap(__Bezier.cubic(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Bezier()"""
        val = __Bezier()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T[],int,int)"""
        return 'Bezier'.__wrap(super(__Bezier, self).set(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: com.badlogic.gdx.math.Bezier 
 
 
# CLASS: com.badlogic.gdx.math.Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vector3():
    """com.badlogic.gdx.math.Vector3"""
 
    @staticmethod
    def __wrap(java_value: __Vector3) -> 'Vector3':
        return Vector3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector3):
        """
        Dynamic initializer for Vector3.
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
    def isCollinear(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinear(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Vector3, self).isCollinear(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector3.len()"""
        return float.__wrap(super(Vector3, self).len())

    @overload
    def interpolate(self, arg0: 'Vector3', arg1: float, arg2: 'Interpolation') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.interpolate(com.badlogic.gdx.math.Vector3,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector3'.__wrap(super(__Vector3, self).interpolate(arg0, __float.valueOf(arg1), arg2))

    @overload
    def untransform(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.untransform(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).untransform(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def prj(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.prj(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).prj(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.hasOppositeDirection(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).hasOppositeDirection(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isUnit()"""
        return bool.__wrap(super(Vector3, self).isUnit())

    @overload
    def fromString(self, arg0: str) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.fromString(java.lang.String)"""
        return 'Vector3'.__wrap(super(__Vector3, self).fromString(arg0))

    @overload
    def lerp(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.lerp(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).set(arg0))

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).mul(arg0))

    @overload
    def isPerpendicular(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isPerpendicular(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Vector3, self).isPerpendicular(arg0, __float.valueOf(arg1)))

    @overload
    def rotateRad(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotateRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).rotateRad(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isZero(float)"""
        return bool.__wrap(super(__Vector3, self).isZero(__float.valueOf(arg0)))

    @override
    @overload
    def setZero(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setZero()"""
        return 'Vector3'.__wrap(super(Vector3, self).setZero())

    @overload
    def set(self, arg0: 'float') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(float[])"""
        return 'Vector3'.__wrap(super(__Vector3, self).set(arg0))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isZero()"""
        return bool.__wrap(super(Vector3, self).isZero())

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(float,float,float)"""
        return bool.__wrap(super(__Vector3, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vector3, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector3()"""
        val = __Vector3()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector3'):
        """public com.badlogic.gdx.math.Vector3(com.badlogic.gdx.math.Vector3)"""
        val = __Vector3(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector2', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).set(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Vector3(float,float,float)"""
        val = __Vector3(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector3()"""
        val = __Vector3()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dst(float,float,float,float,float,float)"""
        return float.__wrap(__Vector3.dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def dst2(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dst2(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Vector3, self).dst2(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinearOpposite(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).isCollinearOpposite(arg0))

    @override
    @overload
    def nor(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.nor()"""
        return 'Vector3'.__wrap(super(Vector3, self).nor())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Vector3(float[])"""
        val = __Vector3(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setLength(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setLength(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).setLength(__float.valueOf(arg0)))

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotate(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).rotate(arg0, __float.valueOf(arg1)))

    @overload
    def isOnLine(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isOnLine(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Vector3, self).isOnLine(arg0, __float.valueOf(arg1)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinearOpposite(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Vector3, self).isCollinearOpposite(arg0, __float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mulAdd(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).mulAdd(arg0, arg1))

    @overload
    def unrotate(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.unrotate(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).unrotate(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def sub(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).sub(arg0))

    @overload
    def add(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).add(__float.valueOf(arg0)))

    @overload
    def limit(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.limit(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).limit(__float.valueOf(arg0)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isUnit(float)"""
        return bool.__wrap(super(__Vector3, self).isUnit(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mul(self, arg0: 'Quaternion') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Quaternion)"""
        return 'Vector3'.__wrap(super(__Vector3, self).mul(arg0))

    @overload
    def dst2(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dst2(float,float,float)"""
        return float.__wrap(super(__Vector3, self).dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector3.len2()"""
        return float.__wrap(super(Vector3, self).len2())

    @overload
    def mulAdd(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mulAdd(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).mulAdd(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dst2(float,float,float,float,float,float)"""
        return float.__wrap(__Vector3.dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(float,float,float,float)"""
        return bool.__wrap(super(__Vector3, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.len(float,float,float)"""
        return float.__wrap(__Vector3.len(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def scl(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).scl(__float.valueOf(arg0)))

    @overload
    def slerp(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.slerp(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).slerp(arg0, __float.valueOf(arg1)))

    @overload
    def setFromSpherical(self, arg0: float, arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setFromSpherical(float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).setFromSpherical(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.math.Vector3(com.badlogic.gdx.math.Vector2,float)"""
        val = __Vector3(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).sub(__float.valueOf(arg0)))

    @overload
    def setLength2(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setLength2(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).setLength2(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.len2(float,float,float)"""
        return float.__wrap(__Vector3.len2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def traMul(self, arg0: 'Matrix3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.traMul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).traMul(arg0))

    @override
    @overload
    def cpy(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.cpy()"""
        return 'Vector3'.__wrap(super(Vector3, self).cpy())

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dot(float,float,float,float,float,float)"""
        return float.__wrap(__Vector3.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector3.hashCode()"""
        return int.__wrap(super(Vector3, self).hashCode())

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dst(float,float,float)"""
        return float.__wrap(super(__Vector3, self).dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.clamp(float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).clamp(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def crs(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.crs(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).crs(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector3.toString()"""
        return str.__wrap(super(Vector3, self).toString())

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).sub(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def mul4x3(self, arg0: 'float') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul4x3(float[])"""
        return 'Vector3'.__wrap(super(__Vector3, self).mul4x3(arg0))

    @overload
    def hasSameDirection(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.hasSameDirection(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).hasSameDirection(arg0))

    @overload
    def dst(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dst(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Vector3, self).dst(arg0))

    @overload
    def rot(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rot(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).rot(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).epsilonEquals(arg0))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).mul(arg0))

    @overload
    def scl(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).scl(arg0))

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotate(float,float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).scl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def traMul(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.traMul(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'.__wrap(super(__Vector3, self).traMul(arg0))

    @overload
    def rotateRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotateRad(float,float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).rotateRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def dot(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dot(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Vector3, self).dot(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isOnLine(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).isOnLine(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Vector3, self).epsilonEquals(arg0, __float.valueOf(arg1)))

    @overload
    def isCollinear(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinear(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).isCollinear(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dot(float,float,float)"""
        return float.__wrap(super(__Vector3, self).dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def isPerpendicular(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isPerpendicular(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).isPerpendicular(arg0))

    @overload
    def limit2(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.limit2(float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).limit2(__float.valueOf(arg0)))

    @overload
    def crs(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.crs(float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).crs(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(float,float,float)"""
        return 'Vector3'.__wrap(super(__Vector3, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def add(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Vector3, self).add(arg0))

    @overload
    def idt(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.idt(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Vector3, self).idt(arg0))

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setToRandomDirection()"""
        return 'Vector3'.__wrap(super(Vector3, self).setToRandomDirection()) 
 
 
# CLASS: com.badlogic.gdx.math.Octree
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Octree as __Octree
__Octree = __Octree
from builtins import object
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet
__ObjectSet = __ObjectSet
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Octree():
    """com.badlogic.gdx.math.Octree"""
 
    @staticmethod
    def __wrap(java_value: __Octree) -> 'Octree':
        return Octree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Octree):
        """
        Dynamic initializer for Octree.
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
    def update(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.update(T)"""
        super(__Octree, self).update(arg0)

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
    def query(self, arg0: 'BoundingBox', arg1: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.query(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'.__wrap(super(__Octree, self).query(arg0, arg1))

    @overload
    def rayCast(self, arg0: 'Ray', arg1: 'RayCastResult') -> object:
        """public T com.badlogic.gdx.math.Octree.rayCast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Octree$RayCastResult<T>)"""
        return object.__wrap(super(__Octree, self).rayCast(arg0, arg1))

    @overload
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.remove(T)"""
        super(__Octree, self).remove(arg0)

    @overload
    def getNodesBoxes(self, arg0: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.math.collision.BoundingBox> com.badlogic.gdx.math.Octree.getNodesBoxes(com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.math.collision.BoundingBox>)"""
        return 'utils.ObjectSet'.__wrap(super(__Octree, self).getNodesBoxes(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def query(self, arg0: 'Frustum', arg1: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.query(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'.__wrap(super(__Octree, self).query(arg0, arg1))

    @overload
    def getAll(self, arg0: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.getAll(com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'.__wrap(super(__Octree, self).getAll(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.add(T)"""
        super(__Octree, self).add(arg0)

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

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3', arg2: int, arg3: int, arg4: 'Collider'):
        """public com.badlogic.gdx.math.Octree(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int,com.badlogic.gdx.math.Octree$Collider<T>)"""
        val = __Octree(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Octree$Collider
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import com.badlogic.gdx.math.Octree as __Octree_Collider
__Collider = __Octree_Collider.Collider
from abc import abstractmethod, ABC
 
class Collider(ABC):
    """com.badlogic.gdx.math.Octree.Collider"""
 
    @staticmethod
    def __wrap(java_value: __Collider) -> 'Collider':
        return Collider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Collider):
        """
        Dynamic initializer for Collider.
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
    def intersects(self, arg0: 'Ray', arg1: object):
        """public abstract float com.badlogic.gdx.math.Octree$Collider.intersects(com.badlogic.gdx.math.collision.Ray,T)"""
        pass

    @abstractmethod
    def intersects(self, arg0: 'Frustum', arg1: object):
        """public abstract boolean com.badlogic.gdx.math.Octree$Collider.intersects(com.badlogic.gdx.math.Frustum,T)"""
        pass

    @abstractmethod
    def intersects(self, arg0: 'BoundingBox', arg1: object):
        """public abstract boolean com.badlogic.gdx.math.Octree$Collider.intersects(com.badlogic.gdx.math.collision.BoundingBox,T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ExpIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_ExpIn
__ExpIn = __Interpolation_ExpIn.ExpIn
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
 
class ExpIn():
    """com.badlogic.gdx.math.Interpolation.ExpIn"""
 
    @staticmethod
    def __wrap(java_value: __ExpIn) -> 'ExpIn':
        return ExpIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExpIn):
        """
        Dynamic initializer for ExpIn.
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

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Interpolation$ExpIn(float,float)"""
        val = __ExpIn(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ExpIn.apply(float)"""
        return float.__wrap(super(__ExpIn, self).apply(__float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector$SplitTriangle
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
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.Intersector as __Intersector_SplitTriangle
__SplitTriangle = __Intersector_SplitTriangle.SplitTriangle
from builtins import int
 
class SplitTriangle():
    """com.badlogic.gdx.math.Intersector.SplitTriangle"""
 
    @staticmethod
    def __wrap(java_value: __SplitTriangle) -> 'SplitTriangle':
        return SplitTriangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SplitTriangle):
        """
        Dynamic initializer for SplitTriangle.
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Intersector$SplitTriangle.toString()"""
        return str.__wrap(super(SplitTriangle, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Intersector$SplitTriangle(int)"""
        val = __SplitTriangle(__int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.math.Matrix3
from builtins import str
import com.badlogic.gdx.math.Matrix3 as __Matrix3
__Matrix3 = __Matrix3
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
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
 
class Matrix3():
    """com.badlogic.gdx.math.Matrix3"""
 
    @staticmethod
    def __wrap(java_value: __Matrix3) -> 'Matrix3':
        return Matrix3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Matrix3):
        """
        Dynamic initializer for Matrix3.
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
        """public java.lang.String com.badlogic.gdx.math.Matrix3.toString()"""
        return str.__wrap(super(Matrix3, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Matrix3()"""
        val = __Matrix3()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scale(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).scale(arg0))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).mul(arg0))

    @overload
    def setToScaling(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToScaling(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToScaling(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.getRotation()"""
        return float.__wrap(super(Matrix3, self).getRotation())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setToRotationRad(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotationRad(float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToRotationRad(__float.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.translate(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).translate(arg0))

    @overload
    def rotate(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.rotate(float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).rotate(__float.valueOf(arg0)))

    @overload
    def getTranslation(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Matrix3.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Matrix3, self).getTranslation(arg0))

    @overload
    def getValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Matrix3.getValues()"""
        return List[float].__wrap(super(Matrix3, self).getValues())

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
    def set(self, arg0: 'float') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(float[])"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).set(arg0))

    @overload
    def idt(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.idt()"""
        return 'Matrix3'.__wrap(super(Matrix3, self).idt())

    @overload
    def scl(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).scl(arg0))

    @overload
    def set(self, arg0: 'Matrix4') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).set(arg0))

    @overload
    def setToScaling(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToScaling(float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToScaling(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setToTranslation(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToTranslation(float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToTranslation(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getRotationRad(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.getRotationRad()"""
        return float.__wrap(super(Matrix3, self).getRotationRad())

    @overload
    def __init__(self, arg0: 'Matrix3'):
        """public com.badlogic.gdx.math.Matrix3(com.badlogic.gdx.math.Matrix3)"""
        val = __Matrix3(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def transpose(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.transpose()"""
        return 'Matrix3'.__wrap(super(Matrix3, self).transpose())

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float, arg2: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(com.badlogic.gdx.math.Vector3,float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToRotation(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setToTranslation(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToTranslation(arg0))

    @overload
    def rotateRad(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.rotateRad(float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).rotateRad(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Matrix3(float[])"""
        val = __Matrix3(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mulLeft(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.mulLeft(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).mulLeft(arg0))

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scale(float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).scale(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def scl(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).scl(__float.valueOf(arg0)))

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.translate(float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).translate(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def trn(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(float,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).trn(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def trn(self, arg0: 'Vector3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).trn(arg0))

    @overload
    def set(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).set(arg0))

    @overload
    def scl(self, arg0: 'Vector3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).scl(arg0))

    @overload
    def set(self, arg0: 'Affine2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).set(arg0))

    @overload
    def setToRotation(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToRotation(__float.valueOf(arg0)))

    @overload
    def getScale(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Matrix3.getScale(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Matrix3, self).getScale(arg0))

    @overload
    def inv(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.inv()"""
        return 'Matrix3'.__wrap(super(Matrix3, self).inv())

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.det()"""
        return float.__wrap(super(Matrix3, self).det())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).setToRotation(arg0, __float.valueOf(arg1)))

    @overload
    def trn(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'.__wrap(super(__Matrix3, self).trn(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Matrix3()"""
        val = __Matrix3()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Vector2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vector2():
    """com.badlogic.gdx.math.Vector2"""
 
    @staticmethod
    def __wrap(java_value: __Vector2) -> 'Vector2':
        return Vector2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector2):
        """
        Dynamic initializer for Vector2.
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
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).mulAdd(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Vector2(float,float)"""
        val = __Vector2(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__Vector2, self).epsilonEquals(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool.__wrap(super(__Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float.__wrap(__Vector2.len(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float.__wrap(super(Vector2, self).len())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__Vector2, self).isCollinear(arg0, __float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__Vector2, self).isPerpendicular(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool.__wrap(super(Vector2, self).isZero())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).isCollinearOpposite(arg0))

    @overload
    def limit(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).limit(__float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).isPerpendicular(arg0))

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'Vector2'.__wrap(super(Vector2, self).setToRandomDirection())

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).crs(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__Vector2, self).isCollinearOpposite(arg0, __float.valueOf(arg1)))

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotateAroundDeg(arg0, __float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def add(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).add(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(super(__Vector2, self).isOnLine(arg0, __float.valueOf(arg1)))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float.__wrap(super(__Vector2, self).dst2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).angle(arg0))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float.__wrap(super(Vector2, self).len2())

    @overload
    def rotate(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotate(__float.valueOf(arg0)))

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector2'.__wrap(super(__Vector2, self).interpolate(arg0, __float.valueOf(arg1), arg2))

    @overload
    def setLength2(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).setLength2(__float.valueOf(arg0)))

    @overload
    def sub(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Vector2, self).sub(arg0))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).sub(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotateAroundRad(arg0, __float.valueOf(arg1)))

    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float.__wrap(super(Vector2, self).angleDeg())

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).angleRad(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool.__wrap(super(Vector2, self).isUnit())

    @overload
    def setAngleDeg(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).setAngleDeg(__float.valueOf(arg0)))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).isOnLine(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float.__wrap(super(__Vector2, self).crs(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).set(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Vector2, self).mulAdd(arg0, arg1))

    @overload
    def rotateRad(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotateRad(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float.__wrap(super(Vector2, self).angleRad())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector2()"""
        val = __Vector2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector2'.__wrap(super(__Vector2, self).mul(arg0))

    @override
    @overload
    def nor(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'Vector2'.__wrap(super(Vector2, self).nor())

    @overload
    def set(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Vector2, self).set(arg0))

    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float.__wrap(super(Vector2, self).angle())

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).dst2(arg0))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float.__wrap(__Vector2.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setLength(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).setLength(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vector2, self).equals(arg0))

    @overload
    def fromString(self, arg0: str) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'Vector2'.__wrap(super(__Vector2, self).fromString(arg0))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len2(float,float)"""
        return float.__wrap(__Vector2.len2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool.__wrap(super(__Vector2, self).isUnit(__float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str.__wrap(super(Vector2, self).toString())

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool.__wrap(super(__Vector2, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float.__wrap(__Vector2.dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).angleDeg(arg0))

    @override
    @overload
    def cpy(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'Vector2'.__wrap(super(Vector2, self).cpy())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int.__wrap(super(Vector2, self).hashCode())

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).clamp(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def scl(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).scl(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def rotate90(self, arg0: int) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotate90(__int.valueOf(arg0)))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float.__wrap(super(__Vector2, self).dst(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector2'):
        """public com.badlogic.gdx.math.Vector2(com.badlogic.gdx.math.Vector2)"""
        val = __Vector2(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scl(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Vector2, self).scl(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).isCollinear(arg0))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).hasSameDirection(arg0))

    @overload
    def add(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Vector2, self).add(arg0))

    @overload
    def setAngleRad(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).setAngleRad(__float.valueOf(arg0)))

    @overload
    def scl(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).scl(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).epsilonEquals(arg0))

    @overload
    def limit2(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).limit2(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float.__wrap(super(__Vector2, self).dot(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def rotateDeg(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotateDeg(__float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector2()"""
        val = __Vector2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).dst(arg0))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool.__wrap(super(__Vector2, self).isZero(__float.valueOf(arg0)))

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).rotateAround(arg0, __float.valueOf(arg1)))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(super(__Vector2, self).dot(arg0))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float.__wrap(__Vector2.dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).idt(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Vector2, self).hasOppositeDirection(arg0))

    @override
    @overload
    def setZero(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'Vector2'.__wrap(super(Vector2, self).setZero())

    @overload
    def setAngle(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'Vector2'.__wrap(super(__Vector2, self).setAngle(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Vector
from abc import abstractmethod, ABC
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
 
class Vector(ABC):
    """com.badlogic.gdx.math.Vector"""
 
    @staticmethod
    def __wrap(java_value: __Vector) -> 'Vector':
        return Vector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector):
        """
        Dynamic initializer for Vector.
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
    def isOnLine(self, arg0: 'Vector', arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isOnLine(T,float)"""
        pass

    @abstractmethod
    def isOnLine(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.isOnLine(T)"""
        pass

    @abstractmethod
    def isZero(self, arg0: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isZero(float)"""
        pass

    @abstractmethod
    def setToRandomDirection(self, ):
        """public abstract T com.badlogic.gdx.math.Vector.setToRandomDirection()"""
        pass

    @abstractmethod
    def isCollinearOpposite(self, arg0: 'Vector', arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isCollinearOpposite(T,float)"""
        pass

    @abstractmethod
    def hasSameDirection(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.hasSameDirection(T)"""
        pass

    @abstractmethod
    def add(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.math.Vector.add(T)"""
        pass

    @abstractmethod
    def dot(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.math.Vector.dot(T)"""
        pass

    @abstractmethod
    def isPerpendicular(self, arg0: 'Vector', arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isPerpendicular(T,float)"""
        pass

    @abstractmethod
    def scl(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.math.Vector.scl(T)"""
        pass

    @abstractmethod
    def setLength(self, arg0: float):
        """public abstract T com.badlogic.gdx.math.Vector.setLength(float)"""
        pass

    @abstractmethod
    def dst2(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.math.Vector.dst2(T)"""
        pass

    @abstractmethod
    def isZero(self, ):
        """public abstract boolean com.badlogic.gdx.math.Vector.isZero()"""
        pass

    @abstractmethod
    def lerp(self, arg0: 'Vector', arg1: float):
        """public abstract T com.badlogic.gdx.math.Vector.lerp(T,float)"""
        pass

    @abstractmethod
    def epsilonEquals(self, arg0: 'Vector', arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.epsilonEquals(T,float)"""
        pass

    @abstractmethod
    def limit(self, arg0: float):
        """public abstract T com.badlogic.gdx.math.Vector.limit(float)"""
        pass

    @abstractmethod
    def isPerpendicular(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.isPerpendicular(T)"""
        pass

    @abstractmethod
    def cpy(self, ):
        """public abstract T com.badlogic.gdx.math.Vector.cpy()"""
        pass

    @abstractmethod
    def isCollinearOpposite(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.isCollinearOpposite(T)"""
        pass

    @abstractmethod
    def nor(self, ):
        """public abstract T com.badlogic.gdx.math.Vector.nor()"""
        pass

    @abstractmethod
    def mulAdd(self, arg0: 'Vector', arg1: float):
        """public abstract T com.badlogic.gdx.math.Vector.mulAdd(T,float)"""
        pass

    @abstractmethod
    def len2(self, ):
        """public abstract float com.badlogic.gdx.math.Vector.len2()"""
        pass

    @abstractmethod
    def setZero(self, ):
        """public abstract T com.badlogic.gdx.math.Vector.setZero()"""
        pass

    @abstractmethod
    def isUnit(self, ):
        """public abstract boolean com.badlogic.gdx.math.Vector.isUnit()"""
        pass

    @abstractmethod
    def isUnit(self, arg0: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isUnit(float)"""
        pass

    @abstractmethod
    def scl(self, arg0: float):
        """public abstract T com.badlogic.gdx.math.Vector.scl(float)"""
        pass

    @abstractmethod
    def dst(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.math.Vector.dst(T)"""
        pass

    @abstractmethod
    def set(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.math.Vector.set(T)"""
        pass

    @abstractmethod
    def mulAdd(self, arg0: 'Vector', arg1: 'Vector'):
        """public abstract T com.badlogic.gdx.math.Vector.mulAdd(T,T)"""
        pass

    @abstractmethod
    def isCollinear(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.isCollinear(T)"""
        pass

    @abstractmethod
    def sub(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.math.Vector.sub(T)"""
        pass

    @abstractmethod
    def clamp(self, arg0: float, arg1: float):
        """public abstract T com.badlogic.gdx.math.Vector.clamp(float,float)"""
        pass

    @abstractmethod
    def hasOppositeDirection(self, arg0: 'Vector'):
        """public abstract boolean com.badlogic.gdx.math.Vector.hasOppositeDirection(T)"""
        pass

    @abstractmethod
    def limit2(self, arg0: float):
        """public abstract T com.badlogic.gdx.math.Vector.limit2(float)"""
        pass

    @abstractmethod
    def len(self, ):
        """public abstract float com.badlogic.gdx.math.Vector.len()"""
        pass

    @abstractmethod
    def interpolate(self, arg0: 'Vector', arg1: float, arg2: 'Interpolation'):
        """public abstract T com.badlogic.gdx.math.Vector.interpolate(T,float,com.badlogic.gdx.math.Interpolation)"""
        pass

    @abstractmethod
    def isCollinear(self, arg0: 'Vector', arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Vector.isCollinear(T,float)"""
        pass

    @abstractmethod
    def setLength2(self, arg0: float):
        """public abstract T com.badlogic.gdx.math.Vector.setLength2(float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Pow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.math.Interpolation as __Interpolation_Pow
__Pow = __Interpolation_Pow.Pow
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pow():
    """com.badlogic.gdx.math.Interpolation.Pow"""
 
    @staticmethod
    def __wrap(java_value: __Pow) -> 'Pow':
        return Pow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pow):
        """
        Dynamic initializer for Pow.
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$Pow(int)"""
        val = __Pow(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Pow.apply(float)"""
        return float.__wrap(super(__Pow, self).apply(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ExpOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_ExpOut
__ExpOut = __Interpolation_ExpOut.ExpOut
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
 
class ExpOut():
    """com.badlogic.gdx.math.Interpolation.ExpOut"""
 
    @staticmethod
    def __wrap(java_value: __ExpOut) -> 'ExpOut':
        return ExpOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExpOut):
        """
        Dynamic initializer for ExpOut.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ExpOut.apply(float)"""
        return float.__wrap(super(__ExpOut, self).apply(__float.valueOf(arg0)))

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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Interpolation$ExpOut(float,float)"""
        val = __ExpOut(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Bounce
from builtins import str
import com.badlogic.gdx.math.Interpolation as __Interpolation_Bounce
__Bounce = __Interpolation_Bounce.Bounce
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
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
 
class Bounce():
    """com.badlogic.gdx.math.Interpolation.Bounce"""
 
    @staticmethod
    def __wrap(java_value: __Bounce) -> 'Bounce':
        return Bounce(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bounce):
        """
        Dynamic initializer for Bounce.
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$Bounce(int)"""
        val = __Bounce(__int.valueOf(arg0))
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

    @overload
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$Bounce(float[],float[])"""
        val = __Bounce(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Bounce.apply(float)"""
        return float.__wrap(super(__Bounce, self).apply(__float.valueOf(arg0)))

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.CatmullRomSpline
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.CatmullRomSpline as __CatmullRomSpline
__CatmullRomSpline = __CatmullRomSpline
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
from builtins import int
 
class CatmullRomSpline():
    """com.badlogic.gdx.math.CatmullRomSpline"""
 
    @staticmethod
    def __wrap(java_value: __CatmullRomSpline) -> 'CatmullRomSpline':
        return CatmullRomSpline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CatmullRomSpline):
        """
        Dynamic initializer for CatmullRomSpline.
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
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.valueAt(T,float)"""
        return 'Vector'.__wrap(super(__CatmullRomSpline, self).valueAt(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.CatmullRomSpline()"""
        val = __CatmullRomSpline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.derivativeAt(T,int,float)"""
        return 'Vector'.__wrap(super(__CatmullRomSpline, self).derivativeAt(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vector', arg1: bool) -> 'CatmullRomSpline':
        """public com.badlogic.gdx.math.CatmullRomSpline com.badlogic.gdx.math.CatmullRomSpline.set(T[],boolean)"""
        return 'CatmullRomSpline'.__wrap(super(__CatmullRomSpline, self).set(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.CatmullRomSpline()"""
        val = __CatmullRomSpline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nearest(self, arg0: 'Vector') -> int:
        """public int com.badlogic.gdx.math.CatmullRomSpline.nearest(T)"""
        return int.__wrap(super(__CatmullRomSpline, self).nearest(arg0))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T,int)"""
        return float.__wrap(super(__CatmullRomSpline, self).approximate(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.calculate(T,int,float,T[],boolean,T)"""
        return Vector.__wrap(__CatmullRomSpline.calculate(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), arg5))

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.locate(T)"""
        return float.__wrap(super(__CatmullRomSpline, self).locate(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T)"""
        return float.__wrap(super(__CatmullRomSpline, self).approximate(arg0))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.valueAt(T,int,float)"""
        return 'Vector'.__wrap(super(__CatmullRomSpline, self).valueAt(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approxLength(int)"""
        return float.__wrap(super(__CatmullRomSpline, self).approxLength(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.calculate(T,float,T[],boolean,T)"""
        return Vector.__wrap(__CatmullRomSpline.calculate(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.derivative(T,int,float,T[],boolean,T)"""
        return Vector.__wrap(__CatmullRomSpline.derivative(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), arg5))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.derivativeAt(T,float)"""
        return 'Vector'.__wrap(super(__CatmullRomSpline, self).derivativeAt(arg0, __float.valueOf(arg1)))

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
    def __init__(self, arg0: 'Vector', arg1: bool):
        """public com.badlogic.gdx.math.CatmullRomSpline(T[],boolean)"""
        val = __CatmullRomSpline(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nearest(self, arg0: 'Vector', arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.math.CatmullRomSpline.nearest(T,int,int)"""
        return int.__wrap(super(__CatmullRomSpline, self).nearest(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.derivative(T,float,T[],boolean,T)"""
        return Vector.__wrap(__CatmullRomSpline.derivative(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T,int,int)"""
        return float.__wrap(super(__CatmullRomSpline, self).approximate(arg0, __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Exp
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import com.badlogic.gdx.math.Interpolation as __Interpolation_Exp
__Exp = __Interpolation_Exp.Exp
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
 
class Exp():
    """com.badlogic.gdx.math.Interpolation.Exp"""
 
    @staticmethod
    def __wrap(java_value: __Exp) -> 'Exp':
        return Exp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Exp):
        """
        Dynamic initializer for Exp.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Exp.apply(float)"""
        return float.__wrap(super(__Exp, self).apply(__float.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Interpolation$Exp(float,float)"""
        val = __Exp(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Plane$PlaneSide
import com.badlogic.gdx.math.Plane as __Plane_PlaneSide
__PlaneSide = __Plane_PlaneSide.PlaneSide
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
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class PlaneSide():
    """com.badlogic.gdx.math.Plane.PlaneSide"""
 
    @staticmethod
    def __wrap(java_value: __PlaneSide) -> 'PlaneSide':
        return PlaneSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlaneSide):
        """
        Dynamic initializer for PlaneSide.
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
    def valueOf(arg0: str) -> 'PlaneSide':
        """public static com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane$PlaneSide.valueOf(java.lang.String)"""
        return PlaneSide.__wrap(__PlaneSide.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['PlaneSide']:
        """public static com.badlogic.gdx.math.Plane$PlaneSide[] com.badlogic.gdx.math.Plane$PlaneSide.values()"""
        return List[PlaneSide].__wrap(__PlaneSide.values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$SwingIn
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.math.Interpolation as __Interpolation_SwingIn
__SwingIn = __Interpolation_SwingIn.SwingIn
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
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
 
class SwingIn():
    """com.badlogic.gdx.math.Interpolation.SwingIn"""
 
    @staticmethod
    def __wrap(java_value: __SwingIn) -> 'SwingIn':
        return SwingIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SwingIn):
        """
        Dynamic initializer for SwingIn.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$SwingIn.apply(float)"""
        return float.__wrap(super(__SwingIn, self).apply(__float.valueOf(arg0)))

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$SwingIn(float)"""
        val = __SwingIn(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Circle
from builtins import str
import com.badlogic.gdx.math.Circle as __Circle
__Circle = __Circle
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
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Circle():
    """com.badlogic.gdx.math.Circle"""
 
    @staticmethod
    def __wrap(java_value: __Circle) -> 'Circle':
        return Circle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Circle):
        """
        Dynamic initializer for Circle.
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
    def __init__(self, ):
        """public com.badlogic.gdx.math.Circle()"""
        val = __Circle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Circle.hashCode()"""
        return int.__wrap(super(Circle, self).hashCode())

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Circle, self).contains(arg0))

    @overload
    def set(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Vector2,float)"""
        super(__Circle, self).set(arg0, __float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Circle.toString()"""
        return str.__wrap(super(Circle, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Circle.setPosition(float,float)"""
        super(__Circle, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def overlaps(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.overlaps(com.badlogic.gdx.math.Circle)"""
        return bool.__wrap(super(__Circle, self).overlaps(arg0))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setX(float)"""
        super(__Circle, self).setX(__float.valueOf(arg0))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Circle.area()"""
        return float.__wrap(super(Circle, self).area())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(float,float)"""
        return bool.__wrap(super(__Circle, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Circle(float,float,float)"""
        val = __Circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(com.badlogic.gdx.math.Circle)"""
        return bool.__wrap(super(__Circle, self).contains(arg0))

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setRadius(float)"""
        super(__Circle, self).setRadius(__float.valueOf(arg0))

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.math.Circle.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(__Circle, self).setPosition(arg0)

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Vector2,float)"""
        val = __Circle(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Circle.equals(java.lang.Object)"""
        return bool.__wrap(super(__Circle, self).equals(arg0))

    @overload
    def circumference(self) -> float:
        """public float com.badlogic.gdx.math.Circle.circumference()"""
        return float.__wrap(super(Circle, self).circumference())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.math.Circle.set(float,float,float)"""
        super(__Circle, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setY(float)"""
        super(__Circle, self).setY(__float.valueOf(arg0))

    @overload
    def set(self, arg0: 'Circle'):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Circle)"""
        super(__Circle, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__Circle, self).set(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = __Circle(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Circle()"""
        val = __Circle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Circle'):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Circle)"""
        val = __Circle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Rectangle
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Rectangle():
    """com.badlogic.gdx.math.Rectangle"""
 
    @staticmethod
    def __wrap(java_value: __Rectangle) -> 'Rectangle':
        return Rectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rectangle):
        """
        Dynamic initializer for Rectangle.
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
    def contains(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(super(__Rectangle, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getWidth()"""
        return float.__wrap(super(Rectangle, self).getWidth())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Rectangle()"""
        val = __Rectangle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCenter(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getCenter(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Rectangle, self).getCenter(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Rectangle()"""
        val = __Rectangle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Rectangle.toString()"""
        return str.__wrap(super(Rectangle, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getX()"""
        return float.__wrap(super(Rectangle, self).getX())

    @overload
    def fromString(self, arg0: str) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fromString(java.lang.String)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).fromString(arg0))

    @overload
    def getPosition(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Rectangle, self).getPosition(arg0))

    @overload
    def fitInside(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitInside(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).fitInside(arg0))

    @overload
    def merge(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).merge(arg0))

    @overload
    def setY(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setY(float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setY(__float.valueOf(arg0)))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getHeight()"""
        return float.__wrap(super(Rectangle, self).getHeight())

    @overload
    def getSize(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getSize(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Rectangle, self).getSize(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def merge(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).merge(arg0))

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setPosition(arg0))

    @overload
    def merge(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2[])"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).merge(arg0))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.area()"""
        return float.__wrap(super(Rectangle, self).area())

    @overload
    def getAspectRatio(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getAspectRatio()"""
        return float.__wrap(super(Rectangle, self).getAspectRatio())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(float,float)"""
        return bool.__wrap(super(__Rectangle, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Rectangle, self).contains(arg0))

    @overload
    def setSize(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setSize(__float.valueOf(arg0)))

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Circle)"""
        return bool.__wrap(super(__Rectangle, self).contains(arg0))

    @overload
    def setCenter(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setCenter(arg0))

    @overload
    def set(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).set(arg0))

    @overload
    def setCenter(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(float,float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setCenter(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setX(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setX(float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setX(__float.valueOf(arg0)))

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(float,float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def overlaps(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.overlaps(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(super(__Rectangle, self).overlaps(arg0))

    @overload
    def setWidth(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setWidth(float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setWidth(__float.valueOf(arg0)))

    @overload
    def merge(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(float,float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).merge(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getY()"""
        return float.__wrap(super(Rectangle, self).getY())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Rectangle.hashCode()"""
        return int.__wrap(super(Rectangle, self).hashCode())

    @overload
    def __init__(self, arg0: 'Rectangle'):
        """public com.badlogic.gdx.math.Rectangle(com.badlogic.gdx.math.Rectangle)"""
        val = __Rectangle(arg0)
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

    @overload
    def setHeight(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setHeight(float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setHeight(__float.valueOf(arg0)))

    @overload
    def fitOutside(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitOutside(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).fitOutside(arg0))

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float,float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def perimeter(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.perimeter()"""
        return float.__wrap(super(Rectangle, self).perimeter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.equals(java.lang.Object)"""
        return bool.__wrap(super(__Rectangle, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(float,float,float,float)"""
        return 'Rectangle'.__wrap(super(__Rectangle, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Rectangle(float,float,float,float)"""
        val = __Rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Elastic
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_Elastic
__Elastic = __Interpolation_Elastic.Elastic
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
 
class Elastic():
    """com.badlogic.gdx.math.Interpolation.Elastic"""
 
    @staticmethod
    def __wrap(java_value: __Elastic) -> 'Elastic':
        return Elastic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Elastic):
        """
        Dynamic initializer for Elastic.
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
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$Elastic(float,float,int,float)"""
        val = __Elastic(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Elastic.apply(float)"""
        return float.__wrap(super(__Elastic, self).apply(__float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Path
import com.badlogic.gdx.math.Path as __Path
__Path = __Path
from abc import abstractmethod, ABC
 
class Path(ABC):
    """com.badlogic.gdx.math.Path"""
 
    @staticmethod
    def __wrap(java_value: __Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Path):
        """
        Dynamic initializer for Path.
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
    def valueAt(self, arg0: object, arg1: float):
        """public abstract T com.badlogic.gdx.math.Path.valueAt(T,float)"""
        pass

    @abstractmethod
    def approximate(self, arg0: object):
        """public abstract float com.badlogic.gdx.math.Path.approximate(T)"""
        pass

    @abstractmethod
    def derivativeAt(self, arg0: object, arg1: float):
        """public abstract T com.badlogic.gdx.math.Path.derivativeAt(T,float)"""
        pass

    @abstractmethod
    def approxLength(self, arg0: int):
        """public abstract float com.badlogic.gdx.math.Path.approxLength(int)"""
        pass

    @abstractmethod
    def locate(self, arg0: object):
        """public abstract float com.badlogic.gdx.math.Path.locate(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ElasticOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_ElasticOut
__ElasticOut = __Interpolation_ElasticOut.ElasticOut
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
 
class ElasticOut():
    """com.badlogic.gdx.math.Interpolation.ElasticOut"""
 
    @staticmethod
    def __wrap(java_value: __ElasticOut) -> 'ElasticOut':
        return ElasticOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ElasticOut):
        """
        Dynamic initializer for ElasticOut.
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

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$ElasticOut(float,float,int,float)"""
        val = __ElasticOut(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ElasticOut.apply(float)"""
        return float.__wrap(super(__ElasticOut, self).apply(__float.valueOf(arg0)))

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Plane
import com.badlogic.gdx.math.Plane as __Plane_PlaneSide
__PlaneSide = __Plane_PlaneSide.PlaneSide
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.math.Plane as __Plane
__Plane = __Plane
from builtins import float
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
 
class Plane():
    """com.badlogic.gdx.math.Plane"""
 
    @staticmethod
    def __wrap(java_value: __Plane) -> 'Plane':
        return Plane(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Plane):
        """
        Dynamic initializer for Plane.
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
    def testPoint(self, arg0: float, arg1: float, arg2: float) -> 'PlaneSide':
        """public com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane.testPoint(float,float,float)"""
        return 'PlaneSide'.__wrap(super(__Plane, self).testPoint(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,float)"""
        val = __Plane(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Plane.toString()"""
        return str.__wrap(super(Plane, self).toString())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.math.Plane.set(float,float,float,float,float,float)"""
        super(__Plane, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__Plane, self).set(arg0, arg1, arg2)

    @overload
    def testPoint(self, arg0: 'Vector3') -> 'PlaneSide':
        """public com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane.testPoint(com.badlogic.gdx.math.Vector3)"""
        return 'PlaneSide'.__wrap(super(__Plane, self).testPoint(arg0))

    @overload
    def isFrontFacing(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Plane.isFrontFacing(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Plane, self).isFrontFacing(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__Plane, self).set(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Plane()"""
        val = __Plane()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def distance(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Plane.distance(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Plane, self).distance(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.math.Plane.set(float,float,float,float)"""
        super(__Plane, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Plane()"""
        val = __Plane()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getD(self) -> float:
        """public float com.badlogic.gdx.math.Plane.getD()"""
        return float.__wrap(super(Plane, self).getD())

    @overload
    def getNormal(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Plane.getNormal()"""
        return 'Vector3'.__wrap(super(Plane, self).getNormal())

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __Plane(arg0, arg1, arg2)
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

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __Plane(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Plane'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Plane)"""
        super(__Plane, self).set(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.math.ConvexHull
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.FloatArray as __FloatArray
__FloatArray = __FloatArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.math.ConvexHull as __ConvexHull
__ConvexHull = __ConvexHull
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.IntArray as __IntArray
__IntArray = __IntArray
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConvexHull():
    """com.badlogic.gdx.math.ConvexHull"""
 
    @staticmethod
    def __wrap(java_value: __ConvexHull) -> 'ConvexHull':
        return ConvexHull(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConvexHull):
        """
        Dynamic initializer for ConvexHull.
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
    def computeIndices(self, arg0: 'float', arg1: int, arg2: int, arg3: bool, arg4: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(float[],int,int,boolean,boolean)"""
        return 'utils.IntArray'.__wrap(super(__ConvexHull, self).computeIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4)))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.ConvexHull()"""
        val = __ConvexHull()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def computePolygon(self, arg0: 'float', arg1: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(float[],boolean)"""
        return 'utils.FloatArray'.__wrap(super(__ConvexHull, self).computePolygon(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.ConvexHull()"""
        val = __ConvexHull()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def computePolygon(self, arg0: 'float', arg1: int, arg2: int, arg3: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(float[],int,int,boolean)"""
        return 'utils.FloatArray'.__wrap(super(__ConvexHull, self).computePolygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def computeIndices(self, arg0: 'FloatArray', arg1: bool, arg2: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(com.badlogic.gdx.utils.FloatArray,boolean,boolean)"""
        return 'utils.IntArray'.__wrap(super(__ConvexHull, self).computeIndices(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def computeIndices(self, arg0: 'float', arg1: bool, arg2: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(float[],boolean,boolean)"""
        return 'utils.IntArray'.__wrap(super(__ConvexHull, self).computeIndices(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def computePolygon(self, arg0: 'FloatArray', arg1: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(com.badlogic.gdx.utils.FloatArray,boolean)"""
        return 'utils.FloatArray'.__wrap(super(__ConvexHull, self).computePolygon(arg0, __boolean.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.math.FloatCounter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.math.FloatCounter as __FloatCounter
__FloatCounter = __FloatCounter
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
 
class FloatCounter():
    """com.badlogic.gdx.math.FloatCounter"""
 
    @staticmethod
    def __wrap(java_value: __FloatCounter) -> 'FloatCounter':
        return FloatCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatCounter):
        """
        Dynamic initializer for FloatCounter.
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
    def reset(self):
        """public void com.badlogic.gdx.math.FloatCounter.reset()"""
        super(FloatCounter, self).reset()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.FloatCounter(int)"""
        val = __FloatCounter(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def put(self, arg0: float):
        """public void com.badlogic.gdx.math.FloatCounter.put(float)"""
        super(__FloatCounter, self).put(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.FloatCounter.toString()"""
        return str.__wrap(super(FloatCounter, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Octree$OctreeNode
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
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.Octree as __Octree_OctreeNode
__OctreeNode = __Octree_OctreeNode.OctreeNode
from builtins import int
 
class OctreeNode():
    """com.badlogic.gdx.math.Octree.OctreeNode"""
 
    @staticmethod
    def __wrap(java_value: __OctreeNode) -> 'OctreeNode':
        return OctreeNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OctreeNode):
        """
        Dynamic initializer for OctreeNode.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Octree$RayCastResult
from builtins import str
import com.badlogic.gdx.math.Octree as __Octree_RayCastResult
__RayCastResult = __Octree_RayCastResult.RayCastResult
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RayCastResult():
    """com.badlogic.gdx.math.Octree.RayCastResult"""
 
    @staticmethod
    def __wrap(java_value: __RayCastResult) -> 'RayCastResult':
        return RayCastResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayCastResult):
        """
        Dynamic initializer for RayCastResult.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Octree$RayCastResult()"""
        val = __RayCastResult()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Octree$RayCastResult()"""
        val = __RayCastResult()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.WindowedMean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.math.WindowedMean as __WindowedMean
__WindowedMean = __WindowedMean
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WindowedMean():
    """com.badlogic.gdx.math.WindowedMean"""
 
    @staticmethod
    def __wrap(java_value: __WindowedMean) -> 'WindowedMean':
        return WindowedMean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowedMean):
        """
        Dynamic initializer for WindowedMean.
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
    def hasEnoughData(self) -> bool:
        """public boolean com.badlogic.gdx.math.WindowedMean.hasEnoughData()"""
        return bool.__wrap(super(WindowedMean, self).hasEnoughData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getHighest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getHighest()"""
        return float.__wrap(super(WindowedMean, self).getHighest())

    @overload
    def getWindowSize(self) -> int:
        """public int com.badlogic.gdx.math.WindowedMean.getWindowSize()"""
        return int.__wrap(super(WindowedMean, self).getWindowSize())

    @overload
    def getLowest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getLowest()"""
        return float.__wrap(super(WindowedMean, self).getLowest())

    @overload
    def getMean(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getMean()"""
        return float.__wrap(super(WindowedMean, self).getMean())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getOldest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getOldest()"""
        return float.__wrap(super(WindowedMean, self).getOldest())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.WindowedMean(int)"""
        val = __WindowedMean(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWindowValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.WindowedMean.getWindowValues()"""
        return List[float].__wrap(super(WindowedMean, self).getWindowValues())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLatest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getLatest()"""
        return float.__wrap(super(WindowedMean, self).getLatest())

    @overload
    def addValue(self, arg0: float):
        """public void com.badlogic.gdx.math.WindowedMean.addValue(float)"""
        super(__WindowedMean, self).addValue(__float.valueOf(arg0))

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
    def clear(self):
        """public void com.badlogic.gdx.math.WindowedMean.clear()"""
        super(WindowedMean, self).clear()

    @overload
    def standardDeviation(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.standardDeviation()"""
        return float.__wrap(super(WindowedMean, self).standardDeviation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getValueCount(self) -> int:
        """public int com.badlogic.gdx.math.WindowedMean.getValueCount()"""
        return int.__wrap(super(WindowedMean, self).getValueCount()) 
 
 
# CLASS: com.badlogic.gdx.math.Affine2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.Affine2 as __Affine2
__Affine2 = __Affine2
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Affine2():
    """com.badlogic.gdx.math.Affine2"""
 
    @staticmethod
    def __wrap(java_value: __Affine2) -> 'Affine2':
        return Affine2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Affine2):
        """
        Dynamic initializer for Affine2.
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
    def preShear(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preShear(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preShear(arg0))

    @overload
    def set(self, arg0: 'Matrix4') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Affine2'.__wrap(super(__Affine2, self).set(arg0))

    @overload
    def mul(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.mul(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).mul(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.translate(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).translate(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def preScale(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preScale(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preScale(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setToRotationRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotationRad(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToRotationRad(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setToRotation(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotation(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToRotation(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).set(arg0))

    @overload
    def setToTrnRotScl(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotScl(float,float,float,float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnRotScl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def setToTrnScl(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnScl(float,float,float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnScl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def preTranslate(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preTranslate(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preTranslate(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def preRotateRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preRotateRad(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preRotateRad(__float.valueOf(arg0)))

    @overload
    def preShear(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preShear(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preShear(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def preMul(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preMul(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preMul(arg0))

    @overload
    def inv(self) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.inv()"""
        return 'Affine2'.__wrap(super(Affine2, self).inv())

    @overload
    def setToTrnRotScl(self, arg0: 'Vector2', arg1: float, arg2: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotScl(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnRotScl(arg0, __float.valueOf(arg1), arg2))

    @overload
    def rotate(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.rotate(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).rotate(__float.valueOf(arg0)))

    @overload
    def rotateRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.rotateRad(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).rotateRad(__float.valueOf(arg0)))

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Affine2.det()"""
        return float.__wrap(super(Affine2, self).det())

    @overload
    def setToProduct(self, arg0: 'Affine2', arg1: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToProduct(com.badlogic.gdx.math.Affine2,com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToProduct(arg0, arg1))

    @overload
    def preRotate(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preRotate(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preRotate(__float.valueOf(arg0)))

    @overload
    def setToTranslation(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTranslation(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTranslation(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Affine2'):
        """public com.badlogic.gdx.math.Affine2(com.badlogic.gdx.math.Affine2)"""
        val = __Affine2(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setToShearing(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToShearing(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToShearing(arg0))

    @overload
    def setToTrnScl(self, arg0: 'Vector2', arg1: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnScl(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnScl(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Affine2.toString()"""
        return str.__wrap(super(Affine2, self).toString())

    @overload
    def setToScaling(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToScaling(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToScaling(arg0))

    @overload
    def preTranslate(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preTranslate(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preTranslate(arg0))

    @overload
    def setToTrnRotRadScl(self, arg0: 'Vector2', arg1: float, arg2: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotRadScl(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnRotRadScl(arg0, __float.valueOf(arg1), arg2))

    @overload
    def translate(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.translate(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).translate(arg0))

    @overload
    def preScale(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preScale(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).preScale(arg0))

    @overload
    def idt(self) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.idt()"""
        return 'Affine2'.__wrap(super(Affine2, self).idt())

    @overload
    def isTranslation(self) -> bool:
        """public boolean com.badlogic.gdx.math.Affine2.isTranslation()"""
        return bool.__wrap(super(Affine2, self).isTranslation())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def shear(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.shear(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).shear(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def applyTo(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.math.Affine2.applyTo(com.badlogic.gdx.math.Vector2)"""
        super(__Affine2, self).applyTo(arg0)

    @overload
    def setToTranslation(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTranslation(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Affine2()"""
        val = __Affine2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def shear(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.shear(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).shear(arg0))

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.scale(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).scale(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setToRotation(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotation(float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToRotation(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setToShearing(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToShearing(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToShearing(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setToScaling(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToScaling(float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToScaling(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isIdt(self) -> bool:
        """public boolean com.badlogic.gdx.math.Affine2.isIdt()"""
        return bool.__wrap(super(Affine2, self).isIdt())

    @overload
    def set(self, arg0: 'Matrix3') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Affine2'.__wrap(super(__Affine2, self).set(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Affine2()"""
        val = __Affine2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.scale(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'.__wrap(super(__Affine2, self).scale(arg0))

    @overload
    def getTranslation(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Affine2.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Affine2, self).getTranslation(arg0))

    @overload
    def setToTrnRotRadScl(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotRadScl(float,float,float,float,float)"""
        return 'Affine2'.__wrap(super(__Affine2, self).setToTrnRotRadScl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))) 
 
 
# CLASS: com.badlogic.gdx.math.CumulativeDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.math.CumulativeDistribution as __CumulativeDistribution
__CumulativeDistribution = __CumulativeDistribution
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CumulativeDistribution():
    """com.badlogic.gdx.math.CumulativeDistribution"""
 
    @staticmethod
    def __wrap(java_value: __CumulativeDistribution) -> 'CumulativeDistribution':
        return CumulativeDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CumulativeDistribution):
        """
        Dynamic initializer for CumulativeDistribution.
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
    def setInterval(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.setInterval(int,float)"""
        super(__CumulativeDistribution, self).setInterval(__int.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.CumulativeDistribution()"""
        val = __CumulativeDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getInterval(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.CumulativeDistribution.getInterval(int)"""
        return float.__wrap(super(__CumulativeDistribution, self).getInterval(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.math.CumulativeDistribution.add(T)"""
        super(__CumulativeDistribution, self).add(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.CumulativeDistribution()"""
        val = __CumulativeDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def value(self, arg0: float) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.value(float)"""
        return object.__wrap(super(__CumulativeDistribution, self).value(__float.valueOf(arg0)))

    @overload
    def value(self) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.value()"""
        return object.__wrap(super(CumulativeDistribution, self).value())

    @overload
    def generateUniform(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.generateUniform()"""
        super(CumulativeDistribution, self).generateUniform()

    @overload
    def getValue(self, arg0: int) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.getValue(int)"""
        return object.__wrap(super(__CumulativeDistribution, self).getValue(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.math.CumulativeDistribution.size()"""
        return int.__wrap(super(CumulativeDistribution, self).size())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.clear()"""
        super(CumulativeDistribution, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setInterval(self, arg0: object, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.setInterval(T,float)"""
        super(__CumulativeDistribution, self).setInterval(arg0, __float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def generate(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.generate()"""
        super(CumulativeDistribution, self).generate()

    @overload
    def generateNormalized(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.generateNormalized()"""
        super(CumulativeDistribution, self).generateNormalized()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def add(self, arg0: object, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.add(T,float)"""
        super(__CumulativeDistribution, self).add(arg0, __float.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.math.Intersector as __Intersector
__Intersector = __Intersector
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class Intersector():
    """com.badlogic.gdx.math.Intersector"""
 
    @staticmethod
    def __wrap(java_value: __Intersector) -> 'Intersector':
        return Intersector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Intersector):
        """
        Dynamic initializer for Intersector.
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
    def intersectRayRay(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> float:
        """public static float com.badlogic.gdx.math.Intersector.intersectRayRay(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(__Intersector.intersectRayRay(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isPointInPolygon(arg0: 'Array', arg1: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInPolygon(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.isPointInPolygon(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayBoundsFast(arg0: 'Ray', arg1: 'Vector3', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayBoundsFast(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def intersectSegmentPlane(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Plane', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentPlane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectSegmentPlane(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.isPointInTriangle(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.isPointInTriangle(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def intersectLines(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLines(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.intersectLines(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), arg8))

    @staticmethod
    @overload
    def intersectLinePolygon(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLinePolygon(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Polygon)"""
        return bool.__wrap(__Intersector.intersectLinePolygon(arg0, arg1, arg2))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'Polygon', arg1: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon)"""
        return bool.__wrap(__Intersector.overlapConvexPolygons(arg0, arg1))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'Polygon', arg1: 'Polygon', arg2: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool.__wrap(__Intersector.overlapConvexPolygons(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayOrientedBounds(arg0: 'Ray', arg1: 'OrientedBoundingBox', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.OrientedBoundingBox,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayOrientedBounds(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def intersectSegments(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegments(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.intersectSegments(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def intersectPolygons(arg0: 'FloatArray', arg1: 'FloatArray') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygons(com.badlogic.gdx.utils.FloatArray,com.badlogic.gdx.utils.FloatArray)"""
        return bool.__wrap(__Intersector.intersectPolygons(arg0, arg1))

    @staticmethod
    @overload
    def intersectSegmentCircle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Circle', arg3: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentCircle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool.__wrap(__Intersector.intersectSegmentCircle(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def intersectRaySphere(arg0: 'Ray', arg1: 'Vector3', arg2: float, arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRaySphere(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,float,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRaySphere(arg0, arg1, __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def intersectLines(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLines(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.intersectLines(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def intersectBoundsPlaneFast(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectBoundsPlaneFast(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(__Intersector.intersectBoundsPlaneFast(arg0, arg1, arg2, __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isPointInPolygon(arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInPolygon(float[],int,int,float,float)"""
        return bool.__wrap(__Intersector.isPointInPolygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def intersectRectangles(arg0: 'Rectangle', arg1: 'Rectangle', arg2: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRectangles(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__Intersector.intersectRectangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def distanceSegmentPoint(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2') -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceSegmentPoint(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(__Intersector.distanceSegmentPoint(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayBoundsFast(arg0: 'Ray', arg1: 'BoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(__Intersector.intersectRayBoundsFast(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayBounds(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def intersectRayOrientedBoundsFast(arg0: 'Ray', arg1: 'OrientedBoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(__Intersector.intersectRayOrientedBoundsFast(arg0, arg1))

    @staticmethod
    @overload
    def intersectSegmentPolygon(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentPolygon(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Polygon)"""
        return bool.__wrap(__Intersector.intersectSegmentPolygon(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayOrientedBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Matrix4', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayOrientedBounds(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def overlaps(arg0: 'Circle', arg1: 'Circle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Circle)"""
        return bool.__wrap(__Intersector.overlaps(arg0, arg1))

    @staticmethod
    @overload
    def intersectPolygonEdges(arg0: 'FloatArray', arg1: 'FloatArray') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygonEdges(com.badlogic.gdx.utils.FloatArray,com.badlogic.gdx.utils.FloatArray)"""
        return bool.__wrap(__Intersector.intersectPolygonEdges(arg0, arg1))

    @staticmethod
    @overload
    def distanceLinePoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceLinePoint(float,float,float,float,float,float)"""
        return float.__wrap(__Intersector.distanceLinePoint(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def intersectBoundsPlaneFast(arg0: 'BoundingBox', arg1: 'Plane') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectBoundsPlaneFast(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Plane)"""
        return bool.__wrap(__Intersector.intersectBoundsPlaneFast(arg0, arg1))

    @staticmethod
    @overload
    def splitTriangle(arg0: 'float', arg1: 'Plane', arg2: 'SplitTriangle'):
        """public static void com.badlogic.gdx.math.Intersector.splitTriangle(float[],com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Intersector$SplitTriangle)"""
        __Intersector.splitTriangle(arg0, arg1, arg2)

    @staticmethod
    @overload
    def intersectPolygons(arg0: 'Polygon', arg1: 'Polygon', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon)"""
        return bool.__wrap(__Intersector.intersectPolygons(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayTriangle(arg0: 'Ray', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangle(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayTriangle(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'float', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,float[],com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayTriangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectPlanes(arg0: 'Plane', arg1: 'Plane', arg2: 'Plane', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPlanes(com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectPlanes(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nearestSegmentPoint(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Intersector.nearestSegmentPoint(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__Intersector.nearestSegmentPoint(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def intersectSegmentCircle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentCircle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        return bool.__wrap(__Intersector.intersectSegmentCircle(arg0, arg1, arg2, __float.valueOf(arg3)))

    @staticmethod
    @overload
    def distanceSegmentPoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceSegmentPoint(float,float,float,float,float,float)"""
        return float.__wrap(__Intersector.distanceSegmentPoint(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def intersectFrustumBounds(arg0: 'Frustum', arg1: 'OrientedBoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectFrustumBounds(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(__Intersector.intersectFrustumBounds(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayPlane(arg0: 'Ray', arg1: 'Plane', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayPlane(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayPlane(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'float', arg2: 'short', arg3: int, arg4: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,float[],short[],int,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayTriangles(arg0, arg1, arg2, __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nearestSegmentPoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Intersector.nearestSegmentPoint(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__Intersector.nearestSegmentPoint(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(float,float,float,float,float,float,float,float)"""
        return bool.__wrap(__Intersector.isPointInTriangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'List', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,java.util.List<com.badlogic.gdx.math.Vector3>,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(__Intersector.intersectRayTriangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegmentRectangle(arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentRectangle(float,float,float,float,com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__Intersector.intersectSegmentRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def intersectRayOrientedBoundsFast(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Matrix4') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return bool.__wrap(__Intersector.intersectRayOrientedBoundsFast(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectLinePlane(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Plane', arg7: 'Vector3') -> float:
        """public static float com.badlogic.gdx.math.Intersector.intersectLinePlane(float,float,float,float,float,float,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(__Intersector.intersectLinePlane(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'float', arg1: 'float', arg2: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(float[],float[],com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool.__wrap(__Intersector.overlapConvexPolygons(arg0, arg1, arg2))

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
    def hasOverlap(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.hasOverlap(com.badlogic.gdx.math.Vector3[],com.badlogic.gdx.math.Vector3[],com.badlogic.gdx.math.Vector3[])"""
        return bool.__wrap(__Intersector.hasOverlap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def pointLineSide(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> int:
        """public static int com.badlogic.gdx.math.Intersector.pointLineSide(float,float,float,float,float,float)"""
        return int.__wrap(__Intersector.pointLineSide(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def pointLineSide(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2') -> int:
        """public static int com.badlogic.gdx.math.Intersector.pointLineSide(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return int.__wrap(__Intersector.pointLineSide(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectFrustumBounds(arg0: 'Frustum', arg1: 'BoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectFrustumBounds(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(__Intersector.intersectFrustumBounds(arg0, arg1))

    @staticmethod
    @overload
    def overlaps(arg0: 'Circle', arg1: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__Intersector.overlaps(arg0, arg1))

    @staticmethod
    @overload
    def overlaps(arg0: 'Rectangle', arg1: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__Intersector.overlaps(arg0, arg1))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'float', arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int, arg6: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(float[],int,int,float[],int,int,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool.__wrap(__Intersector.overlapConvexPolygons(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4), __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def intersectSegmentRectangle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentRectangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__Intersector.intersectSegmentRectangle(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegments(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegments(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__Intersector.intersectSegments(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), arg8)) 
 
 
# CLASS: com.badlogic.gdx.math.CumulativeDistribution$CumulativeValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
import com.badlogic.gdx.math.CumulativeDistribution as __CumulativeDistribution_CumulativeValue
__CumulativeValue = __CumulativeDistribution_CumulativeValue.CumulativeValue
from builtins import int
 
class CumulativeValue():
    """com.badlogic.gdx.math.CumulativeDistribution.CumulativeValue"""
 
    @staticmethod
    def __wrap(java_value: __CumulativeValue) -> 'CumulativeValue':
        return CumulativeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CumulativeValue):
        """
        Dynamic initializer for CumulativeValue.
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
    def __init__(self, arg0: 'CumulativeDistribution', arg1: object, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.CumulativeDistribution$CumulativeValue(T,float,float)"""
        val = __CumulativeValue(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.math.GridPoint3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.GridPoint3 as __GridPoint3
__GridPoint3 = __GridPoint3
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
 
class GridPoint3():
    """com.badlogic.gdx.math.GridPoint3"""
 
    @staticmethod
    def __wrap(java_value: __GridPoint3) -> 'GridPoint3':
        return GridPoint3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GridPoint3):
        """
        Dynamic initializer for GridPoint3.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.math.GridPoint3(int,int,int)"""
        val = __GridPoint3(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.GridPoint3()"""
        val = __GridPoint3()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.set(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).set(arg0))

    @overload
    def cpy(self) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.cpy()"""
        return 'GridPoint3'.__wrap(super(GridPoint3, self).cpy())

    @overload
    def add(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.add(int,int,int)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).add(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def add(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.add(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).add(arg0))

    @overload
    def __init__(self, arg0: 'GridPoint3'):
        """public com.badlogic.gdx.math.GridPoint3(com.badlogic.gdx.math.GridPoint3)"""
        val = __GridPoint3(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.GridPoint3.hashCode()"""
        return int.__wrap(super(GridPoint3, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.set(int,int,int)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def dst(self, arg0: 'GridPoint3') -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst(com.badlogic.gdx.math.GridPoint3)"""
        return float.__wrap(super(__GridPoint3, self).dst(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.GridPoint3.equals(java.lang.Object)"""
        return bool.__wrap(super(__GridPoint3, self).equals(arg0))

    @overload
    def dst2(self, arg0: 'GridPoint3') -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst2(com.badlogic.gdx.math.GridPoint3)"""
        return float.__wrap(super(__GridPoint3, self).dst2(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.GridPoint3.toString()"""
        return str.__wrap(super(GridPoint3, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.GridPoint3()"""
        val = __GridPoint3()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sub(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.sub(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).sub(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst(int,int,int)"""
        return float.__wrap(super(__GridPoint3, self).dst(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def dst2(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst2(int,int,int)"""
        return float.__wrap(super(__GridPoint3, self).dst2(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.sub(int,int,int)"""
        return 'GridPoint3'.__wrap(super(__GridPoint3, self).sub(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.math.Polygon
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Polygon as __Polygon
__Polygon = __Polygon
from builtins import bool
from builtins import int
 
class Polygon():
    """com.badlogic.gdx.math.Polygon"""
 
    @staticmethod
    def __wrap(java_value: __Polygon) -> 'Polygon':
        return Polygon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Polygon):
        """
        Dynamic initializer for Polygon.
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
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.area()"""
        return float.__wrap(super(Polygon, self).area())

    @overload
    def getTransformedVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polygon.getTransformedVertices()"""
        return List[float].__wrap(super(Polygon, self).getTransformedVertices())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getY()"""
        return float.__wrap(super(Polygon, self).getY())

    @overload
    def getCentroid(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Polygon.getCentroid(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Polygon, self).getCentroid(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Polygon.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Polygon, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.rotate(float)"""
        super(__Polygon, self).rotate(__float.valueOf(arg0))

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setScale(float,float)"""
        super(__Polygon, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.translate(float,float)"""
        super(__Polygon, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getOriginY()"""
        return float.__wrap(super(Polygon, self).getOriginY())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Polygon()"""
        val = __Polygon()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Polygon.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'.__wrap(super(__Polygon, self).getVertex(__int.valueOf(arg0), arg1))

    @overload
    def setVertices(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Polygon.setVertices(float[])"""
        super(__Polygon, self).setVertices(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.math.Polygon.getVertexCount()"""
        return int.__wrap(super(Polygon, self).getVertexCount())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Polygon(float[])"""
        val = __Polygon(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getScaleX()"""
        return float.__wrap(super(Polygon, self).getScaleX())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setPosition(float,float)"""
        super(__Polygon, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.setRotation(float)"""
        super(__Polygon, self).setRotation(__float.valueOf(arg0))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polygon.getVertices()"""
        return List[float].__wrap(super(Polygon, self).getVertices())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Polygon()"""
        val = __Polygon()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Polygon.contains(float,float)"""
        return bool.__wrap(super(__Polygon, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getOriginX()"""
        return float.__wrap(super(Polygon, self).getOriginX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setVertex(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.math.Polygon.setVertex(int,float,float)"""
        super(__Polygon, self).setVertex(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setOrigin(float,float)"""
        super(__Polygon, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBoundingRectangle(self) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Polygon.getBoundingRectangle()"""
        return 'Rectangle'.__wrap(super(Polygon, self).getBoundingRectangle())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getScaleY()"""
        return float.__wrap(super(Polygon, self).getScaleY())

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getRotation()"""
        return float.__wrap(super(Polygon, self).getRotation())

    @overload
    def dirty(self):
        """public void com.badlogic.gdx.math.Polygon.dirty()"""
        super(Polygon, self).dirty()

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getX()"""
        return float.__wrap(super(Polygon, self).getX())

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.scale(float)"""
        super(__Polygon, self).scale(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$PowOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_PowOut
__PowOut = __Interpolation_PowOut.PowOut
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
 
class PowOut():
    """com.badlogic.gdx.math.Interpolation.PowOut"""
 
    @staticmethod
    def __wrap(java_value: __PowOut) -> 'PowOut':
        return PowOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PowOut):
        """
        Dynamic initializer for PowOut.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$PowOut.apply(float)"""
        return float.__wrap(super(__PowOut, self).apply(__float.valueOf(arg0)))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$PowOut(int)"""
        val = __PowOut(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
from builtins import float
from abc import abstractmethod, ABC
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
 
class Interpolation(ABC):
    """com.badlogic.gdx.math.Interpolation"""
 
    @staticmethod
    def __wrap(java_value: __Interpolation) -> 'Interpolation':
        return Interpolation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Interpolation):
        """
        Dynamic initializer for Interpolation.
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

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract float com.badlogic.gdx.math.Interpolation.apply(float)"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Interpolation()"""
        val = __Interpolation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Interpolation()"""
        val = __Interpolation()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.EarClippingTriangulator
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ShortArray as __ShortArray
__ShortArray = __ShortArray
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.EarClippingTriangulator as __EarClippingTriangulator
__EarClippingTriangulator = __EarClippingTriangulator
from builtins import int
 
class EarClippingTriangulator():
    """com.badlogic.gdx.math.EarClippingTriangulator"""
 
    @staticmethod
    def __wrap(java_value: __EarClippingTriangulator) -> 'EarClippingTriangulator':
        return EarClippingTriangulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EarClippingTriangulator):
        """
        Dynamic initializer for EarClippingTriangulator.
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
    def computeTriangles(self, arg0: 'float', arg1: int, arg2: int) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(float[],int,int)"""
        return 'utils.ShortArray'.__wrap(super(__EarClippingTriangulator, self).computeTriangles(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.EarClippingTriangulator()"""
        val = __EarClippingTriangulator()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.EarClippingTriangulator()"""
        val = __EarClippingTriangulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def computeTriangles(self, arg0: 'float') -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(float[])"""
        return 'utils.ShortArray'.__wrap(super(__EarClippingTriangulator, self).computeTriangles(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def computeTriangles(self, arg0: 'FloatArray') -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(com.badlogic.gdx.utils.FloatArray)"""
        return 'utils.ShortArray'.__wrap(super(__EarClippingTriangulator, self).computeTriangles(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.GeometryUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import com.badlogic.gdx.math.GeometryUtils as __GeometryUtils
__GeometryUtils = __GeometryUtils
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
 
class GeometryUtils():
    """com.badlogic.gdx.math.GeometryUtils"""
 
    @staticmethod
    def __wrap(java_value: __GeometryUtils) -> 'GeometryUtils':
        return GeometryUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GeometryUtils):
        """
        Dynamic initializer for GeometryUtils.
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
    def polygonArea(arg0: 'float', arg1: int, arg2: int) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.polygonArea(float[],int,int)"""
        return float.__wrap(__GeometryUtils.polygonArea(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def triangleQuality(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleQuality(float,float,float,float,float,float)"""
        return float.__wrap(__GeometryUtils.triangleQuality(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def polygonCentroid(arg0: 'float', arg1: int, arg2: int, arg3: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.polygonCentroid(float[],int,int,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.polygonCentroid(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def triangleArea(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleArea(float,float,float,float,float,float)"""
        return float.__wrap(__GeometryUtils.triangleArea(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[])"""
        __GeometryUtils.ensureCCW(arg0)

    @staticmethod
    @overload
    def barycoordInsideTriangle(arg0: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.barycoordInsideTriangle(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(__GeometryUtils.barycoordInsideTriangle(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,float,float,float)"""
        return float.__wrap(__GeometryUtils.fromBarycoord(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def colinear(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.colinear(float,float,float,float,float,float)"""
        return bool.__wrap(__GeometryUtils.colinear(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def isClockwise(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isClockwise(float[],int,int)"""
        return bool.__wrap(__GeometryUtils.isClockwise(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[])"""
        __GeometryUtils.ensureClockwise(arg0)

    @staticmethod
    @overload
    def lowestPositiveRoot(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.lowestPositiveRoot(float,float,float)"""
        return float.__wrap(__GeometryUtils.lowestPositiveRoot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def triangleCircumcenter(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCircumcenter(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.triangleCircumcenter(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[],int,int)"""
        __GeometryUtils.ensureClockwise(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def quadrilateralCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.quadrilateralCentroid(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.quadrilateralCentroid(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), arg8))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[],int,int)"""
        __GeometryUtils.ensureCCW(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def isCCW(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isCCW(float[],int,int)"""
        return bool.__wrap(__GeometryUtils.isCCW(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def triangleCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCentroid(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.triangleCentroid(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.fromBarycoord(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def reverseVertices(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.reverseVertices(float[],int,int)"""
        __GeometryUtils.reverseVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def triangleCircumradius(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleCircumradius(float,float,float,float,float,float)"""
        return float.__wrap(__GeometryUtils.triangleCircumradius(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @staticmethod
    @overload
    def toBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.toBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2.__wrap(__GeometryUtils.toBarycoord(arg0, arg1, arg2, arg3, arg4)) 
 
 
# CLASS: com.badlogic.gdx.math.Matrix4
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Quaternion as __Quaternion
__Quaternion = __Quaternion
from typing import List
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
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
 
class Matrix4():
    """com.badlogic.gdx.math.Matrix4"""
 
    @staticmethod
    def __wrap(java_value: __Matrix4) -> 'Matrix4':
        return Matrix4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Matrix4):
        """
        Dynamic initializer for Matrix4.
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
    def setToProjection(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToProjection(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToProjection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        val = __Matrix4(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRotation(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Matrix4.getRotation(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'.__wrap(super(__Matrix4, self).getRotation(arg0))

    @overload
    def getRotation(self, arg0: 'Quaternion', arg1: bool) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Matrix4.getRotation(com.badlogic.gdx.math.Quaternion,boolean)"""
        return 'Quaternion'.__wrap(super(__Matrix4, self).getRotation(arg0, __boolean.valueOf(arg1)))

    @overload
    def mulLeft(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.mulLeft(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).mulLeft(arg0))

    @overload
    def __init__(self, arg0: 'Quaternion'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Quaternion)"""
        val = __Matrix4(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rotateRad(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotateRad(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTranslation(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setTranslation(arg0))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleY()"""
        return float.__wrap(super(Matrix4, self).getScaleY())

    @staticmethod
    @overload
    def rot(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.rot(float[],float[],int,int,int)"""
        __Matrix4.rot(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setToProjection(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToProjection(float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToProjection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def setAsAffine(self, arg0: 'Affine2') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setAsAffine(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setAsAffine(arg0))

    @overload
    def scl(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).scl(arg0))

    @overload
    def setAsAffine(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setAsAffine(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setAsAffine(arg0))

    @overload
    def trn(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.trn(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).trn(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleX()"""
        return float.__wrap(super(Matrix4, self).getScaleX())

    @overload
    def rotateTowardTarget(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateTowardTarget(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotateTowardTarget(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotate(arg0, __float.valueOf(arg1)))

    @overload
    def setToTranslation(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToTranslation(arg0))

    @overload
    def setToLookAt(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToLookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToLookAt(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Matrix4.toString()"""
        return str.__wrap(super(Matrix4, self).toString())

    @overload
    def setToTranslation(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslation(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToTranslation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def tra(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.tra()"""
        return 'Matrix4'.__wrap(super(Matrix4, self).tra())

    @overload
    def setTranslation(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setTranslation(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setTranslation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float,float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9)))

    @overload
    def avg(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4[])"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).avg(arg0))

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Matrix4.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Matrix4, self).getTranslation(arg0))

    @overload
    def set(self, arg0: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0))

    @overload
    def avg(self, arg0: 'Matrix4', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).avg(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def mulVec(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.mulVec(float[],float[],int,int,int)"""
        __Matrix4.mulVec(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def toNormalMatrix(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.toNormalMatrix()"""
        return 'Matrix4'.__wrap(super(Matrix4, self).toNormalMatrix())

    @overload
    def __init__(self, arg0: 'Matrix4'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Matrix4)"""
        val = __Matrix4(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setToOrtho2D(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho2D(float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToOrtho2D(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def getScale(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Matrix4.getScale(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Matrix4, self).getScale(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Matrix4.getValues()"""
        return List[float].__wrap(super(Matrix4, self).getValues())

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).mul(arg0))

    @overload
    def translate(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.translate(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).translate(arg0))

    @overload
    def cpy(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.cpy()"""
        return 'Matrix4'.__wrap(super(Matrix4, self).cpy())

    @overload
    def setToOrtho2D(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho2D(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToOrtho2D(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def rotateRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateRad(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotateRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def scl(self, arg0: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).scl(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Matrix3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0))

    @overload
    def rotate(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotate(arg0, arg1))

    @overload
    def lerp(self, arg0: 'Matrix4', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.lerp(com.badlogic.gdx.math.Matrix4,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Matrix4(float[])"""
        val = __Matrix4(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setToTranslationAndScaling(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslationAndScaling(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToTranslationAndScaling(arg0, arg1))

    @overload
    def inv(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.inv()"""
        return 'Matrix4'.__wrap(super(Matrix4, self).inv())

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotation(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0, arg1))

    @overload
    def setFromEulerAnglesRad(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setFromEulerAnglesRad(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setFromEulerAnglesRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def prj(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.prj(float[],float[])"""
        __Matrix4.prj(arg0, arg1)

    @overload
    def setToLookAt(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToLookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToLookAt(arg0, arg1, arg2))

    @overload
    def setToRotationRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotationRad(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotationRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.translate(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getScaleYSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleYSquared()"""
        return float.__wrap(super(Matrix4, self).getScaleYSquared())

    @overload
    def setToRotation(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getScaleZSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleZSquared()"""
        return float.__wrap(super(Matrix4, self).getScaleZSquared())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Matrix4()"""
        val = __Matrix4()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def prj(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.prj(float[],float[],int,int,int)"""
        __Matrix4.prj(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotation(arg0, arg1))

    @overload
    def idt(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.idt()"""
        return 'Matrix4'.__wrap(super(Matrix4, self).idt())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Matrix4()"""
        val = __Matrix4()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setToOrtho(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho(float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToOrtho(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def avg(self, arg0: 'Matrix4', arg1: 'float') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4[],float[])"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).avg(arg0, arg1))

    @overload
    def setToRotationRad(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotationRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotationRad(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def det(arg0: 'float') -> float:
        """public static float com.badlogic.gdx.math.Matrix4.det(float[])"""
        return float.__wrap(__Matrix4.det(arg0))

    @overload
    def set(self, arg0: 'float') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float[])"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0))

    @overload
    def rotateTowardDirection(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateTowardDirection(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotateTowardDirection(arg0, arg1))

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.det()"""
        return float.__wrap(super(Matrix4, self).det())

    @overload
    def rotate(self, arg0: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotate(arg0))

    @staticmethod
    @overload
    def mulVec(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.mulVec(float[],float[])"""
        __Matrix4.mulVec(arg0, arg1)

    @overload
    def setToScaling(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToScaling(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToScaling(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0, arg1, arg2))

    @overload
    def hasRotationOrScaling(self) -> bool:
        """public boolean com.badlogic.gdx.math.Matrix4.hasRotationOrScaling()"""
        return bool.__wrap(super(Matrix4, self).hasRotationOrScaling())

    @staticmethod
    @overload
    def rot(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.rot(float[],float[])"""
        __Matrix4.rot(arg0, arg1)

    @overload
    def setFromEulerAngles(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setFromEulerAngles(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setFromEulerAngles(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).scl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def setToTranslationAndScaling(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslationAndScaling(float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToTranslationAndScaling(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def setToRotation(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToRotation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def det3x3(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.det3x3()"""
        return float.__wrap(super(Matrix4, self).det3x3())

    @overload
    def setToScaling(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToScaling(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToScaling(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Affine2') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(arg0))

    @overload
    def setToWorld(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToWorld(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).setToWorld(arg0, arg1, arg2))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6)))

    @staticmethod
    @overload
    def mul(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.mul(float[],float[])"""
        __Matrix4.mul(arg0, arg1)

    @overload
    def getScaleZ(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleZ()"""
        return float.__wrap(super(Matrix4, self).getScaleZ())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def inv(arg0: 'float') -> bool:
        """public static boolean com.badlogic.gdx.math.Matrix4.inv(float[])"""
        return bool.__wrap(__Matrix4.inv(arg0))

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def extract4x3Matrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Matrix4.extract4x3Matrix(float[])"""
        super(__Matrix4, self).extract4x3Matrix(arg0)

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scale(float,float,float)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getScaleXSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleXSquared()"""
        return float.__wrap(super(Matrix4, self).getScaleXSquared())

    @overload
    def trn(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.trn(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'.__wrap(super(__Matrix4, self).trn(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.DelaunayTriangulator
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.math.DelaunayTriangulator as __DelaunayTriangulator
__DelaunayTriangulator = __DelaunayTriangulator
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.ShortArray as __ShortArray
__ShortArray = __ShortArray
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DelaunayTriangulator():
    """com.badlogic.gdx.math.DelaunayTriangulator"""
 
    @staticmethod
    def __wrap(java_value: __DelaunayTriangulator) -> 'DelaunayTriangulator':
        return DelaunayTriangulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DelaunayTriangulator):
        """
        Dynamic initializer for DelaunayTriangulator.
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

    @overload
    def computeTriangles(self, arg0: 'FloatArray', arg1: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(com.badlogic.gdx.utils.FloatArray,boolean)"""
        return 'utils.ShortArray'.__wrap(super(__DelaunayTriangulator, self).computeTriangles(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.DelaunayTriangulator()"""
        val = __DelaunayTriangulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.DelaunayTriangulator()"""
        val = __DelaunayTriangulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def trim(self, arg0: 'ShortArray', arg1: 'float', arg2: 'float', arg3: int, arg4: int):
        """public void com.badlogic.gdx.math.DelaunayTriangulator.trim(com.badlogic.gdx.utils.ShortArray,float[],float[],int,int)"""
        super(__DelaunayTriangulator, self).trim(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4))

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
    def computeTriangles(self, arg0: 'float', arg1: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(float[],boolean)"""
        return 'utils.ShortArray'.__wrap(super(__DelaunayTriangulator, self).computeTriangles(arg0, __boolean.valueOf(arg1)))

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
    def computeTriangles(self, arg0: 'float', arg1: int, arg2: int, arg3: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(float[],int,int,boolean)"""
        return 'utils.ShortArray'.__wrap(super(__DelaunayTriangulator, self).computeTriangles(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Ellipse
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Ellipse as __Ellipse
__Ellipse = __Ellipse
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
 
class Ellipse():
    """com.badlogic.gdx.math.Ellipse"""
 
    @staticmethod
    def __wrap(java_value: __Ellipse) -> 'Ellipse':
        return Ellipse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ellipse):
        """
        Dynamic initializer for Ellipse.
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
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = __Ellipse(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Ellipse(float,float,float,float)"""
        val = __Ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Ellipse()"""
        val = __Ellipse()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__Ellipse, self).set(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Ellipse()"""
        val = __Ellipse()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.contains(float,float)"""
        return bool.__wrap(super(__Ellipse, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def circumference(self) -> float:
        """public float com.badlogic.gdx.math.Ellipse.circumference()"""
        return float.__wrap(super(Ellipse, self).circumference())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setSize(float,float)"""
        return 'Ellipse'.__wrap(super(__Ellipse, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Ellipse.hashCode()"""
        return int.__wrap(super(Ellipse, self).hashCode())

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setPosition(float,float)"""
        return 'Ellipse'.__wrap(super(__Ellipse, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Ellipse'.__wrap(super(__Ellipse, self).setPosition(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Ellipse'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Ellipse)"""
        super(__Ellipse, self).set(arg0)

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Ellipse, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Ellipse'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Ellipse)"""
        val = __Ellipse(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.equals(java.lang.Object)"""
        return bool.__wrap(super(__Ellipse, self).equals(arg0))

    @overload
    def set(self, arg0: 'Circle'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Circle)"""
        super(__Ellipse, self).set(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Circle'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Circle)"""
        val = __Ellipse(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.math.Ellipse.set(float,float,float,float)"""
        super(__Ellipse, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Vector2,float,float)"""
        val = __Ellipse(arg0, __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Ellipse.area()"""
        return float.__wrap(super(Ellipse, self).area()) 
 
 
# CLASS: com.badlogic.gdx.math.GridPoint2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.GridPoint2 as __GridPoint2
__GridPoint2 = __GridPoint2
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
 
class GridPoint2():
    """com.badlogic.gdx.math.GridPoint2"""
 
    @staticmethod
    def __wrap(java_value: __GridPoint2) -> 'GridPoint2':
        return GridPoint2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GridPoint2):
        """
        Dynamic initializer for GridPoint2.
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
    def sub(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.sub(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).sub(arg0))

    @overload
    def __init__(self, arg0: 'GridPoint2'):
        """public com.badlogic.gdx.math.GridPoint2(com.badlogic.gdx.math.GridPoint2)"""
        val = __GridPoint2(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dst2(self, arg0: 'GridPoint2') -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst2(com.badlogic.gdx.math.GridPoint2)"""
        return float.__wrap(super(__GridPoint2, self).dst2(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.GridPoint2.equals(java.lang.Object)"""
        return bool.__wrap(super(__GridPoint2, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.set(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).set(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.add(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).add(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.GridPoint2.hashCode()"""
        return int.__wrap(super(GridPoint2, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.set(int,int)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.GridPoint2.toString()"""
        return str.__wrap(super(GridPoint2, self).toString())

    @overload
    def dst(self, arg0: 'GridPoint2') -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst(com.badlogic.gdx.math.GridPoint2)"""
        return float.__wrap(super(__GridPoint2, self).dst(arg0))

    @overload
    def sub(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.sub(int,int)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).sub(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.GridPoint2()"""
        val = __GridPoint2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.math.GridPoint2(int,int)"""
        val = __GridPoint2(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.add(int,int)"""
        return 'GridPoint2'.__wrap(super(__GridPoint2, self).add(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def cpy(self) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.cpy()"""
        return 'GridPoint2'.__wrap(super(GridPoint2, self).cpy())

    @overload
    def dst2(self, arg0: int, arg1: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst2(int,int)"""
        return float.__wrap(super(__GridPoint2, self).dst2(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.GridPoint2()"""
        val = __GridPoint2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dst(self, arg0: int, arg1: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst(int,int)"""
        return float.__wrap(super(__GridPoint2, self).dst(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.math.RandomXS128
from builtins import type
import com.badlogic.gdx.math.RandomXS128 as __RandomXS128
__RandomXS128 = __RandomXS128
import java.util.Random as __Random
__Random = __Random
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Class as __Class
__Class = __Class
import java.util.stream.LongStream as LongStream
import java.util.random.RandomGenerator as RandomGenerator
import java.util.stream.DoubleStream as DoubleStream
import java.util.stream.IntStream as IntStream
import java.lang.Double as __double
from builtins import bool
import java.util.random.RandomGenerator as __RandomGenerator
__RandomGenerator = __RandomGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.stream.DoubleStream as __DoubleStream
__DoubleStream = __DoubleStream
from builtins import float
import java.util.stream.LongStream as __LongStream
__LongStream = __LongStream
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.Random as Random
 
class RandomXS128():
    """com.badlogic.gdx.math.RandomXS128"""
 
    @staticmethod
    def __wrap(java_value: __RandomXS128) -> 'RandomXS128':
        return RandomXS128(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomXS128):
        """
        Dynamic initializer for RandomXS128.
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
    def nextDouble(self, arg0: float, arg1: float) -> float:
        """public default double java.util.random.RandomGenerator.nextDouble(double,double)"""
        return float.__wrap(super(__RandomGenerator, self).nextDouble(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def nextFloat(self, arg0: float) -> float:
        """public default float java.util.random.RandomGenerator.nextFloat(float)"""
        return float.__wrap(super(__RandomGenerator, self).nextFloat(__float.valueOf(arg0)))

    @override
    @overload
    def nextExponential(self) -> float:
        """public default double java.util.random.RandomGenerator.nextExponential()"""
        return float.__wrap(super(RandomGenerator, self).nextExponential())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.math.RandomXS128.nextDouble()"""
        return float.__wrap(super(RandomXS128, self).nextDouble())

    @staticmethod
    @overload
    def from(arg0: 'RandomGenerator') -> 'Random':
        """public static java.util.Random java.util.Random.from(java.util.random.RandomGenerator)"""
        return Random.__wrap(__Random.from(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def longs(self, arg0: int, arg1: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long,long)"""
        return 'LongStream'.__wrap(super(__Random, self).longs(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def nextDouble(self, arg0: float) -> float:
        """public default double java.util.random.RandomGenerator.nextDouble(double)"""
        return float.__wrap(super(__RandomGenerator, self).nextDouble(__double.valueOf(arg0)))

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.math.RandomXS128.nextInt()"""
        return int.__wrap(super(RandomXS128, self).nextInt())

    @override
    @overload
    def isDeprecated(self) -> bool:
        """public default boolean java.util.random.RandomGenerator.isDeprecated()"""
        return bool.__wrap(super(RandomGenerator, self).isDeprecated())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def doubles(self, arg0: int, arg1: float, arg2: float) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(long,double,double)"""
        return 'DoubleStream'.__wrap(super(__Random, self).doubles(__long.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def nextFloat(self, arg0: float, arg1: float) -> float:
        """public default float java.util.random.RandomGenerator.nextFloat(float,float)"""
        return float.__wrap(super(__RandomGenerator, self).nextFloat(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.RandomXS128(long)"""
        val = __RandomXS128(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.RandomXS128()"""
        val = __RandomXS128()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public default int java.util.random.RandomGenerator.nextInt(int,int)"""
        return int.__wrap(super(__RandomGenerator, self).nextInt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.badlogic.gdx.math.RandomXS128.nextBoolean()"""
        return bool.__wrap(super(RandomXS128, self).nextBoolean())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def ints(self, arg0: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(long)"""
        return 'IntStream'.__wrap(super(__Random, self).ints(__long.valueOf(arg0)))

    @override
    @overload
    def doubles(self) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles()"""
        return 'DoubleStream'.__wrap(super(Random, self).doubles())

    @override
    @overload
    def nextBytes(self, arg0: bytes):
        """public void com.badlogic.gdx.math.RandomXS128.nextBytes(byte[])"""
        super(__RandomXS128, self).nextBytes(bytes)

    @overload
    def setState(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.math.RandomXS128.setState(long,long)"""
        super(__RandomXS128, self).setState(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.RandomXS128()"""
        val = __RandomXS128()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def nextLong(self, arg0: int, arg1: int) -> int:
        """public default long java.util.random.RandomGenerator.nextLong(long,long)"""
        return int.__wrap(super(__RandomGenerator, self).nextLong(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def doubles(self, arg0: int) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(long)"""
        return 'DoubleStream'.__wrap(super(__Random, self).doubles(__long.valueOf(arg0)))

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void com.badlogic.gdx.math.RandomXS128.setSeed(long)"""
        super(__RandomXS128, self).setSeed(__long.valueOf(arg0))

    @overload
    def ints(self, arg0: int, arg1: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(int,int)"""
        return 'IntStream'.__wrap(super(__Random, self).ints(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(long,int,int)"""
        return 'IntStream'.__wrap(super(__Random, self).ints(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def longs(self) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs()"""
        return 'LongStream'.__wrap(super(Random, self).longs())

    @overload
    def nextLong(self, arg0: int) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.nextLong(long)"""
        return int.__wrap(super(__RandomXS128, self).nextLong(__long.valueOf(arg0)))

    @overload
    def nextGaussian(self, arg0: float, arg1: float) -> float:
        """public default double java.util.random.RandomGenerator.nextGaussian(double,double)"""
        return float.__wrap(super(__RandomGenerator, self).nextGaussian(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def getState(self, arg0: int) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.getState(int)"""
        return int.__wrap(super(__RandomXS128, self).getState(__int.valueOf(arg0)))

    @override
    @overload
    def nextGaussian(self) -> float:
        """public synchronized double java.util.Random.nextGaussian()"""
        return float.__wrap(super(Random, self).nextGaussian())

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int com.badlogic.gdx.math.RandomXS128.nextInt(int)"""
        return int.__wrap(super(__RandomXS128, self).nextInt(__int.valueOf(arg0)))

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.nextLong()"""
        return int.__wrap(super(RandomXS128, self).nextLong())

    @overload
    def doubles(self, arg0: float, arg1: float) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(double,double)"""
        return 'DoubleStream'.__wrap(super(__Random, self).doubles(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def ints(self) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints()"""
        return 'IntStream'.__wrap(super(Random, self).ints())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def longs(self, arg0: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long)"""
        return 'LongStream'.__wrap(super(__Random, self).longs(__long.valueOf(arg0)))

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.math.RandomXS128.nextFloat()"""
        return float.__wrap(super(RandomXS128, self).nextFloat())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.math.RandomXS128(long,long)"""
        val = __RandomXS128(__long.valueOf(arg0), __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long,long,long)"""
        return 'LongStream'.__wrap(super(__Random, self).longs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$SwingOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.Interpolation as __Interpolation_SwingOut
__SwingOut = __Interpolation_SwingOut.SwingOut
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SwingOut():
    """com.badlogic.gdx.math.Interpolation.SwingOut"""
 
    @staticmethod
    def __wrap(java_value: __SwingOut) -> 'SwingOut':
        return SwingOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SwingOut):
        """
        Dynamic initializer for SwingOut.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$SwingOut.apply(float)"""
        return float.__wrap(super(__SwingOut, self).apply(__float.valueOf(arg0)))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$SwingOut(float)"""
        val = __SwingOut(__float.valueOf(arg0))
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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Vector4
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector4 as __Vector4
__Vector4 = __Vector4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Vector4():
    """com.badlogic.gdx.math.Vector4"""
 
    @staticmethod
    def __wrap(java_value: __Vector4) -> 'Vector4':
        return Vector4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Vector4):
        """
        Dynamic initializer for Vector4.
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
    def __init__(self, arg0: 'Vector2', arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector2,float,float)"""
        val = __Vector4(arg0, __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector4.len()"""
        return float.__wrap(super(Vector4, self).len())

    @overload
    def dst2(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dst2(com.badlogic.gdx.math.Vector4)"""
        return float.__wrap(super(__Vector4, self).dst2(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isUnit()"""
        return bool.__wrap(super(Vector4, self).isUnit())

    @overload
    def isCollinear(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinear(com.badlogic.gdx.math.Vector4,float)"""
        return bool.__wrap(super(__Vector4, self).isCollinear(arg0, __float.valueOf(arg1)))

    @overload
    def sub(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'.__wrap(super(__Vector4, self).sub(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Vector4(float[])"""
        val = __Vector4(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector4()"""
        val = __Vector4()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector3', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).set(arg0, __float.valueOf(arg1)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(float,float,float,float)"""
        return bool.__wrap(super(__Vector4, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isUnit(float)"""
        return bool.__wrap(super(__Vector4, self).isUnit(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def hasOppositeDirection(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.hasOppositeDirection(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).hasOppositeDirection(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dot(float,float,float,float)"""
        return float.__wrap(super(__Vector4, self).dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def interpolate(self, arg0: 'Vector4', arg1: float, arg2: 'Interpolation') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.interpolate(com.badlogic.gdx.math.Vector4,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector4'.__wrap(super(__Vector4, self).interpolate(arg0, __float.valueOf(arg1), arg2))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isZero()"""
        return bool.__wrap(super(Vector4, self).isZero())

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector4.len2()"""
        return float.__wrap(super(Vector4, self).len2())

    @overload
    def __init__(self, arg0: 'Vector4'):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector4)"""
        val = __Vector4(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector3,float)"""
        val = __Vector4(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(float,float,float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(float,float,float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).sub(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def scl(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).scl(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(com.badlogic.gdx.math.Vector4,float)"""
        return bool.__wrap(super(__Vector4, self).epsilonEquals(arg0, __float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector4', arg1: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.mulAdd(com.badlogic.gdx.math.Vector4,com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'.__wrap(super(__Vector4, self).mulAdd(arg0, arg1))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isZero(float)"""
        return bool.__wrap(super(__Vector4, self).isZero(__float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isPerpendicular(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).isPerpendicular(arg0))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dot(float,float,float,float,float,float,float,float)"""
        return float.__wrap(__Vector4.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(float,float,float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).scl(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def cpy(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.cpy()"""
        return 'Vector4'.__wrap(super(Vector4, self).cpy())

    @overload
    def isOnLine(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isOnLine(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).isOnLine(arg0))

    @override
    @overload
    def setZero(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setZero()"""
        return 'Vector4'.__wrap(super(Vector4, self).setZero())

    @overload
    def fromString(self, arg0: str) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.fromString(java.lang.String)"""
        return 'Vector4'.__wrap(super(__Vector4, self).fromString(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinearOpposite(com.badlogic.gdx.math.Vector4,float)"""
        return bool.__wrap(super(__Vector4, self).isCollinearOpposite(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector4()"""
        val = __Vector4()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: 'float') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(float[])"""
        return 'Vector4'.__wrap(super(__Vector4, self).set(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isOnLine(com.badlogic.gdx.math.Vector4,float)"""
        return bool.__wrap(super(__Vector4, self).isOnLine(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def nor(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.nor()"""
        return 'Vector4'.__wrap(super(Vector4, self).nor())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dst2(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dst2(float,float,float,float)"""
        return float.__wrap(super(__Vector4, self).dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(float,float,float,float,float)"""
        return bool.__wrap(super(__Vector4, self).epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def limit(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.limit(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).limit(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dst(float,float,float,float,float,float,float,float)"""
        return float.__wrap(__Vector4.dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @overload
    def mulAdd(self, arg0: 'Vector4', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.mulAdd(com.badlogic.gdx.math.Vector4,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).mulAdd(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector4.toString()"""
        return str.__wrap(super(Vector4, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector4.hashCode()"""
        return int.__wrap(super(Vector4, self).hashCode())

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setToRandomDirection()"""
        return 'Vector4'.__wrap(super(Vector4, self).setToRandomDirection())

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.clamp(float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).clamp(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.equals(java.lang.Object)"""
        return bool.__wrap(super(__Vector4, self).equals(arg0))

    @overload
    def setLength2(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setLength2(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).setLength2(__float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'.__wrap(super(__Vector4, self).set(arg0))

    @overload
    def sub(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).sub(__float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).epsilonEquals(arg0))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.len(float,float,float,float)"""
        return float.__wrap(__Vector4.len(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def dot(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dot(com.badlogic.gdx.math.Vector4)"""
        return float.__wrap(super(__Vector4, self).dot(arg0))

    @overload
    def add(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).add(__float.valueOf(arg0)))

    @overload
    def dst(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dst(com.badlogic.gdx.math.Vector4)"""
        return float.__wrap(super(__Vector4, self).dst(arg0))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dst(float,float,float,float)"""
        return float.__wrap(super(__Vector4, self).dst(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def setLength(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setLength(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).setLength(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Vector4(float,float,float,float)"""
        val = __Vector4(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector2', arg1: float, arg2: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector2,float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).set(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'.__wrap(super(__Vector4, self).add(arg0))

    @overload
    def scl(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'.__wrap(super(__Vector4, self).scl(arg0))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dst2(float,float,float,float,float,float,float,float)"""
        return float.__wrap(__Vector4.dst2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.len2(float,float,float,float)"""
        return float.__wrap(__Vector4.len2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def limit2(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.limit2(float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).limit2(__float.valueOf(arg0)))

    @overload
    def idt(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.idt(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).idt(arg0))

    @overload
    def isPerpendicular(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isPerpendicular(com.badlogic.gdx.math.Vector4,float)"""
        return bool.__wrap(super(__Vector4, self).isPerpendicular(arg0, __float.valueOf(arg1)))

    @overload
    def hasSameDirection(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.hasSameDirection(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).hasSameDirection(arg0))

    @overload
    def lerp(self, arg0: 'Vector4', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.lerp(com.badlogic.gdx.math.Vector4,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(float,float,float,float)"""
        return 'Vector4'.__wrap(super(__Vector4, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinearOpposite(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).isCollinearOpposite(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinear(com.badlogic.gdx.math.Vector4)"""
        return bool.__wrap(super(__Vector4, self).isCollinear(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.BSpline
from builtins import str
import java.lang.Boolean as __boolean
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
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
import com.badlogic.gdx.math.BSpline as __BSpline
__BSpline = __BSpline
from builtins import int
 
class BSpline():
    """com.badlogic.gdx.math.BSpline"""
 
    @staticmethod
    def __wrap(java_value: __BSpline) -> 'BSpline':
        return BSpline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BSpline):
        """
        Dynamic initializer for BSpline.
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
    def nearest(self, arg0: 'Vector', arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.math.BSpline.nearest(T,int,int)"""
        return int.__wrap(super(__BSpline, self).nearest(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.valueAt(T,int,float)"""
        return 'Vector'.__wrap(super(__BSpline, self).valueAt(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T)"""
        return float.__wrap(super(__BSpline, self).approximate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic(T,int,float,T[],boolean,T)"""
        return Vector.__wrap(__BSpline.cubic(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: int, arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.calculate(T,float,T[],int,boolean,T)"""
        return Vector.__wrap(__BSpline.calculate(arg0, __float.valueOf(arg1), arg2, __int.valueOf(arg3), __boolean.valueOf(arg4), arg5))

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.BSpline.locate(T)"""
        return float.__wrap(super(__BSpline, self).locate(arg0))

    @overload
    def nearest(self, arg0: 'Vector') -> int:
        """public int com.badlogic.gdx.math.BSpline.nearest(T)"""
        return int.__wrap(super(__BSpline, self).nearest(arg0))

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic(T,float,T[],boolean,T)"""
        return Vector.__wrap(__BSpline.cubic(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic_derivative(T,float,T[],boolean,T)"""
        return Vector.__wrap(__BSpline.cubic_derivative(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3), arg4))

    @overload
    def __init__(self, arg0: 'Vector', arg1: int, arg2: bool):
        """public com.badlogic.gdx.math.BSpline(T[],int,boolean)"""
        val = __BSpline(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: int, arg5: bool, arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.calculate(T,int,float,T[],int,boolean,T)"""
        return Vector.__wrap(__BSpline.calculate(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __int.valueOf(arg4), __boolean.valueOf(arg5), arg6))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.BSpline()"""
        val = __BSpline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.derivativeAt(T,int,float)"""
        return 'Vector'.__wrap(super(__BSpline, self).derivativeAt(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic_derivative(T,int,float,T[],boolean,T)"""
        return Vector.__wrap(__BSpline.cubic_derivative(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __boolean.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: int, arg5: bool, arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.derivative(T,int,float,T[],int,boolean,T)"""
        return Vector.__wrap(__BSpline.derivative(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, __int.valueOf(arg4), __boolean.valueOf(arg5), arg6))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def approximate(self, arg0: 'Vector', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T,int,int)"""
        return float.__wrap(super(__BSpline, self).approximate(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.valueAt(T,float)"""
        return 'Vector'.__wrap(super(__BSpline, self).valueAt(arg0, __float.valueOf(arg1)))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.derivativeAt(T,float)"""
        return 'Vector'.__wrap(super(__BSpline, self).derivativeAt(arg0, __float.valueOf(arg1)))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T,int)"""
        return float.__wrap(super(__BSpline, self).approximate(arg0, __int.valueOf(arg1)))

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
        """public com.badlogic.gdx.math.BSpline()"""
        val = __BSpline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector', arg1: int, arg2: bool) -> 'BSpline':
        """public com.badlogic.gdx.math.BSpline com.badlogic.gdx.math.BSpline.set(T[],int,boolean)"""
        return 'BSpline'.__wrap(super(__BSpline, self).set(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: int, arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.derivative(T,float,T[],int,boolean,T)"""
        return Vector.__wrap(__BSpline.derivative(arg0, __float.valueOf(arg1), arg2, __int.valueOf(arg3), __boolean.valueOf(arg4), arg5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approxLength(int)"""
        return float.__wrap(super(__BSpline, self).approxLength(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Quaternion
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Quaternion as __Quaternion
__Quaternion = __Quaternion
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
 
class Quaternion():
    """com.badlogic.gdx.math.Quaternion"""
 
    @staticmethod
    def __wrap(java_value: __Quaternion) -> 'Quaternion':
        return Quaternion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Quaternion):
        """
        Dynamic initializer for Quaternion.
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
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.dot(float,float,float,float)"""
        return float.__wrap(super(__Quaternion, self).dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getAngleAroundRad(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAroundRad(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Quaternion, self).getAngleAroundRad(arg0))

    @overload
    def isIdentity(self) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.isIdentity()"""
        return bool.__wrap(super(Quaternion, self).isIdentity())

    @overload
    def setEulerAngles(self, arg0: float, arg1: float, arg2: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setEulerAngles(float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setEulerAngles(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Quaternion()"""
        val = __Quaternion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isIdentity(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.isIdentity(float)"""
        return bool.__wrap(super(__Quaternion, self).isIdentity(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Quaternion(com.badlogic.gdx.math.Vector3,float)"""
        val = __Quaternion(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def conjugate(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.conjugate()"""
        return 'Quaternion'.__wrap(super(Quaternion, self).conjugate())

    @overload
    def getYaw(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getYaw()"""
        return float.__wrap(super(Quaternion, self).getYaw())

    @overload
    def setFromMatrix(self, arg0: 'Matrix4') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(com.badlogic.gdx.math.Matrix4)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromMatrix(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).set(arg0))

    @overload
    def setFromAxis(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxis(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxis(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def nor(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.nor()"""
        return 'Quaternion'.__wrap(super(Quaternion, self).nor())

    @overload
    def set(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).set(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.len(float,float,float,float)"""
        return float.__wrap(__Quaternion.len(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def mul(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).mul(arg0))

    @overload
    def dot(self, arg0: 'Quaternion') -> float:
        """public float com.badlogic.gdx.math.Quaternion.dot(com.badlogic.gdx.math.Quaternion)"""
        return float.__wrap(super(__Quaternion, self).dot(arg0))

    @overload
    def __init__(self, arg0: 'Quaternion'):
        """public com.badlogic.gdx.math.Quaternion(com.badlogic.gdx.math.Quaternion)"""
        val = __Quaternion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).mul(__float.valueOf(arg0)))

    @overload
    def exp(self, arg0: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.exp(float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).exp(__float.valueOf(arg0)))

    @overload
    def setFromAxisRad(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxisRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxisRad(arg0, __float.valueOf(arg1)))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).mul(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def slerp(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion[])"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).slerp(arg0))

    @overload
    def cpy(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.cpy()"""
        return 'Quaternion'.__wrap(super(Quaternion, self).cpy())

    @overload
    def getGimbalPole(self) -> int:
        """public int com.badlogic.gdx.math.Quaternion.getGimbalPole()"""
        return int.__wrap(super(Quaternion, self).getGimbalPole())

    @overload
    def setFromCross(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromCross(float,float,float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromCross(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.equals(java.lang.Object)"""
        return bool.__wrap(super(__Quaternion, self).equals(arg0))

    @overload
    def setFromMatrix(self, arg0: 'Matrix3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(com.badlogic.gdx.math.Matrix3)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromMatrix(arg0))

    @overload
    def getAngleRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleRad()"""
        return float.__wrap(super(Quaternion, self).getAngleRad())

    @overload
    def setFromMatrix(self, arg0: bool, arg1: 'Matrix4') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(boolean,com.badlogic.gdx.math.Matrix4)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromMatrix(__boolean.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Quaternion.toString()"""
        return str.__wrap(super(Quaternion, self).toString())

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.len2(float,float,float,float)"""
        return float.__wrap(__Quaternion.len2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPitchRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getPitchRad()"""
        return float.__wrap(super(Quaternion, self).getPitchRad())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAngleAround(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAround(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Quaternion, self).getAngleAround(arg0))

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngle()"""
        return float.__wrap(super(Quaternion, self).getAngle())

    @overload
    def getSwingTwist(self, arg0: float, arg1: float, arg2: float, arg3: 'Quaternion', arg4: 'Quaternion'):
        """public void com.badlogic.gdx.math.Quaternion.getSwingTwist(float,float,float,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Quaternion)"""
        super(__Quaternion, self).getSwingTwist(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3, arg4)

    @overload
    def getSwingTwist(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Quaternion'):
        """public void com.badlogic.gdx.math.Quaternion.getSwingTwist(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Quaternion)"""
        super(__Quaternion, self).getSwingTwist(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Quaternion.hashCode()"""
        return int.__wrap(super(Quaternion, self).hashCode())

    @overload
    def slerp(self, arg0: 'Quaternion', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).slerp(arg0, __float.valueOf(arg1)))

    @overload
    def setEulerAnglesRad(self, arg0: float, arg1: float, arg2: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setEulerAnglesRad(float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setEulerAnglesRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def setFromMatrix(self, arg0: bool, arg1: 'Matrix3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(boolean,com.badlogic.gdx.math.Matrix3)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromMatrix(__boolean.valueOf(arg0), arg1))

    @overload
    def transform(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Quaternion.transform(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'.__wrap(super(__Quaternion, self).transform(arg0))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.dot(float,float,float,float,float,float,float,float)"""
        return float.__wrap(__Quaternion.dot(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7)))

    @overload
    def idt(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.idt()"""
        return 'Quaternion'.__wrap(super(Quaternion, self).idt())

    @overload
    def setFromAxis(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxis(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxis(arg0, __float.valueOf(arg1)))

    @overload
    def setFromAxisRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxisRad(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxisRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Quaternion()"""
        val = __Quaternion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.len2()"""
        return float.__wrap(super(Quaternion, self).len2())

    @overload
    def setFromAxes(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxes(float,float,float,float,float,float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxes(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @overload
    def slerp(self, arg0: 'Quaternion', arg1: 'float') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion[],float[])"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).slerp(arg0, arg1))

    @overload
    def getAxisAngle(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAxisAngle(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Quaternion, self).getAxisAngle(arg0))

    @overload
    def getAngleAroundRad(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAroundRad(float,float,float)"""
        return float.__wrap(super(__Quaternion, self).getAngleAroundRad(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getRollRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getRollRad()"""
        return float.__wrap(super(Quaternion, self).getRollRad())

    @overload
    def setFromAxes(self, arg0: bool, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxes(boolean,float,float,float,float,float,float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromAxes(__boolean.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9)))

    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.len()"""
        return float.__wrap(super(Quaternion, self).len())

    @overload
    def mulLeft(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mulLeft(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).mulLeft(arg0))

    @overload
    def mulLeft(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mulLeft(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).mulLeft(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def toMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Quaternion.toMatrix(float[])"""
        super(__Quaternion, self).toMatrix(arg0)

    @overload
    def getAngleAround(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAround(float,float,float)"""
        return float.__wrap(super(__Quaternion, self).getAngleAround(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getPitch()"""
        return float.__wrap(super(Quaternion, self).getPitch())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.add(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).add(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getRoll()"""
        return float.__wrap(super(Quaternion, self).getRoll())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Quaternion(float,float,float,float)"""
        val = __Quaternion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setFromCross(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromCross(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).setFromCross(arg0, arg1))

    @overload
    def getYawRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getYawRad()"""
        return float.__wrap(super(Quaternion, self).getYawRad())

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.add(float,float,float,float)"""
        return 'Quaternion'.__wrap(super(__Quaternion, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getAxisAngleRad(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAxisAngleRad(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Quaternion, self).getAxisAngleRad(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector$MinimumTranslationVector
from builtins import str
import java.lang.Long as __long
import com.badlogic.gdx.math.Intersector as __Intersector_MinimumTranslationVector
__MinimumTranslationVector = __Intersector_MinimumTranslationVector.MinimumTranslationVector
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MinimumTranslationVector():
    """com.badlogic.gdx.math.Intersector.MinimumTranslationVector"""
 
    @staticmethod
    def __wrap(java_value: __MinimumTranslationVector) -> 'MinimumTranslationVector':
        return MinimumTranslationVector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MinimumTranslationVector):
        """
        Dynamic initializer for MinimumTranslationVector.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Intersector$MinimumTranslationVector()"""
        val = __MinimumTranslationVector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Intersector$MinimumTranslationVector()"""
        val = __MinimumTranslationVector()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Polyline
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Polyline as __Polyline
__Polyline = __Polyline
from builtins import float
from typing import List
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
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
 
class Polyline():
    """com.badlogic.gdx.math.Polyline"""
 
    @staticmethod
    def __wrap(java_value: __Polyline) -> 'Polyline':
        return Polyline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Polyline):
        """
        Dynamic initializer for Polyline.
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
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.rotate(float)"""
        super(__Polyline, self).rotate(__float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaleX()"""
        return float.__wrap(super(Polyline, self).getScaleX())

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setScale(float,float)"""
        super(__Polyline, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getOriginX()"""
        return float.__wrap(super(Polyline, self).getOriginX())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateScaledLength(self):
        """public void com.badlogic.gdx.math.Polyline.calculateScaledLength()"""
        super(Polyline, self).calculateScaledLength()

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.scale(float)"""
        super(__Polyline, self).scale(__float.valueOf(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getRotation()"""
        return float.__wrap(super(Polyline, self).getRotation())

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
        """public com.badlogic.gdx.math.Polyline()"""
        val = __Polyline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setVertices(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Polyline.setVertices(float[])"""
        super(__Polyline, self).setVertices(arg0)

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaleY()"""
        return float.__wrap(super(Polyline, self).getScaleY())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getY()"""
        return float.__wrap(super(Polyline, self).getY())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def calculateLength(self):
        """public void com.badlogic.gdx.math.Polyline.calculateLength()"""
        super(Polyline, self).calculateLength()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Polyline(float[])"""
        val = __Polyline(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getOriginY()"""
        return float.__wrap(super(Polyline, self).getOriginY())

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Polyline.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__Polyline, self).contains(arg0))

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getLength()"""
        return float.__wrap(super(Polyline, self).getLength())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.translate(float,float)"""
        super(__Polyline, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Polyline()"""
        val = __Polyline()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Polyline.contains(float,float)"""
        return bool.__wrap(super(__Polyline, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setOrigin(float,float)"""
        super(__Polyline, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setPosition(float,float)"""
        super(__Polyline, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def dirty(self):
        """public void com.badlogic.gdx.math.Polyline.dirty()"""
        super(Polyline, self).dirty()

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getX()"""
        return float.__wrap(super(Polyline, self).getX())

    @overload
    def getScaledLength(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaledLength()"""
        return float.__wrap(super(Polyline, self).getScaledLength())

    @overload
    def getTransformedVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polyline.getTransformedVertices()"""
        return List[float].__wrap(super(Polyline, self).getTransformedVertices())

    @overload
    def getBoundingRectangle(self) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Polyline.getBoundingRectangle()"""
        return 'Rectangle'.__wrap(super(Polyline, self).getBoundingRectangle())

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.setRotation(float)"""
        super(__Polyline, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polyline.getVertices()"""
        return List[float].__wrap(super(Polyline, self).getVertices()) 
 
 
# CLASS: com.badlogic.gdx.math.Frustum
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Frustum as __Frustum
__Frustum = __Frustum
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

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
 
class Frustum():
    """com.badlogic.gdx.math.Frustum"""
 
    @staticmethod
    def __wrap(java_value: __Frustum) -> 'Frustum':
        return Frustum(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Frustum):
        """
        Dynamic initializer for Frustum.
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
    def pointInFrustum(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.pointInFrustum(float,float,float)"""
        return bool.__wrap(super(__Frustum, self).pointInFrustum(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def update(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.Frustum.update(com.badlogic.gdx.math.Matrix4)"""
        super(__Frustum, self).update(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def sphereInFrustumWithoutNearFar(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustumWithoutNearFar(float,float,float,float)"""
        return bool.__wrap(super(__Frustum, self).sphereInFrustumWithoutNearFar(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Frustum()"""
        val = __Frustum()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def boundsInFrustum(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__Frustum, self).boundsInFrustum(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def sphereInFrustumWithoutNearFar(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustumWithoutNearFar(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Frustum, self).sphereInFrustumWithoutNearFar(arg0, __float.valueOf(arg1)))

    @overload
    def boundsInFrustum(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(float,float,float,float,float,float)"""
        return bool.__wrap(super(__Frustum, self).boundsInFrustum(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

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
    def boundsInFrustum(self, arg0: 'Vector3', arg1: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Frustum, self).boundsInFrustum(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def sphereInFrustum(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustum(com.badlogic.gdx.math.Vector3,float)"""
        return bool.__wrap(super(__Frustum, self).sphereInFrustum(arg0, __float.valueOf(arg1)))

    @overload
    def sphereInFrustum(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustum(float,float,float,float)"""
        return bool.__wrap(super(__Frustum, self).sphereInFrustum(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def boundsInFrustum(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(super(__Frustum, self).boundsInFrustum(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Frustum()"""
        val = __Frustum()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pointInFrustum(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.pointInFrustum(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__Frustum, self).pointInFrustum(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Bresenham2
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Bresenham2 as __Bresenham2
__Bresenham2 = __Bresenham2
from builtins import bool
from builtins import int
 
class Bresenham2():
    """com.badlogic.gdx.math.Bresenham2"""
 
    @staticmethod
    def __wrap(java_value: __Bresenham2) -> 'Bresenham2':
        return Bresenham2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bresenham2):
        """
        Dynamic initializer for Bresenham2.
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
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(int,int,int,int)"""
        return 'utils.Array'.__wrap(super(__Bresenham2, self).line(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Bresenham2()"""
        val = __Bresenham2()
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
    def __init__(self):
        """public com.badlogic.gdx.math.Bresenham2()"""
        val = __Bresenham2()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Pool', arg5: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(int,int,int,int,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.math.GridPoint2>,com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2>)"""
        return 'utils.Array'.__wrap(super(__Bresenham2, self).line(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5))

    @overload
    def line(self, arg0: 'GridPoint2', arg1: 'GridPoint2') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(com.badlogic.gdx.math.GridPoint2,com.badlogic.gdx.math.GridPoint2)"""
        return 'utils.Array'.__wrap(super(__Bresenham2, self).line(arg0, arg1)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$BounceIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.math.Interpolation as __Interpolation_BounceIn
__BounceIn = __Interpolation_BounceIn.BounceIn
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BounceIn():
    """com.badlogic.gdx.math.Interpolation.BounceIn"""
 
    @staticmethod
    def __wrap(java_value: __BounceIn) -> 'BounceIn':
        return BounceIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BounceIn):
        """
        Dynamic initializer for BounceIn.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$BounceIn(int)"""
        val = __BounceIn(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$BounceIn(float[],float[])"""
        val = __BounceIn(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$BounceIn.apply(float)"""
        return float.__wrap(super(__BounceIn, self).apply(__float.valueOf(arg0)))

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.MathUtils
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
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.MathUtils as __MathUtils
__MathUtils = __MathUtils
from builtins import int
 
class MathUtils():
    """com.badlogic.gdx.math.MathUtils"""
 
    @staticmethod
    def __wrap(java_value: __MathUtils) -> 'MathUtils':
        return MathUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MathUtils):
        """
        Dynamic initializer for MathUtils.
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
    def isEqual(arg0: float, arg1: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isEqual(float,float)"""
        return bool.__wrap(__MathUtils.isEqual(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.clamp(int,int,int)"""
        return int.__wrap(__MathUtils.clamp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def round(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.round(float)"""
        return int.__wrap(__MathUtils.round(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def log(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.log(float,float)"""
        return float.__wrap(__MathUtils.log(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def tanDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.tanDeg(float)"""
        return float.__wrap(__MathUtils.tanDeg(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random(float)"""
        return float.__wrap(__MathUtils.random(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerp(float,float,float)"""
        return float.__wrap(__MathUtils.lerp(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def sinDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.sinDeg(float)"""
        return float.__wrap(__MathUtils.sinDeg(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def ceilPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.ceilPositive(float)"""
        return int.__wrap(__MathUtils.ceilPositive(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.clamp(long,long,long)"""
        return int.__wrap(__MathUtils.clamp(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.clamp(float,float,float)"""
        return float.__wrap(__MathUtils.clamp(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isPowerOfTwo(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isPowerOfTwo(int)"""
        return bool.__wrap(__MathUtils.isPowerOfTwo(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def randomTriangular(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float)"""
        return float.__wrap(__MathUtils.randomTriangular(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def lerpAngleDeg(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerpAngleDeg(float,float,float)"""
        return float.__wrap(__MathUtils.lerpAngleDeg(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def acos(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.acos(float)"""
        return float.__wrap(__MathUtils.acos(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def isZero(arg0: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isZero(float)"""
        return bool.__wrap(__MathUtils.isZero(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2(float,float)"""
        return float.__wrap(__MathUtils.atan2(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def random(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random(float,float)"""
        return float.__wrap(__MathUtils.random(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def nextPowerOfTwo(arg0: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.nextPowerOfTwo(int)"""
        return int.__wrap(__MathUtils.nextPowerOfTwo(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def atanDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atanDeg(float)"""
        return float.__wrap(__MathUtils.atanDeg(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def lerpAngle(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerpAngle(float,float,float)"""
        return float.__wrap(__MathUtils.lerpAngle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def tan(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.tan(float)"""
        return float.__wrap(__MathUtils.tan(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def acosDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.acosDeg(float)"""
        return float.__wrap(__MathUtils.acosDeg(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def sin(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.sin(float)"""
        return float.__wrap(__MathUtils.sin(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.random(long,long)"""
        return int.__wrap(__MathUtils.random(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def randomBoolean() -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.randomBoolean()"""
        return bool.__wrap(__MathUtils.randomBoolean())

    @staticmethod
    @overload
    def randomTriangular(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float,float,float)"""
        return float.__wrap(__MathUtils.randomTriangular(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def atan(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan(float)"""
        return float.__wrap(__MathUtils.atan(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def isEqual(arg0: float, arg1: float, arg2: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isEqual(float,float,float)"""
        return bool.__wrap(__MathUtils.isEqual(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def cosDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.cosDeg(float)"""
        return float.__wrap(__MathUtils.cosDeg(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def floor(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.floor(float)"""
        return int.__wrap(__MathUtils.floor(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def ceil(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.ceil(float)"""
        return int.__wrap(__MathUtils.ceil(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def floorPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.floorPositive(float)"""
        return int.__wrap(__MathUtils.floorPositive(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random() -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random()"""
        return float.__wrap(__MathUtils.random())

    @staticmethod
    @overload
    def randomSign() -> int:
        """public static int com.badlogic.gdx.math.MathUtils.randomSign()"""
        return int.__wrap(__MathUtils.randomSign())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def asin(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.asin(float)"""
        return float.__wrap(__MathUtils.asin(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static short com.badlogic.gdx.math.MathUtils.clamp(short,short,short)"""
        return int.__wrap(__MathUtils.clamp(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @staticmethod
    @overload
    def randomTriangular() -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular()"""
        return float.__wrap(__MathUtils.randomTriangular())

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double com.badlogic.gdx.math.MathUtils.clamp(double,double,double)"""
        return float.__wrap(__MathUtils.clamp(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def log2(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.log2(float)"""
        return float.__wrap(__MathUtils.log2(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.random(int,int)"""
        return int.__wrap(__MathUtils.random(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def atan2Deg360(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2Deg360(float,float)"""
        return float.__wrap(__MathUtils.atan2Deg360(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def randomTriangular(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float,float)"""
        return float.__wrap(__MathUtils.randomTriangular(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def randomBoolean(arg0: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.randomBoolean(float)"""
        return bool.__wrap(__MathUtils.randomBoolean(__float.valueOf(arg0)))

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
    def atanUnchecked(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atanUnchecked(double)"""
        return float.__wrap(__MathUtils.atanUnchecked(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def isZero(arg0: float, arg1: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isZero(float,float)"""
        return bool.__wrap(__MathUtils.isZero(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def cos(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.cos(float)"""
        return float.__wrap(__MathUtils.cos(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.random(long)"""
        return int.__wrap(__MathUtils.random(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def atanUncheckedDeg(arg0: float) -> float:
        """public static double com.badlogic.gdx.math.MathUtils.atanUncheckedDeg(double)"""
        return float.__wrap(__MathUtils.atanUncheckedDeg(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2Deg(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2Deg(float,float)"""
        return float.__wrap(__MathUtils.atan2Deg(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def norm(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.norm(float,float,float)"""
        return float.__wrap(__MathUtils.norm(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def asinDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.asinDeg(float)"""
        return float.__wrap(__MathUtils.asinDeg(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def map(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.map(float,float,float,float,float)"""
        return float.__wrap(__MathUtils.map(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def roundPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.roundPositive(float)"""
        return int.__wrap(__MathUtils.roundPositive(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.random(int)"""
        return int.__wrap(__MathUtils.random(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$BounceOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_BounceOut
__BounceOut = __Interpolation_BounceOut.BounceOut
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
 
class BounceOut():
    """com.badlogic.gdx.math.Interpolation.BounceOut"""
 
    @staticmethod
    def __wrap(java_value: __BounceOut) -> 'BounceOut':
        return BounceOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BounceOut):
        """
        Dynamic initializer for BounceOut.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$BounceOut(int)"""
        val = __BounceOut(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$BounceOut(float[],float[])"""
        val = __BounceOut(arg0, arg1)
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$BounceOut.apply(float)"""
        return float.__wrap(super(__BounceOut, self).apply(__float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ElasticIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_ElasticIn
__ElasticIn = __Interpolation_ElasticIn.ElasticIn
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
 
class ElasticIn():
    """com.badlogic.gdx.math.Interpolation.ElasticIn"""
 
    @staticmethod
    def __wrap(java_value: __ElasticIn) -> 'ElasticIn':
        return ElasticIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ElasticIn):
        """
        Dynamic initializer for ElasticIn.
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

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$ElasticIn(float,float,int,float)"""
        val = __ElasticIn(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ElasticIn.apply(float)"""
        return float.__wrap(super(__ElasticIn, self).apply(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Shape2D
import com.badlogic.gdx.math.Shape2D as __Shape2D
__Shape2D = __Shape2D
from abc import abstractmethod, ABC
 
class Shape2D(ABC):
    """com.badlogic.gdx.math.Shape2D"""
 
    @staticmethod
    def __wrap(java_value: __Shape2D) -> 'Shape2D':
        return Shape2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shape2D):
        """
        Dynamic initializer for Shape2D.
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
    def contains(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.math.Shape2D.contains(float,float)"""
        pass

    @abstractmethod
    def contains(self, arg0: 'Vector2'):
        """public abstract boolean com.badlogic.gdx.math.Shape2D.contains(com.badlogic.gdx.math.Vector2)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$PowIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Interpolation as __Interpolation_PowIn
__PowIn = __Interpolation_PowIn.PowIn
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
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
 
class PowIn():
    """com.badlogic.gdx.math.Interpolation.PowIn"""
 
    @staticmethod
    def __wrap(java_value: __PowIn) -> 'PowIn':
        return PowIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PowIn):
        """
        Dynamic initializer for PowIn.
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$PowIn.apply(float)"""
        return float.__wrap(super(__PowIn, self).apply(__float.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$PowIn(int)"""
        val = __PowIn(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Swing
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.math.Interpolation as __Interpolation_Swing
__Swing = __Interpolation_Swing.Swing
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
 
class Swing():
    """com.badlogic.gdx.math.Interpolation.Swing"""
 
    @staticmethod
    def __wrap(java_value: __Swing) -> 'Swing':
        return Swing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Swing):
        """
        Dynamic initializer for Swing.
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

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Swing.apply(float)"""
        return float.__wrap(super(__Swing, self).apply(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$Swing(float)"""
        val = __Swing(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float.__wrap(super(__Interpolation, self).apply(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))