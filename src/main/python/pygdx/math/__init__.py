from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.GeometryUtils as _GeometryUtils
_GeometryUtils = _GeometryUtils
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GeometryUtils():
    """com.badlogic.gdx.math.GeometryUtils"""
 
    @staticmethod
    def _wrap(java_value: _GeometryUtils) -> 'GeometryUtils':
        return GeometryUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GeometryUtils):
        """
        Dynamic initializer for GeometryUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GeometryUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GeometryUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lowestPositiveRoot(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.lowestPositiveRoot(float,float,float)"""
        return float._wrap(_GeometryUtils.lowestPositiveRoot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[])"""
        _GeometryUtils.ensureClockwise(arg0)

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.fromBarycoord(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[])"""
        _GeometryUtils.ensureCCW(arg0)

    @staticmethod
    @overload
    def barycoordInsideTriangle(arg0: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.barycoordInsideTriangle(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_GeometryUtils.barycoordInsideTriangle(arg0))

    @staticmethod
    @overload
    def isCCW(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isCCW(float[],int,int)"""
        return bool._wrap(_GeometryUtils.isCCW(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def triangleArea(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleArea(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleArea(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[],int,int)"""
        _GeometryUtils.ensureCCW(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,float,float,float)"""
        return float._wrap(_GeometryUtils.fromBarycoord(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def triangleQuality(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleQuality(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleQuality(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def triangleCircumcenter(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCircumcenter(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.triangleCircumcenter(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def triangleCircumradius(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleCircumradius(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleCircumradius(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def reverseVertices(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.reverseVertices(float[],int,int)"""
        _GeometryUtils.reverseVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def quadrilateralCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.quadrilateralCentroid(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.quadrilateralCentroid(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), arg8))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[],int,int)"""
        _GeometryUtils.ensureClockwise(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def polygonArea(arg0: 'float', arg1: int, arg2: int) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.polygonArea(float[],int,int)"""
        return float._wrap(_GeometryUtils.polygonArea(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def colinear(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.colinear(float,float,float,float,float,float)"""
        return bool._wrap(_GeometryUtils.colinear(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def polygonCentroid(arg0: 'float', arg1: int, arg2: int, arg3: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.polygonCentroid(float[],int,int,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.polygonCentroid(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def triangleCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCentroid(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.triangleCentroid(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.toBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.toBarycoord(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isClockwise(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isClockwise(float[],int,int)"""
        return bool._wrap(_GeometryUtils.isClockwise(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.math.GeometryUtils
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.GeometryUtils as _GeometryUtils
_GeometryUtils = _GeometryUtils
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GeometryUtils():
    """com.badlogic.gdx.math.GeometryUtils"""
 
    @staticmethod
    def _wrap(java_value: _GeometryUtils) -> 'GeometryUtils':
        return GeometryUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GeometryUtils):
        """
        Dynamic initializer for GeometryUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GeometryUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GeometryUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lowestPositiveRoot(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.lowestPositiveRoot(float,float,float)"""
        return float._wrap(_GeometryUtils.lowestPositiveRoot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[])"""
        _GeometryUtils.ensureClockwise(arg0)

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.fromBarycoord(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float'):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[])"""
        _GeometryUtils.ensureCCW(arg0)

    @staticmethod
    @overload
    def barycoordInsideTriangle(arg0: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.barycoordInsideTriangle(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_GeometryUtils.barycoordInsideTriangle(arg0))

    @staticmethod
    @overload
    def isCCW(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isCCW(float[],int,int)"""
        return bool._wrap(_GeometryUtils.isCCW(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def triangleArea(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleArea(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleArea(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ensureCCW(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureCCW(float[],int,int)"""
        _GeometryUtils.ensureCCW(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def fromBarycoord(arg0: 'Vector2', arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.fromBarycoord(com.badlogic.gdx.math.Vector2,float,float,float)"""
        return float._wrap(_GeometryUtils.fromBarycoord(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def triangleQuality(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleQuality(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleQuality(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def triangleCircumcenter(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCircumcenter(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.triangleCircumcenter(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def triangleCircumradius(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.triangleCircumradius(float,float,float,float,float,float)"""
        return float._wrap(_GeometryUtils.triangleCircumradius(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def reverseVertices(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.reverseVertices(float[],int,int)"""
        _GeometryUtils.reverseVertices(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def quadrilateralCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.quadrilateralCentroid(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.quadrilateralCentroid(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), arg8))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def ensureClockwise(arg0: 'float', arg1: int, arg2: int):
        """public static void com.badlogic.gdx.math.GeometryUtils.ensureClockwise(float[],int,int)"""
        _GeometryUtils.ensureClockwise(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def polygonArea(arg0: 'float', arg1: int, arg2: int) -> float:
        """public static float com.badlogic.gdx.math.GeometryUtils.polygonArea(float[],int,int)"""
        return float._wrap(_GeometryUtils.polygonArea(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def colinear(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.colinear(float,float,float,float,float,float)"""
        return bool._wrap(_GeometryUtils.colinear(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def polygonCentroid(arg0: 'float', arg1: int, arg2: int, arg3: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.polygonCentroid(float[],int,int,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.polygonCentroid(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def triangleCentroid(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.triangleCentroid(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.triangleCentroid(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toBarycoord(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.GeometryUtils.toBarycoord(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_GeometryUtils.toBarycoord(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isClockwise(arg0: 'float', arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.math.GeometryUtils.isClockwise(float[],int,int)"""
        return bool._wrap(_GeometryUtils.isClockwise(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.math.GeometryUtils 
 
 
# CLASS: com.badlogic.gdx.math.Circle
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
import com.badlogic.gdx.math.Circle as _Circle
_Circle = _Circle
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Circle():
    """com.badlogic.gdx.math.Circle"""
 
    @staticmethod
    def _wrap(java_value: _Circle) -> 'Circle':
        return Circle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Circle):
        """
        Dynamic initializer for Circle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Circle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Circle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Circle.equals(java.lang.Object)"""
        return bool._wrap(super(_Circle, self).equals(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.math.Circle.set(float,float,float)"""
        super(_Circle, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setX(float)"""
        super(_Circle, self).setX(_float.valueOf(arg0))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Circle.area()"""
        return float._wrap(super(Circle, self).area())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Circle.setPosition(float,float)"""
        super(_Circle, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def overlaps(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.overlaps(com.badlogic.gdx.math.Circle)"""
        return bool._wrap(super(_Circle, self).overlaps(arg0))

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_Circle, self).set(arg0, arg1)

    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.math.Circle.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_Circle, self).setPosition(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(float,float)"""
        return bool._wrap(super(_Circle, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Circle'):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Circle)"""
        super(_Circle, self).set(arg0)

    @overload
    def __init__(self, arg0: 'Circle'):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Circle)"""
        val = _Circle(arg0)
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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Circle(float,float,float)"""
        val = _Circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Circle, self).contains(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setY(float)"""
        super(_Circle, self).setY(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Vector2,float)"""
        val = _Circle(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def circumference(self) -> float:
        """public float com.badlogic.gdx.math.Circle.circumference()"""
        return float._wrap(super(Circle, self).circumference())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Circle.hashCode()"""
        return int._wrap(super(Circle, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Circle.toString()"""
        return str._wrap(super(Circle, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Circle()"""
        val = _Circle()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector2', arg1: float):
        """public void com.badlogic.gdx.math.Circle.set(com.badlogic.gdx.math.Vector2,float)"""
        super(_Circle, self).set(arg0, _float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.math.Circle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = _Circle(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.math.Circle.setRadius(float)"""
        super(_Circle, self).setRadius(_float.valueOf(arg0))

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Circle.contains(com.badlogic.gdx.math.Circle)"""
        return bool._wrap(super(_Circle, self).contains(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Circle()"""
        val = _Circle()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.EarClippingTriangulator
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.EarClippingTriangulator as _EarClippingTriangulator
_EarClippingTriangulator = _EarClippingTriangulator
import java.lang.Integer as _int
import com.badlogic.gdx.utils.ShortArray as _ShortArray
_ShortArray = _ShortArray
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EarClippingTriangulator():
    """com.badlogic.gdx.math.EarClippingTriangulator"""
 
    @staticmethod
    def _wrap(java_value: _EarClippingTriangulator) -> 'EarClippingTriangulator':
        return EarClippingTriangulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EarClippingTriangulator):
        """
        Dynamic initializer for EarClippingTriangulator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EarClippingTriangulator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EarClippingTriangulator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def computeTriangles(self, arg0: 'float') -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(float[])"""
        return 'utils.ShortArray'._wrap(super(_EarClippingTriangulator, self).computeTriangles(arg0))

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
    def computeTriangles(self, arg0: 'float', arg1: int, arg2: int) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(float[],int,int)"""
        return 'utils.ShortArray'._wrap(super(_EarClippingTriangulator, self).computeTriangles(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.EarClippingTriangulator()"""
        val = _EarClippingTriangulator()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def computeTriangles(self, arg0: 'FloatArray') -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.EarClippingTriangulator.computeTriangles(com.badlogic.gdx.utils.FloatArray)"""
        return 'utils.ShortArray'._wrap(super(_EarClippingTriangulator, self).computeTriangles(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.math.EarClippingTriangulator()"""
        val = _EarClippingTriangulator()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.ConvexHull
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.math.ConvexHull as _ConvexHull
_ConvexHull = _ConvexHull
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.utils.FloatArray as _FloatArray
_FloatArray = _FloatArray
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.IntArray as _IntArray
_IntArray = _IntArray
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConvexHull():
    """com.badlogic.gdx.math.ConvexHull"""
 
    @staticmethod
    def _wrap(java_value: _ConvexHull) -> 'ConvexHull':
        return ConvexHull(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConvexHull):
        """
        Dynamic initializer for ConvexHull.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConvexHull__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConvexHull__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def computeIndices(self, arg0: 'float', arg1: int, arg2: int, arg3: bool, arg4: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(float[],int,int,boolean,boolean)"""
        return 'utils.IntArray'._wrap(super(_ConvexHull, self).computeIndices(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def computePolygon(self, arg0: 'FloatArray', arg1: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(com.badlogic.gdx.utils.FloatArray,boolean)"""
        return 'utils.FloatArray'._wrap(super(_ConvexHull, self).computePolygon(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.ConvexHull()"""
        val = _ConvexHull()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def computePolygon(self, arg0: 'float', arg1: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(float[],boolean)"""
        return 'utils.FloatArray'._wrap(super(_ConvexHull, self).computePolygon(arg0, _boolean.valueOf(arg1)))

    @overload
    def computeIndices(self, arg0: 'FloatArray', arg1: bool, arg2: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(com.badlogic.gdx.utils.FloatArray,boolean,boolean)"""
        return 'utils.IntArray'._wrap(super(_ConvexHull, self).computeIndices(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

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
    def computeIndices(self, arg0: 'float', arg1: bool, arg2: bool) -> 'utils.IntArray':
        """public com.badlogic.gdx.utils.IntArray com.badlogic.gdx.math.ConvexHull.computeIndices(float[],boolean,boolean)"""
        return 'utils.IntArray'._wrap(super(_ConvexHull, self).computeIndices(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def computePolygon(self, arg0: 'float', arg1: int, arg2: int, arg3: bool) -> 'utils.FloatArray':
        """public com.badlogic.gdx.utils.FloatArray com.badlogic.gdx.math.ConvexHull.computePolygon(float[],int,int,boolean)"""
        return 'utils.FloatArray'._wrap(super(_ConvexHull, self).computePolygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.ConvexHull()"""
        val = _ConvexHull()
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
 
 
# CLASS: com.badlogic.gdx.math.Vector4
import com.badlogic.gdx.math.Vector4 as _Vector4
_Vector4 = _Vector4
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vector4():
    """com.badlogic.gdx.math.Vector4"""
 
    @staticmethod
    def _wrap(java_value: _Vector4) -> 'Vector4':
        return Vector4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector4):
        """
        Dynamic initializer for Vector4.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector4__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector4__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isZero(float)"""
        return bool._wrap(super(_Vector4, self).isZero(_float.valueOf(arg0)))

    @overload
    def isPerpendicular(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isPerpendicular(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).isPerpendicular(arg0))

    @overload
    def limit2(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.limit2(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).limit2(_float.valueOf(arg0)))

    @overload
    def add(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).add(_float.valueOf(arg0)))

    @overload
    def setLength(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setLength(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).setLength(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).scl(_float.valueOf(arg0)))

    @overload
    def dst2(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dst2(float,float,float,float)"""
        return float._wrap(super(_Vector4, self).dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.equals(java.lang.Object)"""
        return bool._wrap(super(_Vector4, self).equals(arg0))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector4.len2()"""
        return float._wrap(super(Vector4, self).len2())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isOnLine(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isOnLine(com.badlogic.gdx.math.Vector4,float)"""
        return bool._wrap(super(_Vector4, self).isOnLine(arg0, _float.valueOf(arg1)))

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
    def hasSameDirection(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.hasSameDirection(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).hasSameDirection(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).set(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dot(com.badlogic.gdx.math.Vector4)"""
        return float._wrap(super(_Vector4, self).dot(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(com.badlogic.gdx.math.Vector4,float)"""
        return bool._wrap(super(_Vector4, self).epsilonEquals(arg0, _float.valueOf(arg1)))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dst(float,float,float,float)"""
        return float._wrap(super(_Vector4, self).dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'Vector4'):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector4)"""
        val = _Vector4(arg0)
        self.__wrapper = val

    @overload
    def epsilonEquals(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).epsilonEquals(arg0))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.clamp(float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).clamp(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mulAdd(self, arg0: 'Vector4', arg1: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.mulAdd(com.badlogic.gdx.math.Vector4,com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'._wrap(super(_Vector4, self).mulAdd(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector4.hashCode()"""
        return int._wrap(super(Vector4, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Vector4(float,float,float,float)"""
        val = _Vector4(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector4.toString()"""
        return str._wrap(super(Vector4, self).toString())

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(float,float,float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def isPerpendicular(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isPerpendicular(com.badlogic.gdx.math.Vector4,float)"""
        return bool._wrap(super(_Vector4, self).isPerpendicular(arg0, _float.valueOf(arg1)))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.hasOppositeDirection(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).hasOppositeDirection(arg0))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(float,float,float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).sub(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def fromString(self, arg0: str) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.fromString(java.lang.String)"""
        return 'Vector4'._wrap(super(_Vector4, self).fromString(arg0))

    @overload
    def interpolate(self, arg0: 'Vector4', arg1: float, arg2: 'Interpolation') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.interpolate(com.badlogic.gdx.math.Vector4,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector4'._wrap(super(_Vector4, self).interpolate(arg0, _float.valueOf(arg1), arg2))

    @overload
    def dst2(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dst2(com.badlogic.gdx.math.Vector4)"""
        return float._wrap(super(_Vector4, self).dst2(arg0))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(float,float,float,float,float)"""
        return bool._wrap(super(_Vector4, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.len2(float,float,float,float)"""
        return float._wrap(_Vector4.len2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def limit(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.limit(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).limit(_float.valueOf(arg0)))

    @overload
    def isCollinear(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinear(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).isCollinear(arg0))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector3,float)"""
        val = _Vector4(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dst(float,float,float,float,float,float,float,float)"""
        return float._wrap(_Vector4.dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinearOpposite(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).isCollinearOpposite(arg0))

    @overload
    def sub(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'._wrap(super(_Vector4, self).sub(arg0))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.len(float,float,float,float)"""
        return float._wrap(_Vector4.len(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Vector4.dot(float,float,float,float)"""
        return float._wrap(super(_Vector4, self).dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector4()"""
        val = _Vector4()
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.add(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'._wrap(super(_Vector4, self).add(arg0))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector4.len()"""
        return float._wrap(super(Vector4, self).len())

    @override
    @overload
    def cpy(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.cpy()"""
        return 'Vector4'._wrap(super(Vector4, self).cpy())

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(float,float,float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).scl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: 'Vector2', arg1: float, arg2: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector2,float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).set(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(float,float,float,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setLength2(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setLength2(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).setLength2(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dot(float,float,float,float,float,float,float,float)"""
        return float._wrap(_Vector4.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Vector4(com.badlogic.gdx.math.Vector2,float,float)"""
        val = _Vector4(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Vector4(float[])"""
        val = _Vector4(arg0)
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.sub(float)"""
        return 'Vector4'._wrap(super(_Vector4, self).sub(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.scl(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'._wrap(super(_Vector4, self).scl(arg0))

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static float com.badlogic.gdx.math.Vector4.dst2(float,float,float,float,float,float,float,float)"""
        return float._wrap(_Vector4.dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def isOnLine(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isOnLine(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).isOnLine(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector4()"""
        val = _Vector4()
        self.__wrapper = val

    @overload
    def idt(self, arg0: 'Vector4') -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.idt(com.badlogic.gdx.math.Vector4)"""
        return bool._wrap(super(_Vector4, self).idt(arg0))

    @override
    @overload
    def nor(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.nor()"""
        return 'Vector4'._wrap(super(Vector4, self).nor())

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.epsilonEquals(float,float,float,float)"""
        return bool._wrap(super(_Vector4, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinearOpposite(com.badlogic.gdx.math.Vector4,float)"""
        return bool._wrap(super(_Vector4, self).isCollinearOpposite(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def setZero(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setZero()"""
        return 'Vector4'._wrap(super(Vector4, self).setZero())

    @overload
    def isCollinear(self, arg0: 'Vector4', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isCollinear(com.badlogic.gdx.math.Vector4,float)"""
        return bool._wrap(super(_Vector4, self).isCollinear(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.setToRandomDirection()"""
        return 'Vector4'._wrap(super(Vector4, self).setToRandomDirection())

    @overload
    def set(self, arg0: 'Vector4') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(com.badlogic.gdx.math.Vector4)"""
        return 'Vector4'._wrap(super(_Vector4, self).set(arg0))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isZero()"""
        return bool._wrap(super(Vector4, self).isZero())

    @overload
    def set(self, arg0: 'float') -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.set(float[])"""
        return 'Vector4'._wrap(super(_Vector4, self).set(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def mulAdd(self, arg0: 'Vector4', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.mulAdd(com.badlogic.gdx.math.Vector4,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).mulAdd(arg0, _float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Vector4', arg1: float) -> 'Vector4':
        """public com.badlogic.gdx.math.Vector4 com.badlogic.gdx.math.Vector4.lerp(com.badlogic.gdx.math.Vector4,float)"""
        return 'Vector4'._wrap(super(_Vector4, self).lerp(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isUnit()"""
        return bool._wrap(super(Vector4, self).isUnit())

    @overload
    def dst(self, arg0: 'Vector4') -> float:
        """public float com.badlogic.gdx.math.Vector4.dst(com.badlogic.gdx.math.Vector4)"""
        return float._wrap(super(_Vector4, self).dst(arg0))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector4.isUnit(float)"""
        return bool._wrap(super(_Vector4, self).isUnit(_float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.math.Matrix3
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
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.Matrix3 as _Matrix3
_Matrix3 = _Matrix3
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Matrix3():
    """com.badlogic.gdx.math.Matrix3"""
 
    @staticmethod
    def _wrap(java_value: _Matrix3) -> 'Matrix3':
        return Matrix3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Matrix3):
        """
        Dynamic initializer for Matrix3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Matrix3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Matrix3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Matrix3.getValues()"""
        return List[float]._wrap(super(Matrix3, self).getValues())

    @overload
    def mulLeft(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.mulLeft(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).mulLeft(arg0))

    @overload
    def __init__(self, arg0: 'Matrix3'):
        """public com.badlogic.gdx.math.Matrix3(com.badlogic.gdx.math.Matrix3)"""
        val = _Matrix3(arg0)
        self.__wrapper = val

    @overload
    def scale(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scale(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).scale(arg0))

    @overload
    def setToScaling(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToScaling(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToScaling(arg0))

    @overload
    def trn(self, arg0: 'Vector3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).trn(arg0))

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scale(float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).scale(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float, arg2: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(com.badlogic.gdx.math.Vector3,float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToRotation(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def rotateRad(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.rotateRad(float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).rotateRad(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Matrix3(float[])"""
        val = _Matrix3(arg0)
        self.__wrapper = val

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.translate(float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).translate(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def transpose(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.transpose()"""
        return 'Matrix3'._wrap(super(Matrix3, self).transpose())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getRotationRad(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.getRotationRad()"""
        return float._wrap(super(Matrix3, self).getRotationRad())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'Matrix4') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).set(arg0))

    @overload
    def trn(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).trn(arg0))

    @overload
    def rotate(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.rotate(float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).rotate(_float.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.translate(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).translate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Matrix3.toString()"""
        return str._wrap(super(Matrix3, self).toString())

    @overload
    def setToTranslation(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToTranslation(float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToTranslation(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def inv(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.inv()"""
        return 'Matrix3'._wrap(super(Matrix3, self).inv())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Matrix3()"""
        val = _Matrix3()
        self.__wrapper = val

    @overload
    def setToRotationRad(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotationRad(float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToRotationRad(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Affine2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).set(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.getRotation()"""
        return float._wrap(super(Matrix3, self).getRotation())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def idt(self) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.idt()"""
        return 'Matrix3'._wrap(super(Matrix3, self).idt())

    @overload
    def scl(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).scl(arg0))

    @overload
    def scl(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).scl(_float.valueOf(arg0)))

    @overload
    def setToRotation(self, arg0: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToRotation(_float.valueOf(arg0)))

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Matrix3.det()"""
        return float._wrap(super(Matrix3, self).det())

    @overload
    def getScale(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Matrix3.getScale(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Matrix3, self).getScale(arg0))

    @overload
    def setToTranslation(self, arg0: 'Vector2') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToTranslation(arg0))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).mul(arg0))

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToRotation(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToRotation(arg0, _float.valueOf(arg1)))

    @overload
    def scl(self, arg0: 'Vector3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).scl(arg0))

    @overload
    def setToScaling(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.setToScaling(float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).setToScaling(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Matrix3') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).set(arg0))

    @overload
    def set(self, arg0: 'float') -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.set(float[])"""
        return 'Matrix3'._wrap(super(_Matrix3, self).set(arg0))

    @overload
    def getTranslation(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Matrix3.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Matrix3, self).getTranslation(arg0))

    @overload
    def trn(self, arg0: float, arg1: float) -> 'Matrix3':
        """public com.badlogic.gdx.math.Matrix3 com.badlogic.gdx.math.Matrix3.trn(float,float)"""
        return 'Matrix3'._wrap(super(_Matrix3, self).trn(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def __init__(self):
        """public com.badlogic.gdx.math.Matrix3()"""
        val = _Matrix3()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Path
import com.badlogic.gdx.math.Path as _Path
_Path = _Path
from abc import abstractmethod, ABC
 
class Path():
    """com.badlogic.gdx.math.Path"""
 
    @staticmethod
    def _wrap(java_value: _Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Path):
        """
        Dynamic initializer for Path.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Path__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Path__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def locate(self, arg0: object):
        """public abstract float com.badlogic.gdx.math.Path.locate(T)"""
        pass

    @abstractmethod
    def approxLength(self, arg0: int):
        """public abstract float com.badlogic.gdx.math.Path.approxLength(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.math.Vector2
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vector2():
    """com.badlogic.gdx.math.Vector2"""
 
    @staticmethod
    def _wrap(java_value: _Vector2) -> 'Vector2':
        return Vector2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector2):
        """
        Dynamic initializer for Vector2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isPerpendicular(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_Vector2, self).isPerpendicular(arg0, _float.valueOf(arg1)))

    @overload
    def angle(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angle(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).angle(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasOppositeDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).hasOppositeDirection(arg0))

    @override
    @overload
    def nor(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.nor()"""
        return 'Vector2'._wrap(super(Vector2, self).nor())

    @overload
    def isCollinear(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).isCollinear(arg0))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float,float)"""
        return bool._wrap(super(_Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(float,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).set(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setAngleDeg(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleDeg(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).setAngleDeg(_float.valueOf(arg0)))

    @overload
    def lerp(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.lerp(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).lerp(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.set(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Vector2, self).set(arg0))

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst(float,float,float,float)"""
        return float._wrap(_Vector2.dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).mulAdd(arg0, _float.valueOf(arg1)))

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
    def epsilonEquals(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).epsilonEquals(arg0))

    @overload
    def __init__(self, arg0: 'Vector2'):
        """public com.badlogic.gdx.math.Vector2(com.badlogic.gdx.math.Vector2)"""
        val = _Vector2(arg0)
        self.__wrapper = val

    @overload
    def dst(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).dst(arg0))

    @overload
    def angleDeg(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).angleDeg(arg0))

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setToRandomDirection()"""
        return 'Vector2'._wrap(super(Vector2, self).setToRandomDirection())

    @overload
    def sub(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Vector2, self).sub(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_Vector2, self).isOnLine(arg0, _float.valueOf(arg1)))

    @overload
    def scl(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).scl(_float.valueOf(arg0)))

    @overload
    def mulAdd(self, arg0: 'Vector2', arg1: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mulAdd(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Vector2, self).mulAdd(arg0, arg1))

    @override
    @overload
    def setZero(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setZero()"""
        return 'Vector2'._wrap(super(Vector2, self).setZero())

    @overload
    def setLength(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).setLength(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.equals(java.lang.Object)"""
        return bool._wrap(super(_Vector2, self).equals(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit()"""
        return bool._wrap(super(Vector2, self).isUnit())

    @overload
    def setLength2(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setLength2(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).setLength2(_float.valueOf(arg0)))

    @overload
    def interpolate(self, arg0: 'Vector2', arg1: float, arg2: 'Interpolation') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.interpolate(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector2'._wrap(super(_Vector2, self).interpolate(arg0, _float.valueOf(arg1), arg2))

    @overload
    def limit2(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit2(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).limit2(_float.valueOf(arg0)))

    @overload
    def setAngle(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngle(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).setAngle(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector2()"""
        val = _Vector2()
        self.__wrapper = val

    @override
    @overload
    def cpy(self) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.cpy()"""
        return 'Vector2'._wrap(super(Vector2, self).cpy())

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
    def add(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Vector2, self).add(arg0))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).isCollinearOpposite(arg0))

    @overload
    def dst2(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(float,float)"""
        return float._wrap(super(_Vector2, self).dst2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinear(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinear(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_Vector2, self).isCollinear(arg0, _float.valueOf(arg1)))

    @overload
    def dst2(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dst2(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).dst2(arg0))

    @overload
    def idt(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.idt(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).idt(arg0))

    @overload
    def dst(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dst(float,float)"""
        return float._wrap(super(_Vector2, self).dst(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isPerpendicular(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isPerpendicular(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).isPerpendicular(arg0))

    @overload
    def rotateDeg(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateDeg(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotateDeg(_float.valueOf(arg0)))

    @overload
    def sub(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.sub(float,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).sub(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector2'._wrap(super(_Vector2, self).mul(arg0))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isUnit(float)"""
        return bool._wrap(super(_Vector2, self).isUnit(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector2()"""
        val = _Vector2()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Vector2(float,float)"""
        val = _Vector2(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len2()"""
        return float._wrap(super(Vector2, self).len2())

    @overload
    def rotate(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotate(_float.valueOf(arg0)))

    @overload
    def angleRad(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).angleRad(arg0))

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.clamp(float,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).clamp(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero(float)"""
        return bool._wrap(super(_Vector2, self).isZero(_float.valueOf(arg0)))

    @overload
    def rotateAroundDeg(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundDeg(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotateAroundDeg(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(float,float)"""
        return float._wrap(super(_Vector2, self).dot(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isZero()"""
        return bool._wrap(super(Vector2, self).isZero())

    @overload
    def angle(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angle()"""
        return float._wrap(super(Vector2, self).angle())

    @overload
    def limit(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.limit(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).limit(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dot(float,float,float,float)"""
        return float._wrap(_Vector2.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def crs(self, arg0: float, arg1: float) -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(float,float)"""
        return float._wrap(super(_Vector2, self).crs(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def scl(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Vector2, self).scl(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def hasSameDirection(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.hasSameDirection(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).hasSameDirection(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_Vector2, self).epsilonEquals(arg0, _float.valueOf(arg1)))

    @overload
    def isOnLine(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isOnLine(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Vector2, self).isOnLine(arg0))

    @overload
    def add(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.add(float,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).add(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.len(float,float)"""
        return float._wrap(_Vector2.len(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def angleRad(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleRad()"""
        return float._wrap(super(Vector2, self).angleRad())

    @overload
    def crs(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.crs(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).crs(arg0))

    @overload
    def angleDeg(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.angleDeg()"""
        return float._wrap(super(Vector2, self).angleDeg())

    @overload
    def setAngleRad(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.setAngleRad(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).setAngleRad(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector2.hashCode()"""
        return int._wrap(super(Vector2, self).hashCode())

    @overload
    def epsilonEquals(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.epsilonEquals(float,float)"""
        return bool._wrap(super(_Vector2, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def rotateAround(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAround(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotateAround(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def scl(self, arg0: float, arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.scl(float,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).scl(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector2.len()"""
        return float._wrap(super(Vector2, self).len())

    @overload
    def rotate90(self, arg0: int) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotate90(int)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotate90(_int.valueOf(arg0)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector2', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector2.isCollinearOpposite(com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(super(_Vector2, self).isCollinearOpposite(arg0, _float.valueOf(arg1)))

    @overload
    def rotateAroundRad(self, arg0: 'Vector2', arg1: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateAroundRad(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotateAroundRad(arg0, _float.valueOf(arg1)))

    @overload
    def fromString(self, arg0: str) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.fromString(java.lang.String)"""
        return 'Vector2'._wrap(super(_Vector2, self).fromString(arg0))

    @overload
    def rotateRad(self, arg0: float) -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Vector2.rotateRad(float)"""
        return 'Vector2'._wrap(super(_Vector2, self).rotateRad(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector2.toString()"""
        return str._wrap(super(Vector2, self).toString())

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.math.Vector2.dst2(float,float,float,float)"""
        return float._wrap(_Vector2.dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def dot(self, arg0: 'Vector2') -> float:
        """public float com.badlogic.gdx.math.Vector2.dot(com.badlogic.gdx.math.Vector2)"""
        return float._wrap(super(_Vector2, self).dot(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Vector
import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from abc import abstractmethod, ABC
 
class Vector():
    """com.badlogic.gdx.math.Vector"""
 
    @staticmethod
    def _wrap(java_value: _Vector) -> 'Vector':
        return Vector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector):
        """
        Dynamic initializer for Vector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.math.Octree$Collider
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

from abc import abstractmethod, ABC
import com.badlogic.gdx.math.Octree as _Octree_Collider
_Collider = _Octree_Collider.Collider
 
class Collider():
    """com.badlogic.gdx.math.Octree.Collider"""
 
    @staticmethod
    def _wrap(java_value: _Collider) -> 'Collider':
        return Collider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Collider):
        """
        Dynamic initializer for Collider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Collider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Collider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.math.Octree$RayCastResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.Octree as _Octree_RayCastResult
_RayCastResult = _Octree_RayCastResult.RayCastResult
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RayCastResult():
    """com.badlogic.gdx.math.Octree.RayCastResult"""
 
    @staticmethod
    def _wrap(java_value: _RayCastResult) -> 'RayCastResult':
        return RayCastResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RayCastResult):
        """
        Dynamic initializer for RayCastResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RayCastResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RayCastResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public com.badlogic.gdx.math.Octree$RayCastResult()"""
        val = _RayCastResult()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Octree$RayCastResult()"""
        val = _RayCastResult()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$PowIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.math.Interpolation as _Interpolation_PowIn
_PowIn = _Interpolation_PowIn.PowIn
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PowIn():
    """com.badlogic.gdx.math.Interpolation.PowIn"""
 
    @staticmethod
    def _wrap(java_value: _PowIn) -> 'PowIn':
        return PowIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PowIn):
        """
        Dynamic initializer for PowIn.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PowIn__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PowIn__wrapper":
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$PowIn.apply(float)"""
        return float._wrap(super(_PowIn, self).apply(_float.valueOf(arg0)))

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

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$PowIn(int)"""
        val = _PowIn(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.math.Bresenham2
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.Bresenham2 as _Bresenham2
_Bresenham2 = _Bresenham2
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bresenham2():
    """com.badlogic.gdx.math.Bresenham2"""
 
    @staticmethod
    def _wrap(java_value: _Bresenham2) -> 'Bresenham2':
        return Bresenham2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bresenham2):
        """
        Dynamic initializer for Bresenham2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bresenham2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bresenham2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(int,int,int,int)"""
        return 'utils.Array'._wrap(super(_Bresenham2, self).line(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
        """public com.badlogic.gdx.math.Bresenham2()"""
        val = _Bresenham2()
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
    def line(self, arg0: 'GridPoint2', arg1: 'GridPoint2') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(com.badlogic.gdx.math.GridPoint2,com.badlogic.gdx.math.GridPoint2)"""
        return 'utils.Array'._wrap(super(_Bresenham2, self).line(arg0, arg1))

    @overload
    def line(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'Pool', arg5: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2> com.badlogic.gdx.math.Bresenham2.line(int,int,int,int,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.math.GridPoint2>,com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.GridPoint2>)"""
        return 'utils.Array'._wrap(super(_Bresenham2, self).line(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5))

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
    def __init__(self):
        """public com.badlogic.gdx.math.Bresenham2()"""
        val = _Bresenham2()
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
 
 
# CLASS: com.badlogic.gdx.math.Affine2
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.math.Affine2 as _Affine2
_Affine2 = _Affine2
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Affine2():
    """com.badlogic.gdx.math.Affine2"""
 
    @staticmethod
    def _wrap(java_value: _Affine2) -> 'Affine2':
        return Affine2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Affine2):
        """
        Dynamic initializer for Affine2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Affine2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Affine2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Affine2.toString()"""
        return str._wrap(super(Affine2, self).toString())

    @overload
    def isIdt(self) -> bool:
        """public boolean com.badlogic.gdx.math.Affine2.isIdt()"""
        return bool._wrap(super(Affine2, self).isIdt())

    @overload
    def preRotateRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preRotateRad(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).preRotateRad(_float.valueOf(arg0)))

    @overload
    def scale(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.scale(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).scale(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def shear(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.shear(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).shear(arg0))

    @overload
    def applyTo(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.math.Affine2.applyTo(com.badlogic.gdx.math.Vector2)"""
        super(_Affine2, self).applyTo(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def preTranslate(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preTranslate(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).preTranslate(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def translate(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.translate(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).translate(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def preScale(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preScale(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).preScale(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def rotate(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.rotate(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).rotate(_float.valueOf(arg0)))

    @overload
    def setToProduct(self, arg0: 'Affine2', arg1: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToProduct(com.badlogic.gdx.math.Affine2,com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToProduct(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setToTranslation(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTranslation(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTranslation(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToTrnRotRadScl(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotRadScl(float,float,float,float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnRotRadScl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def setToTrnRotScl(self, arg0: 'Vector2', arg1: float, arg2: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotScl(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnRotScl(arg0, _float.valueOf(arg1), arg2))

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Affine2.det()"""
        return float._wrap(super(Affine2, self).det())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def preTranslate(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preTranslate(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).preTranslate(arg0))

    @overload
    def set(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'._wrap(super(_Affine2, self).set(arg0))

    @overload
    def setToRotation(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotation(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToRotation(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToShearing(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToShearing(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToShearing(arg0))

    @overload
    def preShear(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preShear(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).preShear(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: 'Matrix3') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Affine2'._wrap(super(_Affine2, self).set(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setToShearing(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToShearing(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToShearing(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToTrnRotRadScl(self, arg0: 'Vector2', arg1: float, arg2: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotRadScl(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnRotRadScl(arg0, _float.valueOf(arg1), arg2))

    @overload
    def shear(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.shear(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).shear(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Affine2()"""
        val = _Affine2()
        self.__wrapper = val

    @overload
    def getTranslation(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Affine2.getTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Affine2, self).getTranslation(arg0))

    @overload
    def preMul(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preMul(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'._wrap(super(_Affine2, self).preMul(arg0))

    @overload
    def idt(self) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.idt()"""
        return 'Affine2'._wrap(super(Affine2, self).idt())

    @overload
    def set(self, arg0: 'Matrix4') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Affine2'._wrap(super(_Affine2, self).set(arg0))

    @overload
    def setToRotation(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotation(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToRotation(_float.valueOf(arg0)))

    @overload
    def setToTranslation(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTranslation(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTranslation(arg0))

    @overload
    def setToScaling(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToScaling(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToScaling(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setToTrnScl(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnScl(float,float,float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnScl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Affine2()"""
        val = _Affine2()
        self.__wrapper = val

    @overload
    def isTranslation(self) -> bool:
        """public boolean com.badlogic.gdx.math.Affine2.isTranslation()"""
        return bool._wrap(super(Affine2, self).isTranslation())

    @overload
    def mul(self, arg0: 'Affine2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.mul(com.badlogic.gdx.math.Affine2)"""
        return 'Affine2'._wrap(super(_Affine2, self).mul(arg0))

    @overload
    def translate(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.translate(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).translate(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setToScaling(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToScaling(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToScaling(arg0))

    @overload
    def rotateRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.rotateRad(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).rotateRad(_float.valueOf(arg0)))

    @overload
    def preRotate(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preRotate(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).preRotate(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def preShear(self, arg0: float, arg1: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preShear(float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).preShear(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def scale(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.scale(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).scale(arg0))

    @overload
    def setToTrnScl(self, arg0: 'Vector2', arg1: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnScl(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnScl(arg0, arg1))

    @overload
    def preScale(self, arg0: 'Vector2') -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.preScale(com.badlogic.gdx.math.Vector2)"""
        return 'Affine2'._wrap(super(_Affine2, self).preScale(arg0))

    @overload
    def inv(self) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.inv()"""
        return 'Affine2'._wrap(super(Affine2, self).inv())

    @overload
    def setToRotationRad(self, arg0: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToRotationRad(float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToRotationRad(_float.valueOf(arg0)))

    @overload
    def setToTrnRotScl(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Affine2':
        """public com.badlogic.gdx.math.Affine2 com.badlogic.gdx.math.Affine2.setToTrnRotScl(float,float,float,float,float)"""
        return 'Affine2'._wrap(super(_Affine2, self).setToTrnRotScl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def __init__(self, arg0: 'Affine2'):
        """public com.badlogic.gdx.math.Affine2(com.badlogic.gdx.math.Affine2)"""
        val = _Affine2(arg0)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.GridPoint2
from builtins import str
import com.badlogic.gdx.math.GridPoint2 as _GridPoint2
_GridPoint2 = _GridPoint2
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GridPoint2():
    """com.badlogic.gdx.math.GridPoint2"""
 
    @staticmethod
    def _wrap(java_value: _GridPoint2) -> 'GridPoint2':
        return GridPoint2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GridPoint2):
        """
        Dynamic initializer for GridPoint2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GridPoint2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GridPoint2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.add(int,int)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).add(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def dst(self, arg0: int, arg1: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst(int,int)"""
        return float._wrap(super(_GridPoint2, self).dst(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def cpy(self) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.cpy()"""
        return 'GridPoint2'._wrap(super(GridPoint2, self).cpy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dst2(self, arg0: int, arg1: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst2(int,int)"""
        return float._wrap(super(_GridPoint2, self).dst2(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'GridPoint2'):
        """public com.badlogic.gdx.math.GridPoint2(com.badlogic.gdx.math.GridPoint2)"""
        val = _GridPoint2(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.GridPoint2()"""
        val = _GridPoint2()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.GridPoint2.equals(java.lang.Object)"""
        return bool._wrap(super(_GridPoint2, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.GridPoint2.hashCode()"""
        return int._wrap(super(GridPoint2, self).hashCode())

    @overload
    def dst2(self, arg0: 'GridPoint2') -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst2(com.badlogic.gdx.math.GridPoint2)"""
        return float._wrap(super(_GridPoint2, self).dst2(arg0))

    @overload
    def set(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.set(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.GridPoint2()"""
        val = _GridPoint2()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.GridPoint2.toString()"""
        return str._wrap(super(GridPoint2, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dst(self, arg0: 'GridPoint2') -> float:
        """public float com.badlogic.gdx.math.GridPoint2.dst(com.badlogic.gdx.math.GridPoint2)"""
        return float._wrap(super(_GridPoint2, self).dst(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.add(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).add(arg0))

    @overload
    def set(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.set(int,int)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sub(self, arg0: int, arg1: int) -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.sub(int,int)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).sub(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.math.GridPoint2(int,int)"""
        val = _GridPoint2(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def sub(self, arg0: 'GridPoint2') -> 'GridPoint2':
        """public com.badlogic.gdx.math.GridPoint2 com.badlogic.gdx.math.GridPoint2.sub(com.badlogic.gdx.math.GridPoint2)"""
        return 'GridPoint2'._wrap(super(_GridPoint2, self).sub(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ElasticIn
import com.badlogic.gdx.math.Interpolation as _Interpolation_ElasticIn
_ElasticIn = _Interpolation_ElasticIn.ElasticIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ElasticIn():
    """com.badlogic.gdx.math.Interpolation.ElasticIn"""
 
    @staticmethod
    def _wrap(java_value: _ElasticIn) -> 'ElasticIn':
        return ElasticIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ElasticIn):
        """
        Dynamic initializer for ElasticIn.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ElasticIn__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ElasticIn__wrapper":
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
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$ElasticIn(float,float,int,float)"""
        val = _ElasticIn(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))
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

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ElasticIn.apply(float)"""
        return float._wrap(super(_ElasticIn, self).apply(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Plane
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.math.Plane as _Plane
_Plane = _Plane
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.Plane as _Plane_PlaneSide
_PlaneSide = _Plane_PlaneSide.PlaneSide
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Plane():
    """com.badlogic.gdx.math.Plane"""
 
    @staticmethod
    def _wrap(java_value: _Plane) -> 'Plane':
        return Plane(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Plane):
        """
        Dynamic initializer for Plane.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Plane__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Plane__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _Plane(arg0, arg1)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_Plane, self).set(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,float)"""
        val = _Plane(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isFrontFacing(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Plane.isFrontFacing(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Plane, self).isFrontFacing(arg0))

    @overload
    def testPoint(self, arg0: float, arg1: float, arg2: float) -> 'PlaneSide':
        """public com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane.testPoint(float,float,float)"""
        return 'PlaneSide'._wrap(super(_Plane, self).testPoint(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getNormal(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Plane.getNormal()"""
        return 'Vector3'._wrap(super(Plane, self).getNormal())

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public com.badlogic.gdx.math.Plane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _Plane(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_Plane, self).set(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getD(self) -> float:
        """public float com.badlogic.gdx.math.Plane.getD()"""
        return float._wrap(super(Plane, self).getD())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void com.badlogic.gdx.math.Plane.set(float,float,float,float,float,float)"""
        super(_Plane, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def set(self, arg0: 'Plane'):
        """public void com.badlogic.gdx.math.Plane.set(com.badlogic.gdx.math.Plane)"""
        super(_Plane, self).set(arg0)

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.math.Plane.set(float,float,float,float)"""
        super(_Plane, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def testPoint(self, arg0: 'Vector3') -> 'PlaneSide':
        """public com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane.testPoint(com.badlogic.gdx.math.Vector3)"""
        return 'PlaneSide'._wrap(super(_Plane, self).testPoint(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def distance(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Plane.distance(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Plane, self).distance(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Plane()"""
        val = _Plane()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Plane()"""
        val = _Plane()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Plane.toString()"""
        return str._wrap(super(Plane, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$PowOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.math.Interpolation as _Interpolation_PowOut
_PowOut = _Interpolation_PowOut.PowOut
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PowOut():
    """com.badlogic.gdx.math.Interpolation.PowOut"""
 
    @staticmethod
    def _wrap(java_value: _PowOut) -> 'PowOut':
        return PowOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PowOut):
        """
        Dynamic initializer for PowOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PowOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PowOut__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$PowOut(int)"""
        val = _PowOut(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$PowOut.apply(float)"""
        return float._wrap(super(_PowOut, self).apply(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ElasticOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation_ElasticOut
_ElasticOut = _Interpolation_ElasticOut.ElasticOut
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ElasticOut():
    """com.badlogic.gdx.math.Interpolation.ElasticOut"""
 
    @staticmethod
    def _wrap(java_value: _ElasticOut) -> 'ElasticOut':
        return ElasticOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ElasticOut):
        """
        Dynamic initializer for ElasticOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ElasticOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ElasticOut__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$ElasticOut(float,float,int,float)"""
        val = _ElasticOut(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))
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

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ElasticOut.apply(float)"""
        return float._wrap(super(_ElasticOut, self).apply(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Polyline
import com.badlogic.gdx.math.Polyline as _Polyline
_Polyline = _Polyline
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Polyline():
    """com.badlogic.gdx.math.Polyline"""
 
    @staticmethod
    def _wrap(java_value: _Polyline) -> 'Polyline':
        return Polyline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Polyline):
        """
        Dynamic initializer for Polyline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Polyline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Polyline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.rotate(float)"""
        super(_Polyline, self).rotate(_float.valueOf(arg0))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Polyline.contains(float,float)"""
        return bool._wrap(super(_Polyline, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Polyline()"""
        val = _Polyline()
        self.__wrapper = val

    @overload
    def getTransformedVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polyline.getTransformedVertices()"""
        return List[float]._wrap(super(Polyline, self).getTransformedVertices())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateScaledLength(self):
        """public void com.badlogic.gdx.math.Polyline.calculateScaledLength()"""
        super(Polyline, self).calculateScaledLength()

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
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.setRotation(float)"""
        super(_Polyline, self).setRotation(_float.valueOf(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getOriginX()"""
        return float._wrap(super(Polyline, self).getOriginX())

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.math.Polyline.scale(float)"""
        super(_Polyline, self).scale(_float.valueOf(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getX()"""
        return float._wrap(super(Polyline, self).getX())

    @overload
    def calculateLength(self):
        """public void com.badlogic.gdx.math.Polyline.calculateLength()"""
        super(Polyline, self).calculateLength()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getScaledLength(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaledLength()"""
        return float._wrap(super(Polyline, self).getScaledLength())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaleX()"""
        return float._wrap(super(Polyline, self).getScaleX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setOrigin(float,float)"""
        super(_Polyline, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setVertices(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Polyline.setVertices(float[])"""
        super(_Polyline, self).setVertices(arg0)

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getOriginY()"""
        return float._wrap(super(Polyline, self).getOriginY())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Polyline()"""
        val = _Polyline()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Polyline(float[])"""
        val = _Polyline(arg0)
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Polyline.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Polyline, self).contains(arg0))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polyline.getVertices()"""
        return List[float]._wrap(super(Polyline, self).getVertices())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getY()"""
        return float._wrap(super(Polyline, self).getY())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getLength()"""
        return float._wrap(super(Polyline, self).getLength())

    @overload
    def dirty(self):
        """public void com.badlogic.gdx.math.Polyline.dirty()"""
        super(Polyline, self).dirty()

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getScaleY()"""
        return float._wrap(super(Polyline, self).getScaleY())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setPosition(float,float)"""
        super(_Polyline, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getBoundingRectangle(self) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Polyline.getBoundingRectangle()"""
        return 'Rectangle'._wrap(super(Polyline, self).getBoundingRectangle())

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.setScale(float,float)"""
        super(_Polyline, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Polyline.getRotation()"""
        return float._wrap(super(Polyline, self).getRotation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polyline.translate(float,float)"""
        super(_Polyline, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Intersector as _Intersector
_Intersector = _Intersector
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Intersector():
    """com.badlogic.gdx.math.Intersector"""
 
    @staticmethod
    def _wrap(java_value: _Intersector) -> 'Intersector':
        return Intersector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Intersector):
        """
        Dynamic initializer for Intersector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Intersector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Intersector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def intersectPlanes(arg0: 'Plane', arg1: 'Plane', arg2: 'Plane', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPlanes(com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectPlanes(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def intersectRayPlane(arg0: 'Ray', arg1: 'Plane', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayPlane(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayPlane(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectLines(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLines(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.intersectLines(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def distanceLinePoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceLinePoint(float,float,float,float,float,float)"""
        return float._wrap(_Intersector.distanceLinePoint(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def distanceSegmentPoint(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2') -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceSegmentPoint(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float._wrap(_Intersector.distanceSegmentPoint(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'List', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,java.util.List<com.badlogic.gdx.math.Vector3>,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayTriangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayOrientedBounds(arg0: 'Ray', arg1: 'OrientedBoundingBox', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.OrientedBoundingBox,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayOrientedBounds(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nearestSegmentPoint(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Intersector.nearestSegmentPoint(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_Intersector.nearestSegmentPoint(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nearestSegmentPoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Vector2') -> 'Vector2':
        """public static com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Intersector.nearestSegmentPoint(float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return Vector2._wrap(_Intersector.nearestSegmentPoint(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6))

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

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'float', arg1: 'float', arg2: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(float[],float[],com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool._wrap(_Intersector.overlapConvexPolygons(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectPolygons(arg0: 'Polygon', arg1: 'Polygon', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon)"""
        return bool._wrap(_Intersector.intersectPolygons(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegmentCircle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentCircle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        return bool._wrap(_Intersector.intersectSegmentCircle(arg0, arg1, arg2, _float.valueOf(arg3)))

    @staticmethod
    @overload
    def intersectLinePlane(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Plane', arg7: 'Vector3') -> float:
        """public static float com.badlogic.gdx.math.Intersector.intersectLinePlane(float,float,float,float,float,float,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return float._wrap(_Intersector.intersectLinePlane(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def intersectFrustumBounds(arg0: 'Frustum', arg1: 'BoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectFrustumBounds(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(_Intersector.intersectFrustumBounds(arg0, arg1))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.isPointInTriangle(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'float', arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int, arg6: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(float[],int,int,float[],int,int,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool._wrap(_Intersector.overlapConvexPolygons(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4), _int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def intersectPolygons(arg0: 'FloatArray', arg1: 'FloatArray') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygons(com.badlogic.gdx.utils.FloatArray,com.badlogic.gdx.utils.FloatArray)"""
        return bool._wrap(_Intersector.intersectPolygons(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayOrientedBoundsFast(arg0: 'Ray', arg1: 'OrientedBoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(_Intersector.intersectRayOrientedBoundsFast(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayOrientedBoundsFast(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Matrix4') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(_Intersector.intersectRayOrientedBoundsFast(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectBoundsPlaneFast(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectBoundsPlaneFast(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(_Intersector.intersectBoundsPlaneFast(arg0, arg1, arg2, _float.valueOf(arg3)))

    @staticmethod
    @overload
    def intersectBoundsPlaneFast(arg0: 'BoundingBox', arg1: 'Plane') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectBoundsPlaneFast(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Plane)"""
        return bool._wrap(_Intersector.intersectBoundsPlaneFast(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def intersectRayBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayBounds(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegmentRectangle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentRectangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_Intersector.intersectSegmentRectangle(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegmentPolygon(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentPolygon(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Polygon)"""
        return bool._wrap(_Intersector.intersectSegmentPolygon(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(float,float,float,float,float,float,float,float)"""
        return bool._wrap(_Intersector.isPointInTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @staticmethod
    @overload
    def isPointInTriangle(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInTriangle(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.isPointInTriangle(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def intersectLines(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLines(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.intersectLines(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), arg8))

    @staticmethod
    @overload
    def intersectLinePolygon(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectLinePolygon(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Polygon)"""
        return bool._wrap(_Intersector.intersectLinePolygon(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayBoundsFast(arg0: 'Ray', arg1: 'Vector3', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayBoundsFast(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def overlaps(arg0: 'Circle', arg1: 'Circle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Circle)"""
        return bool._wrap(_Intersector.overlaps(arg0, arg1))

    @staticmethod
    @overload
    def hasOverlap(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.hasOverlap(com.badlogic.gdx.math.Vector3[],com.badlogic.gdx.math.Vector3[],com.badlogic.gdx.math.Vector3[])"""
        return bool._wrap(_Intersector.hasOverlap(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def intersectRayTriangle(arg0: 'Ray', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangle(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayTriangle(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def intersectSegmentCircle(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Circle', arg3: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentCircle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool._wrap(_Intersector.intersectSegmentCircle(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def pointLineSide(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2') -> int:
        """public static int com.badlogic.gdx.math.Intersector.pointLineSide(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return int._wrap(_Intersector.pointLineSide(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectSegmentPlane(arg0: 'Vector3', arg1: 'Vector3', arg2: 'Plane', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentPlane(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectSegmentPlane(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def intersectRayRay(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> float:
        """public static float com.badlogic.gdx.math.Intersector.intersectRayRay(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float._wrap(_Intersector.intersectRayRay(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'Polygon', arg1: 'Polygon') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon)"""
        return bool._wrap(_Intersector.overlapConvexPolygons(arg0, arg1))

    @staticmethod
    @overload
    def intersectSegments(arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegments(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.intersectSegments(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def intersectRayBoundsFast(arg0: 'Ray', arg1: 'BoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayBoundsFast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(_Intersector.intersectRayBoundsFast(arg0, arg1))

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'float', arg2: 'short', arg3: int, arg4: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,float[],short[],int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayTriangles(arg0, arg1, arg2, _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def intersectPolygonEdges(arg0: 'FloatArray', arg1: 'FloatArray') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectPolygonEdges(com.badlogic.gdx.utils.FloatArray,com.badlogic.gdx.utils.FloatArray)"""
        return bool._wrap(_Intersector.intersectPolygonEdges(arg0, arg1))

    @staticmethod
    @overload
    def intersectRectangles(arg0: 'Rectangle', arg1: 'Rectangle', arg2: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRectangles(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_Intersector.intersectRectangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def overlaps(arg0: 'Rectangle', arg1: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_Intersector.overlaps(arg0, arg1))

    @staticmethod
    @overload
    def splitTriangle(arg0: 'float', arg1: 'Plane', arg2: 'SplitTriangle'):
        """public static void com.badlogic.gdx.math.Intersector.splitTriangle(float[],com.badlogic.gdx.math.Plane,com.badlogic.gdx.math.Intersector$SplitTriangle)"""
        _Intersector.splitTriangle(arg0, arg1, arg2)

    @staticmethod
    @overload
    def distanceSegmentPoint(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Intersector.distanceSegmentPoint(float,float,float,float,float,float)"""
        return float._wrap(_Intersector.distanceSegmentPoint(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def overlaps(arg0: 'Circle', arg1: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlaps(com.badlogic.gdx.math.Circle,com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_Intersector.overlaps(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isPointInPolygon(arg0: 'Array', arg1: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInPolygon(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.isPointInPolygon(arg0, arg1))

    @staticmethod
    @overload
    def intersectFrustumBounds(arg0: 'Frustum', arg1: 'OrientedBoundingBox') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectFrustumBounds(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(_Intersector.intersectFrustumBounds(arg0, arg1))

    @staticmethod
    @overload
    def intersectSegments(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: 'Vector2') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegments(float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(_Intersector.intersectSegments(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), arg8))

    @staticmethod
    @overload
    def intersectRaySphere(arg0: 'Ray', arg1: 'Vector3', arg2: float, arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRaySphere(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Vector3,float,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRaySphere(arg0, arg1, _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def isPointInPolygon(arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: float) -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.isPointInPolygon(float[],int,int,float,float)"""
        return bool._wrap(_Intersector.isPointInPolygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @staticmethod
    @overload
    def pointLineSide(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> int:
        """public static int com.badlogic.gdx.math.Intersector.pointLineSide(float,float,float,float,float,float)"""
        return int._wrap(_Intersector.pointLineSide(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @staticmethod
    @overload
    def intersectSegmentRectangle(arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectSegmentRectangle(float,float,float,float,com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_Intersector.intersectSegmentRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def overlapConvexPolygons(arg0: 'Polygon', arg1: 'Polygon', arg2: 'MinimumTranslationVector') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.overlapConvexPolygons(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Polygon,com.badlogic.gdx.math.Intersector$MinimumTranslationVector)"""
        return bool._wrap(_Intersector.overlapConvexPolygons(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def intersectRayTriangles(arg0: 'Ray', arg1: 'float', arg2: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayTriangles(com.badlogic.gdx.math.collision.Ray,float[],com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayTriangles(arg0, arg1, arg2))

    @staticmethod
    @overload
    def intersectRayOrientedBounds(arg0: 'Ray', arg1: 'BoundingBox', arg2: 'Matrix4', arg3: 'Vector3') -> bool:
        """public static boolean com.badlogic.gdx.math.Intersector.intersectRayOrientedBounds(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(_Intersector.intersectRayOrientedBounds(arg0, arg1, arg2, arg3)) 
 
 
# CLASS: com.badlogic.gdx.math.CumulativeDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.CumulativeDistribution as _CumulativeDistribution
_CumulativeDistribution = _CumulativeDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CumulativeDistribution():
    """com.badlogic.gdx.math.CumulativeDistribution"""
 
    @staticmethod
    def _wrap(java_value: _CumulativeDistribution) -> 'CumulativeDistribution':
        return CumulativeDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CumulativeDistribution):
        """
        Dynamic initializer for CumulativeDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CumulativeDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CumulativeDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.CumulativeDistribution()"""
        val = _CumulativeDistribution()
        self.__wrapper = val

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.math.CumulativeDistribution.add(T)"""
        super(_CumulativeDistribution, self).add(arg0)

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
    def value(self) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.value()"""
        return object._wrap(super(CumulativeDistribution, self).value())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, arg0: object, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.add(T,float)"""
        super(_CumulativeDistribution, self).add(arg0, _float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.CumulativeDistribution()"""
        val = _CumulativeDistribution()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getValue(self, arg0: int) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.getValue(int)"""
        return object._wrap(super(_CumulativeDistribution, self).getValue(_int.valueOf(arg0)))

    @overload
    def generateUniform(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.generateUniform()"""
        super(CumulativeDistribution, self).generateUniform()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def clear(self):
        """public void com.badlogic.gdx.math.CumulativeDistribution.clear()"""
        super(CumulativeDistribution, self).clear()

    @overload
    def setInterval(self, arg0: object, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.setInterval(T,float)"""
        super(_CumulativeDistribution, self).setInterval(arg0, _float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getInterval(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.CumulativeDistribution.getInterval(int)"""
        return float._wrap(super(_CumulativeDistribution, self).getInterval(_int.valueOf(arg0)))

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
    def setInterval(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.math.CumulativeDistribution.setInterval(int,float)"""
        super(_CumulativeDistribution, self).setInterval(_int.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.math.CumulativeDistribution.size()"""
        return int._wrap(super(CumulativeDistribution, self).size())

    @overload
    def value(self, arg0: float) -> object:
        """public T com.badlogic.gdx.math.CumulativeDistribution.value(float)"""
        return object._wrap(super(_CumulativeDistribution, self).value(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.MathUtils
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.MathUtils as _MathUtils
_MathUtils = _MathUtils
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MathUtils():
    """com.badlogic.gdx.math.MathUtils"""
 
    @staticmethod
    def _wrap(java_value: _MathUtils) -> 'MathUtils':
        return MathUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MathUtils):
        """
        Dynamic initializer for MathUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MathUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MathUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def randomBoolean(arg0: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.randomBoolean(float)"""
        return bool._wrap(_MathUtils.randomBoolean(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def randomBoolean() -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.randomBoolean()"""
        return bool._wrap(_MathUtils.randomBoolean())

    @staticmethod
    @overload
    def round(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.round(float)"""
        return int._wrap(_MathUtils.round(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def asin(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.asin(float)"""
        return float._wrap(_MathUtils.asin(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def ceil(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.ceil(float)"""
        return int._wrap(_MathUtils.ceil(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def randomTriangular(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float,float)"""
        return float._wrap(_MathUtils.randomTriangular(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def random(arg0: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.random(long)"""
        return int._wrap(_MathUtils.random(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ceilPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.ceilPositive(float)"""
        return int._wrap(_MathUtils.ceilPositive(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.clamp(long,long,long)"""
        return int._wrap(_MathUtils.clamp(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def random(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random(float)"""
        return float._wrap(_MathUtils.random(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double com.badlogic.gdx.math.MathUtils.clamp(double,double,double)"""
        return float._wrap(_MathUtils.clamp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def log(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.log(float,float)"""
        return float._wrap(_MathUtils.log(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def atanUnchecked(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atanUnchecked(double)"""
        return float._wrap(_MathUtils.atanUnchecked(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def randomTriangular(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float,float,float)"""
        return float._wrap(_MathUtils.randomTriangular(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def random(arg0: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.random(int)"""
        return int._wrap(_MathUtils.random(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def lerpAngle(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerpAngle(float,float,float)"""
        return float._wrap(_MathUtils.lerpAngle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def cosDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.cosDeg(float)"""
        return float._wrap(_MathUtils.cosDeg(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def map(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.map(float,float,float,float,float)"""
        return float._wrap(_MathUtils.map(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @staticmethod
    @overload
    def tan(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.tan(float)"""
        return float._wrap(_MathUtils.tan(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sinDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.sinDeg(float)"""
        return float._wrap(_MathUtils.sinDeg(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def tanDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.tanDeg(float)"""
        return float._wrap(_MathUtils.tanDeg(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def atan(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan(float)"""
        return float._wrap(_MathUtils.atan(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sin(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.sin(float)"""
        return float._wrap(_MathUtils.sin(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.random(int,int)"""
        return int._wrap(_MathUtils.random(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def isZero(arg0: float, arg1: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isZero(float,float)"""
        return bool._wrap(_MathUtils.isZero(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def asinDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.asinDeg(float)"""
        return float._wrap(_MathUtils.asinDeg(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def randomTriangular(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular(float)"""
        return float._wrap(_MathUtils.randomTriangular(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static short com.badlogic.gdx.math.MathUtils.clamp(short,short,short)"""
        return int._wrap(_MathUtils.clamp(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def roundPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.roundPositive(float)"""
        return int._wrap(_MathUtils.roundPositive(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def random(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random(float,float)"""
        return float._wrap(_MathUtils.random(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def randomSign() -> int:
        """public static int com.badlogic.gdx.math.MathUtils.randomSign()"""
        return int._wrap(_MathUtils.randomSign())

    @staticmethod
    @overload
    def randomTriangular() -> float:
        """public static float com.badlogic.gdx.math.MathUtils.randomTriangular()"""
        return float._wrap(_MathUtils.randomTriangular())

    @staticmethod
    @overload
    def random() -> float:
        """public static float com.badlogic.gdx.math.MathUtils.random()"""
        return float._wrap(_MathUtils.random())

    @staticmethod
    @overload
    def isEqual(arg0: float, arg1: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isEqual(float,float)"""
        return bool._wrap(_MathUtils.isEqual(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def floor(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.floor(float)"""
        return int._wrap(_MathUtils.floor(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def isEqual(arg0: float, arg1: float, arg2: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isEqual(float,float,float)"""
        return bool._wrap(_MathUtils.isEqual(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def atan2(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2(float,float)"""
        return float._wrap(_MathUtils.atan2(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.clamp(float,float,float)"""
        return float._wrap(_MathUtils.clamp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def isPowerOfTwo(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isPowerOfTwo(int)"""
        return bool._wrap(_MathUtils.isPowerOfTwo(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2Deg360(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2Deg360(float,float)"""
        return float._wrap(_MathUtils.atan2Deg360(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def floorPositive(arg0: float) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.floorPositive(float)"""
        return int._wrap(_MathUtils.floorPositive(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def nextPowerOfTwo(arg0: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.nextPowerOfTwo(int)"""
        return int._wrap(_MathUtils.nextPowerOfTwo(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def atanDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atanDeg(float)"""
        return float._wrap(_MathUtils.atanDeg(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isZero(arg0: float) -> bool:
        """public static boolean com.badlogic.gdx.math.MathUtils.isZero(float)"""
        return bool._wrap(_MathUtils.isZero(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerp(float,float,float)"""
        return float._wrap(_MathUtils.lerp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def log2(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.log2(float)"""
        return float._wrap(_MathUtils.log2(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def lerpAngleDeg(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.lerpAngleDeg(float,float,float)"""
        return float._wrap(_MathUtils.lerpAngleDeg(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def atanUncheckedDeg(arg0: float) -> float:
        """public static double com.badlogic.gdx.math.MathUtils.atanUncheckedDeg(double)"""
        return float._wrap(_MathUtils.atanUncheckedDeg(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2Deg(arg0: float, arg1: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.atan2Deg(float,float)"""
        return float._wrap(_MathUtils.atan2Deg(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static int com.badlogic.gdx.math.MathUtils.clamp(int,int,int)"""
        return int._wrap(_MathUtils.clamp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def random(arg0: int, arg1: int) -> int:
        """public static long com.badlogic.gdx.math.MathUtils.random(long,long)"""
        return int._wrap(_MathUtils.random(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def cos(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.cos(float)"""
        return float._wrap(_MathUtils.cos(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def acos(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.acos(float)"""
        return float._wrap(_MathUtils.acos(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def acosDeg(arg0: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.acosDeg(float)"""
        return float._wrap(_MathUtils.acosDeg(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def norm(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.MathUtils.norm(float,float,float)"""
        return float._wrap(_MathUtils.norm(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector$MinimumTranslationVector
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.Intersector as _Intersector_MinimumTranslationVector
_MinimumTranslationVector = _Intersector_MinimumTranslationVector.MinimumTranslationVector
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MinimumTranslationVector():
    """com.badlogic.gdx.math.Intersector.MinimumTranslationVector"""
 
    @staticmethod
    def _wrap(java_value: _MinimumTranslationVector) -> 'MinimumTranslationVector':
        return MinimumTranslationVector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MinimumTranslationVector):
        """
        Dynamic initializer for MinimumTranslationVector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MinimumTranslationVector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MinimumTranslationVector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public com.badlogic.gdx.math.Intersector$MinimumTranslationVector()"""
        val = _MinimumTranslationVector()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Intersector$MinimumTranslationVector()"""
        val = _MinimumTranslationVector()
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Rectangle
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
from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rectangle():
    """com.badlogic.gdx.math.Rectangle"""
 
    @staticmethod
    def _wrap(java_value: _Rectangle) -> 'Rectangle':
        return Rectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rectangle):
        """
        Dynamic initializer for Rectangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rectangle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rectangle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def merge(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).merge(arg0))

    @overload
    def setX(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setX(float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setX(_float.valueOf(arg0)))

    @overload
    def merge(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(float,float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).merge(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getPosition(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Rectangle, self).getPosition(arg0))

    @overload
    def getAspectRatio(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getAspectRatio()"""
        return float._wrap(super(Rectangle, self).getAspectRatio())

    @overload
    def getSize(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getSize(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Rectangle, self).getSize(arg0))

    @overload
    def contains(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(super(_Rectangle, self).contains(arg0))

    @overload
    def __init__(self, arg0: 'Rectangle'):
        """public com.badlogic.gdx.math.Rectangle(com.badlogic.gdx.math.Rectangle)"""
        val = _Rectangle(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setPosition(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getX()"""
        return float._wrap(super(Rectangle, self).getX())

    @overload
    def setY(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setY(float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setY(_float.valueOf(arg0)))

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Rectangle, self).contains(arg0))

    @overload
    def fitInside(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitInside(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).fitInside(arg0))

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
    def setHeight(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setHeight(float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setHeight(_float.valueOf(arg0)))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.area()"""
        return float._wrap(super(Rectangle, self).area())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getY()"""
        return float._wrap(super(Rectangle, self).getY())

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float,float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setCenter(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(float,float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setCenter(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getHeight()"""
        return float._wrap(super(Rectangle, self).getHeight())

    @overload
    def fromString(self, arg0: str) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fromString(java.lang.String)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).fromString(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getWidth()"""
        return float._wrap(super(Rectangle, self).getWidth())

    @overload
    def getCenter(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getCenter(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Rectangle, self).getCenter(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Rectangle.toString()"""
        return str._wrap(super(Rectangle, self).toString())

    @overload
    def setWidth(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setWidth(float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setWidth(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Rectangle()"""
        val = _Rectangle()
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Circle)"""
        return bool._wrap(super(_Rectangle, self).contains(arg0))

    @overload
    def set(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(float,float)"""
        return bool._wrap(super(_Rectangle, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def perimeter(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.perimeter()"""
        return float._wrap(super(Rectangle, self).perimeter())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Rectangle.hashCode()"""
        return int._wrap(super(Rectangle, self).hashCode())

    @overload
    def merge(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).merge(arg0))

    @overload
    def overlaps(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.overlaps(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(super(_Rectangle, self).overlaps(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.equals(java.lang.Object)"""
        return bool._wrap(super(_Rectangle, self).equals(arg0))

    @overload
    def setSize(self, arg0: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setSize(_float.valueOf(arg0)))

    @overload
    def setCenter(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(com.badlogic.gdx.math.Vector2)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setCenter(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(float,float,float,float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Rectangle(float,float,float,float)"""
        val = _Rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def fitOutside(self, arg0: 'Rectangle') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitOutside(com.badlogic.gdx.math.Rectangle)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).fitOutside(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Rectangle()"""
        val = _Rectangle()
        self.__wrapper = val

    @overload
    def merge(self, arg0: 'Vector2') -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2[])"""
        return 'Rectangle'._wrap(super(_Rectangle, self).merge(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(float,float)"""
        return 'Rectangle'._wrap(super(_Rectangle, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ExpOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.math.Interpolation as _Interpolation_ExpOut
_ExpOut = _Interpolation_ExpOut.ExpOut
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExpOut():
    """com.badlogic.gdx.math.Interpolation.ExpOut"""
 
    @staticmethod
    def _wrap(java_value: _ExpOut) -> 'ExpOut':
        return ExpOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExpOut):
        """
        Dynamic initializer for ExpOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExpOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExpOut__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ExpOut.apply(float)"""
        return float._wrap(super(_ExpOut, self).apply(_float.valueOf(arg0)))

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
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Interpolation$ExpOut(float,float)"""
        val = _ExpOut(_float.valueOf(arg0), _float.valueOf(arg1))
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
 
 
# CLASS: com.badlogic.gdx.math.Ellipse
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
import com.badlogic.gdx.math.Ellipse as _Ellipse
_Ellipse = _Ellipse
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ellipse():
    """com.badlogic.gdx.math.Ellipse"""
 
    @staticmethod
    def _wrap(java_value: _Ellipse) -> 'Ellipse':
        return Ellipse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ellipse):
        """
        Dynamic initializer for Ellipse.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ellipse__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ellipse__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Ellipse(float,float,float,float)"""
        val = _Ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def circumference(self) -> float:
        """public float com.badlogic.gdx.math.Ellipse.circumference()"""
        return float._wrap(super(Ellipse, self).circumference())

    @overload
    def set(self, arg0: 'Ellipse'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Ellipse)"""
        super(_Ellipse, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Ellipse()"""
        val = _Ellipse()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Ellipse.hashCode()"""
        return int._wrap(super(Ellipse, self).hashCode())

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setSize(float,float)"""
        return 'Ellipse'._wrap(super(_Ellipse, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def __init__(self, arg0: 'Circle'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Circle)"""
        val = _Ellipse(arg0)
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.contains(float,float)"""
        return bool._wrap(super(_Ellipse, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        val = _Ellipse(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Vector2,float,float)"""
        val = _Ellipse(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'Ellipse'._wrap(super(_Ellipse, self).setPosition(arg0))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Ellipse.area()"""
        return float._wrap(super(Ellipse, self).area())

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Ellipse, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Ellipse()"""
        val = _Ellipse()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Circle'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Circle)"""
        super(_Ellipse, self).set(arg0)

    @overload
    def __init__(self, arg0: 'Ellipse'):
        """public com.badlogic.gdx.math.Ellipse(com.badlogic.gdx.math.Ellipse)"""
        val = _Ellipse(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Ellipse.equals(java.lang.Object)"""
        return bool._wrap(super(_Ellipse, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void com.badlogic.gdx.math.Ellipse.set(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_Ellipse, self).set(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.math.Ellipse.set(float,float,float,float)"""
        super(_Ellipse, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.math.Ellipse.setPosition(float,float)"""
        return 'Ellipse'._wrap(super(_Ellipse, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.math.Intersector$SplitTriangle
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
import com.badlogic.gdx.math.Intersector as _Intersector_SplitTriangle
_SplitTriangle = _Intersector_SplitTriangle.SplitTriangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SplitTriangle():
    """com.badlogic.gdx.math.Intersector.SplitTriangle"""
 
    @staticmethod
    def _wrap(java_value: _SplitTriangle) -> 'SplitTriangle':
        return SplitTriangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SplitTriangle):
        """
        Dynamic initializer for SplitTriangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SplitTriangle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SplitTriangle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Intersector$SplitTriangle.toString()"""
        return str._wrap(super(SplitTriangle, self).toString())

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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Intersector$SplitTriangle(int)"""
        val = _SplitTriangle(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.math.WindowedMean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.WindowedMean as _WindowedMean
_WindowedMean = _WindowedMean
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WindowedMean():
    """com.badlogic.gdx.math.WindowedMean"""
 
    @staticmethod
    def _wrap(java_value: _WindowedMean) -> 'WindowedMean':
        return WindowedMean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowedMean):
        """
        Dynamic initializer for WindowedMean.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowedMean__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowedMean__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getHighest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getHighest()"""
        return float._wrap(super(WindowedMean, self).getHighest())

    @overload
    def getWindowValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.WindowedMean.getWindowValues()"""
        return List[float]._wrap(super(WindowedMean, self).getWindowValues())

    @overload
    def standardDeviation(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.standardDeviation()"""
        return float._wrap(super(WindowedMean, self).standardDeviation())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def hasEnoughData(self) -> bool:
        """public boolean com.badlogic.gdx.math.WindowedMean.hasEnoughData()"""
        return bool._wrap(super(WindowedMean, self).hasEnoughData())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getOldest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getOldest()"""
        return float._wrap(super(WindowedMean, self).getOldest())

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

    @overload
    def getMean(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getMean()"""
        return float._wrap(super(WindowedMean, self).getMean())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addValue(self, arg0: float):
        """public void com.badlogic.gdx.math.WindowedMean.addValue(float)"""
        super(_WindowedMean, self).addValue(_float.valueOf(arg0))

    @overload
    def getValueCount(self) -> int:
        """public int com.badlogic.gdx.math.WindowedMean.getValueCount()"""
        return int._wrap(super(WindowedMean, self).getValueCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLowest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getLowest()"""
        return float._wrap(super(WindowedMean, self).getLowest())

    @overload
    def getWindowSize(self) -> int:
        """public int com.badlogic.gdx.math.WindowedMean.getWindowSize()"""
        return int._wrap(super(WindowedMean, self).getWindowSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getLatest(self) -> float:
        """public float com.badlogic.gdx.math.WindowedMean.getLatest()"""
        return float._wrap(super(WindowedMean, self).getLatest())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.math.WindowedMean.clear()"""
        super(WindowedMean, self).clear()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.WindowedMean(int)"""
        val = _WindowedMean(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Exp
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation_Exp
_Exp = _Interpolation_Exp.Exp
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Exp():
    """com.badlogic.gdx.math.Interpolation.Exp"""
 
    @staticmethod
    def _wrap(java_value: _Exp) -> 'Exp':
        return Exp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Exp):
        """
        Dynamic initializer for Exp.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Exp__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Exp__wrapper":
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Exp.apply(float)"""
        return float._wrap(super(_Exp, self).apply(_float.valueOf(arg0)))

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
        """public com.badlogic.gdx.math.Interpolation$Exp(float,float)"""
        val = _Exp(_float.valueOf(arg0), _float.valueOf(arg1))
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Bounce
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.Interpolation as _Interpolation_Bounce
_Bounce = _Interpolation_Bounce.Bounce
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bounce():
    """com.badlogic.gdx.math.Interpolation.Bounce"""
 
    @staticmethod
    def _wrap(java_value: _Bounce) -> 'Bounce':
        return Bounce(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bounce):
        """
        Dynamic initializer for Bounce.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bounce__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bounce__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$Bounce(float[],float[])"""
        val = _Bounce(arg0, arg1)
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$Bounce(int)"""
        val = _Bounce(_int.valueOf(arg0))
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Bounce.apply(float)"""
        return float._wrap(super(_Bounce, self).apply(_float.valueOf(arg0)))

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Shape2D
from abc import abstractmethod, ABC
import com.badlogic.gdx.math.Shape2D as _Shape2D
_Shape2D = _Shape2D
 
class Shape2D():
    """com.badlogic.gdx.math.Shape2D"""
 
    @staticmethod
    def _wrap(java_value: _Shape2D) -> 'Shape2D':
        return Shape2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Shape2D):
        """
        Dynamic initializer for Shape2D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Shape2D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Shape2D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.math.Polygon
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
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.math.Polygon as _Polygon
_Polygon = _Polygon
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Polygon():
    """com.badlogic.gdx.math.Polygon"""
 
    @staticmethod
    def _wrap(java_value: _Polygon) -> 'Polygon':
        return Polygon(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Polygon):
        """
        Dynamic initializer for Polygon.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Polygon__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Polygon__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBoundingRectangle(self) -> 'Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Polygon.getBoundingRectangle()"""
        return 'Rectangle'._wrap(super(Polygon, self).getBoundingRectangle())

    @overload
    def setVertex(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.math.Polygon.setVertex(int,float,float)"""
        super(_Polygon, self).setVertex(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.translate(float,float)"""
        super(_Polygon, self).translate(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Polygon()"""
        val = _Polygon()
        self.__wrapper = val

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.rotate(float)"""
        super(_Polygon, self).rotate(_float.valueOf(arg0))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getScaleY()"""
        return float._wrap(super(Polygon, self).getScaleY())

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.setRotation(float)"""
        super(_Polygon, self).setRotation(_float.valueOf(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getRotation()"""
        return float._wrap(super(Polygon, self).getRotation())

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Polygon.contains(com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_Polygon, self).contains(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getOriginX()"""
        return float._wrap(super(Polygon, self).getOriginX())

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
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setScale(float,float)"""
        super(_Polygon, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getScaleX()"""
        return float._wrap(super(Polygon, self).getScaleX())

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setOrigin(float,float)"""
        super(_Polygon, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polygon.getVertices()"""
        return List[float]._wrap(super(Polygon, self).getVertices())

    @overload
    def getTransformedVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Polygon.getTransformedVertices()"""
        return List[float]._wrap(super(Polygon, self).getTransformedVertices())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getOriginY()"""
        return float._wrap(super(Polygon, self).getOriginY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getVertexCount(self) -> int:
        """public int com.badlogic.gdx.math.Polygon.getVertexCount()"""
        return int._wrap(super(Polygon, self).getVertexCount())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getX()"""
        return float._wrap(super(Polygon, self).getX())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Polygon()"""
        val = _Polygon()
        self.__wrapper = val

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.getY()"""
        return float._wrap(super(Polygon, self).getY())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Polygon(float[])"""
        val = _Polygon(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getVertex(self, arg0: int, arg1: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Polygon.getVertex(int,com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Polygon, self).getVertex(_int.valueOf(arg0), arg1))

    @overload
    def setVertices(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Polygon.setVertices(float[])"""
        super(_Polygon, self).setVertices(arg0)

    @overload
    def getCentroid(self, arg0: 'Vector2') -> 'Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Polygon.getCentroid(com.badlogic.gdx.math.Vector2)"""
        return 'Vector2'._wrap(super(_Polygon, self).getCentroid(arg0))

    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Polygon.area()"""
        return float._wrap(super(Polygon, self).area())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Polygon.contains(float,float)"""
        return bool._wrap(super(_Polygon, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.math.Polygon.scale(float)"""
        super(_Polygon, self).scale(_float.valueOf(arg0))

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
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.math.Polygon.setPosition(float,float)"""
        super(_Polygon, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def dirty(self):
        """public void com.badlogic.gdx.math.Polygon.dirty()"""
        super(Polygon, self).dirty()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.RandomXS128
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.random.RandomGenerator as _RandomGenerator
_RandomGenerator = _RandomGenerator
import java.util.stream.DoubleStream as _DoubleStream
_DoubleStream = _DoubleStream
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.util.stream.LongStream as LongStream
import java.util.random.RandomGenerator as RandomGenerator
import java.util.stream.DoubleStream as DoubleStream
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.util.stream.LongStream as _LongStream
_LongStream = _LongStream
import java.lang.Integer as _int
import com.badlogic.gdx.math.RandomXS128 as _RandomXS128
_RandomXS128 = _RandomXS128
import java.util.Random as _Random
_Random = _Random
import java.lang.Long as _long
from builtins import int
import java.util.Random as Random
import java.lang.Class as _Class
_Class = _Class
 
class RandomXS128():
    """com.badlogic.gdx.math.RandomXS128"""
 
    @staticmethod
    def _wrap(java_value: _RandomXS128) -> 'RandomXS128':
        return RandomXS128(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomXS128):
        """
        Dynamic initializer for RandomXS128.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomXS128__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomXS128__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def doubles(self, arg0: int) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(long)"""
        return 'DoubleStream'._wrap(super(_Random, self).doubles(_long.valueOf(arg0)))

    @overload
    def nextDouble(self, arg0: float) -> float:
        """public default double java.util.random.RandomGenerator.nextDouble(double)"""
        return float._wrap(super(_RandomGenerator, self).nextDouble(_double.valueOf(arg0)))

    @overload
    def setState(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.math.RandomXS128.setState(long,long)"""
        super(_RandomXS128, self).setState(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def ints(self, arg0: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(long)"""
        return 'IntStream'._wrap(super(_Random, self).ints(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def longs(self, arg0: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long)"""
        return 'LongStream'._wrap(super(_Random, self).longs(_long.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.RandomXS128()"""
        val = _RandomXS128()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def nextGaussian(self) -> float:
        """public synchronized double java.util.Random.nextGaussian()"""
        return float._wrap(super(Random, self).nextGaussian())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ints(self, arg0: int, arg1: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(int,int)"""
        return 'IntStream'._wrap(super(_Random, self).ints(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def nextFloat(self, arg0: float, arg1: float) -> float:
        """public default float java.util.random.RandomGenerator.nextFloat(float,float)"""
        return float._wrap(super(_RandomGenerator, self).nextFloat(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def isDeprecated(self) -> bool:
        """public default boolean java.util.random.RandomGenerator.isDeprecated()"""
        return bool._wrap(super(RandomGenerator, self).isDeprecated())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.math.RandomXS128.nextInt()"""
        return int._wrap(super(RandomXS128, self).nextInt())

    @overload
    def doubles(self, arg0: float, arg1: float) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(double,double)"""
        return 'DoubleStream'._wrap(super(_Random, self).doubles(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.RandomXS128()"""
        val = _RandomXS128()
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.math.RandomXS128.nextDouble()"""
        return float._wrap(super(RandomXS128, self).nextDouble())

    @override
    @overload
    def longs(self) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs()"""
        return 'LongStream'._wrap(super(Random, self).longs())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def nextExponential(self) -> float:
        """public default double java.util.random.RandomGenerator.nextExponential()"""
        return float._wrap(super(RandomGenerator, self).nextExponential())

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public default int java.util.random.RandomGenerator.nextInt(int,int)"""
        return int._wrap(super(_RandomGenerator, self).nextInt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def doubles(self) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles()"""
        return 'DoubleStream'._wrap(super(Random, self).doubles())

    @overload
    def getState(self, arg0: int) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.getState(int)"""
        return int._wrap(super(_RandomXS128, self).getState(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def nextLong(self, arg0: int, arg1: int) -> int:
        """public default long java.util.random.RandomGenerator.nextLong(long,long)"""
        return int._wrap(super(_RandomGenerator, self).nextLong(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def nextGaussian(self, arg0: float, arg1: float) -> float:
        """public default double java.util.random.RandomGenerator.nextGaussian(double,double)"""
        return float._wrap(super(_RandomGenerator, self).nextGaussian(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.math.RandomXS128.nextFloat()"""
        return float._wrap(super(RandomXS128, self).nextFloat())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long,long,long)"""
        return 'LongStream'._wrap(super(_Random, self).longs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def longs(self, arg0: int, arg1: int) -> 'LongStream':
        """public java.util.stream.LongStream java.util.Random.longs(long,long)"""
        return 'LongStream'._wrap(super(_Random, self).longs(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int com.badlogic.gdx.math.RandomXS128.nextInt(int)"""
        return int._wrap(super(_RandomXS128, self).nextInt(_int.valueOf(arg0)))

    @overload
    def nextDouble(self, arg0: float, arg1: float) -> float:
        """public default double java.util.random.RandomGenerator.nextDouble(double,double)"""
        return float._wrap(super(_RandomGenerator, self).nextDouble(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.math.RandomXS128(long,long)"""
        val = _RandomXS128(_long.valueOf(arg0), _long.valueOf(arg1))
        self.__wrapper = val

    @staticmethod
    @overload
    def from(arg0: 'RandomGenerator') -> 'Random':
        """public static java.util.Random java.util.Random.from(java.util.random.RandomGenerator)"""
        return Random._wrap(_Random.from(arg0))

    @override
    @overload
    def nextBytes(self, arg0: bytes):
        """public void com.badlogic.gdx.math.RandomXS128.nextBytes(byte[])"""
        super(_RandomXS128, self).nextBytes(bytes)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.RandomXS128(long)"""
        val = _RandomXS128(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def ints(self) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints()"""
        return 'IntStream'._wrap(super(Random, self).ints())

    @overload
    def nextLong(self, arg0: int) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.nextLong(long)"""
        return int._wrap(super(_RandomXS128, self).nextLong(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.math.RandomXS128.nextLong()"""
        return int._wrap(super(RandomXS128, self).nextLong())

    @override
    @overload
    def nextBoolean(self) -> bool:
        """public boolean com.badlogic.gdx.math.RandomXS128.nextBoolean()"""
        return bool._wrap(super(RandomXS128, self).nextBoolean())

    @overload
    def nextFloat(self, arg0: float) -> float:
        """public default float java.util.random.RandomGenerator.nextFloat(float)"""
        return float._wrap(super(_RandomGenerator, self).nextFloat(_float.valueOf(arg0)))

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void com.badlogic.gdx.math.RandomXS128.setSeed(long)"""
        super(_RandomXS128, self).setSeed(_long.valueOf(arg0))

    @overload
    def doubles(self, arg0: int, arg1: float, arg2: float) -> 'DoubleStream':
        """public java.util.stream.DoubleStream java.util.Random.doubles(long,double,double)"""
        return 'DoubleStream'._wrap(super(_Random, self).doubles(_long.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int) -> 'IntStream':
        """public java.util.stream.IntStream java.util.Random.ints(long,int,int)"""
        return 'IntStream'._wrap(super(_Random, self).ints(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.DelaunayTriangulator
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.math.DelaunayTriangulator as _DelaunayTriangulator
_DelaunayTriangulator = _DelaunayTriangulator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.utils.ShortArray as _ShortArray
_ShortArray = _ShortArray
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DelaunayTriangulator():
    """com.badlogic.gdx.math.DelaunayTriangulator"""
 
    @staticmethod
    def _wrap(java_value: _DelaunayTriangulator) -> 'DelaunayTriangulator':
        return DelaunayTriangulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DelaunayTriangulator):
        """
        Dynamic initializer for DelaunayTriangulator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DelaunayTriangulator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DelaunayTriangulator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def computeTriangles(self, arg0: 'FloatArray', arg1: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(com.badlogic.gdx.utils.FloatArray,boolean)"""
        return 'utils.ShortArray'._wrap(super(_DelaunayTriangulator, self).computeTriangles(arg0, _boolean.valueOf(arg1)))

    @overload
    def computeTriangles(self, arg0: 'float', arg1: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(float[],boolean)"""
        return 'utils.ShortArray'._wrap(super(_DelaunayTriangulator, self).computeTriangles(arg0, _boolean.valueOf(arg1)))

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
    def computeTriangles(self, arg0: 'float', arg1: int, arg2: int, arg3: bool) -> 'utils.ShortArray':
        """public com.badlogic.gdx.utils.ShortArray com.badlogic.gdx.math.DelaunayTriangulator.computeTriangles(float[],int,int,boolean)"""
        return 'utils.ShortArray'._wrap(super(_DelaunayTriangulator, self).computeTriangles(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def trim(self, arg0: 'ShortArray', arg1: 'float', arg2: 'float', arg3: int, arg4: int):
        """public void com.badlogic.gdx.math.DelaunayTriangulator.trim(com.badlogic.gdx.utils.ShortArray,float[],float[],int,int)"""
        super(_DelaunayTriangulator, self).trim(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4))

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
    def __init__(self):
        """public com.badlogic.gdx.math.DelaunayTriangulator()"""
        val = _DelaunayTriangulator()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.DelaunayTriangulator()"""
        val = _DelaunayTriangulator()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.math.Interpolation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Interpolation():
    """com.badlogic.gdx.math.Interpolation"""
 
    @staticmethod
    def _wrap(java_value: _Interpolation) -> 'Interpolation':
        return Interpolation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Interpolation):
        """
        Dynamic initializer for Interpolation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Interpolation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Interpolation__wrapper":
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Interpolation()"""
        val = _Interpolation()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Interpolation()"""
        val = _Interpolation()
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
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Swing
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.math.Interpolation as _Interpolation_Swing
_Swing = _Interpolation_Swing.Swing
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Swing():
    """com.badlogic.gdx.math.Interpolation.Swing"""
 
    @staticmethod
    def _wrap(java_value: _Swing) -> 'Swing':
        return Swing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Swing):
        """
        Dynamic initializer for Swing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Swing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Swing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$Swing(float)"""
        val = _Swing(_float.valueOf(arg0))
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

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Swing.apply(float)"""
        return float._wrap(super(_Swing, self).apply(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.FloatCounter
from builtins import str
import com.badlogic.gdx.math.FloatCounter as _FloatCounter
_FloatCounter = _FloatCounter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatCounter():
    """com.badlogic.gdx.math.FloatCounter"""
 
    @staticmethod
    def _wrap(java_value: _FloatCounter) -> 'FloatCounter':
        return FloatCounter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatCounter):
        """
        Dynamic initializer for FloatCounter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatCounter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatCounter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def put(self, arg0: float):
        """public void com.badlogic.gdx.math.FloatCounter.put(float)"""
        super(_FloatCounter, self).put(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.FloatCounter.toString()"""
        return str._wrap(super(FloatCounter, self).toString())

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.FloatCounter(int)"""
        val = _FloatCounter(_int.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.math.Plane$PlaneSide
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
import com.badlogic.gdx.math.Plane as _Plane_PlaneSide
_PlaneSide = _Plane_PlaneSide.PlaneSide
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlaneSide():
    """com.badlogic.gdx.math.Plane.PlaneSide"""
 
    @staticmethod
    def _wrap(java_value: _PlaneSide) -> 'PlaneSide':
        return PlaneSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlaneSide):
        """
        Dynamic initializer for PlaneSide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlaneSide__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlaneSide__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PlaneSide':
        """public static com.badlogic.gdx.math.Plane$PlaneSide com.badlogic.gdx.math.Plane$PlaneSide.valueOf(java.lang.String)"""
        return PlaneSide._wrap(_PlaneSide.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['PlaneSide']:
        """public static com.badlogic.gdx.math.Plane$PlaneSide[] com.badlogic.gdx.math.Plane$PlaneSide.values()"""
        return List[PlaneSide]._wrap(_PlaneSide.values()) 
 
 
# CLASS: com.badlogic.gdx.math.Matrix4
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Quaternion as _Quaternion
_Quaternion = _Quaternion
from typing import List
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Matrix4():
    """com.badlogic.gdx.math.Matrix4"""
 
    @staticmethod
    def _wrap(java_value: _Matrix4) -> 'Matrix4':
        return Matrix4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Matrix4):
        """
        Dynamic initializer for Matrix4.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Matrix4__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Matrix4__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mul(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.mul(float[],float[])"""
        _Matrix4.mul(arg0, arg1)

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleY()"""
        return float._wrap(super(Matrix4, self).getScaleY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0, arg1, arg2))

    @overload
    def setToTranslationAndScaling(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslationAndScaling(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToTranslationAndScaling(arg0, arg1))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0, arg1))

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Matrix4(float[])"""
        val = _Matrix4(arg0)
        self.__wrapper = val

    @overload
    def getScaleZ(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleZ()"""
        return float._wrap(super(Matrix4, self).getScaleZ())

    @overload
    def set(self, arg0: 'Matrix3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Matrix3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0))

    @overload
    def setTranslation(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setTranslation(arg0))

    @overload
    def translate(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.translate(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).translate(arg0))

    @overload
    def hasRotationOrScaling(self) -> bool:
        """public boolean com.badlogic.gdx.math.Matrix4.hasRotationOrScaling()"""
        return bool._wrap(super(Matrix4, self).hasRotationOrScaling())

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).mul(arg0))

    @overload
    def setFromEulerAngles(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setFromEulerAngles(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setFromEulerAngles(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def toNormalMatrix(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.toNormalMatrix()"""
        return 'Matrix4'._wrap(super(Matrix4, self).toNormalMatrix())

    @overload
    def setToWorld(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToWorld(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToWorld(arg0, arg1, arg2))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def rotate(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotate(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rotateRad(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotateRad(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotate(arg0, _float.valueOf(arg1)))

    @overload
    def setToTranslationAndScaling(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslationAndScaling(float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToTranslationAndScaling(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6)))

    @staticmethod
    @overload
    def inv(arg0: 'float') -> bool:
        """public static boolean com.badlogic.gdx.math.Matrix4.inv(float[])"""
        return bool._wrap(_Matrix4.inv(arg0))

    @overload
    def det(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.det()"""
        return float._wrap(super(Matrix4, self).det())

    @overload
    def lerp(self, arg0: 'Matrix4', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.lerp(com.badlogic.gdx.math.Matrix4,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def setToRotation(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setFromEulerAnglesRad(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setFromEulerAnglesRad(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setFromEulerAnglesRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def getValues(self) -> List[float]:
        """public float[] com.badlogic.gdx.math.Matrix4.getValues()"""
        return List[float]._wrap(super(Matrix4, self).getValues())

    @overload
    def rotateRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateRad(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotateRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getScaleZSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleZSquared()"""
        return float._wrap(super(Matrix4, self).getScaleZSquared())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Matrix4()"""
        val = _Matrix4()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Matrix4'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Matrix4)"""
        val = _Matrix4(arg0)
        self.__wrapper = val

    @overload
    def tra(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.tra()"""
        return 'Matrix4'._wrap(super(Matrix4, self).tra())

    @overload
    def getScaleXSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleXSquared()"""
        return float._wrap(super(Matrix4, self).getScaleXSquared())

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotation(arg0, _float.valueOf(arg1)))

    @overload
    def extract4x3Matrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Matrix4.extract4x3Matrix(float[])"""
        super(_Matrix4, self).extract4x3Matrix(arg0)

    @overload
    def setToLookAt(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToLookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToLookAt(arg0, arg1, arg2))

    @overload
    def set(self, arg0: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0))

    @staticmethod
    @overload
    def prj(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.prj(float[],float[],int,int,int)"""
        _Matrix4.prj(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def trn(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.trn(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).trn(arg0))

    @overload
    def cpy(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.cpy()"""
        return 'Matrix4'._wrap(super(Matrix4, self).cpy())

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scale(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def getRotation(self, arg0: 'Quaternion', arg1: bool) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Matrix4.getRotation(com.badlogic.gdx.math.Quaternion,boolean)"""
        return 'Quaternion'._wrap(super(_Matrix4, self).getRotation(arg0, _boolean.valueOf(arg1)))

    @overload
    def setToOrtho2D(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho2D(float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToOrtho2D(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def set(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def det3x3(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.det3x3()"""
        return float._wrap(super(Matrix4, self).det3x3())

    @overload
    def setToScaling(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToScaling(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToScaling(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def rotate(self, arg0: 'Quaternion') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotate(com.badlogic.gdx.math.Quaternion)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotate(arg0))

    @overload
    def set(self, arg0: 'Affine2') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0))

    @overload
    def setToRotationRad(self, arg0: 'Vector3', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotationRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotationRad(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Vector3'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Vector3)"""
        val = _Matrix4(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def setToLookAt(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToLookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToLookAt(arg0, arg1))

    @overload
    def setAsAffine(self, arg0: 'Affine2') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setAsAffine(com.badlogic.gdx.math.Affine2)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setAsAffine(arg0))

    @overload
    def rotateTowardDirection(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateTowardDirection(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotateTowardDirection(arg0, arg1))

    @overload
    def setToRotation(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def avg(self, arg0: 'Matrix4', arg1: 'float') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4[],float[])"""
        return 'Matrix4'._wrap(super(_Matrix4, self).avg(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def rot(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.rot(float[],float[])"""
        _Matrix4.rot(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def scl(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).scl(arg0))

    @overload
    def idt(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.idt()"""
        return 'Matrix4'._wrap(super(Matrix4, self).idt())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setToRotationRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotationRad(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotationRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).scl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setToRotation(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToRotation(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToRotation(arg0, arg1))

    @overload
    def setToOrtho2D(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho2D(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToOrtho2D(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def scl(self, arg0: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.scl(float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).scl(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0, arg1, arg2, arg3))

    @overload
    def setToOrtho(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToOrtho(float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToOrtho(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def avg(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4[])"""
        return 'Matrix4'._wrap(super(_Matrix4, self).avg(arg0))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.translate(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def getScale(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Matrix4.getScale(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Matrix4, self).getScale(arg0))

    @overload
    def setTranslation(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setTranslation(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setTranslation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def mulVec(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.mulVec(float[],float[])"""
        _Matrix4.mulVec(arg0, arg1)

    @overload
    def rotateTowardTarget(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.rotateTowardTarget(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).rotateTowardTarget(arg0, arg1))

    @overload
    def getScaleYSquared(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleYSquared()"""
        return float._wrap(super(Matrix4, self).getScaleYSquared())

    @overload
    def setAsAffine(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setAsAffine(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setAsAffine(arg0))

    @staticmethod
    @overload
    def rot(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.rot(float[],float[],int,int,int)"""
        _Matrix4.rot(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def setToScaling(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToScaling(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToScaling(arg0))

    @staticmethod
    @overload
    def mulVec(arg0: 'float', arg1: 'float', arg2: int, arg3: int, arg4: int):
        """public static native void com.badlogic.gdx.math.Matrix4.mulVec(float[],float[],int,int,int)"""
        _Matrix4.mulVec(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def setToTranslation(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslation(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToTranslation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float,float,float,float,float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9)))

    @overload
    def set(self, arg0: 'float') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.set(float[])"""
        return 'Matrix4'._wrap(super(_Matrix4, self).set(arg0))

    @overload
    def setToProjection(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToProjection(float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToProjection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setToProjection(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToProjection(float,float,float,float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToProjection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Matrix4()"""
        val = _Matrix4()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Quaternion'):
        """public com.badlogic.gdx.math.Matrix4(com.badlogic.gdx.math.Quaternion)"""
        val = _Matrix4(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def det(arg0: 'float') -> float:
        """public static float com.badlogic.gdx.math.Matrix4.det(float[])"""
        return float._wrap(_Matrix4.det(arg0))

    @overload
    def inv(self) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.inv()"""
        return 'Matrix4'._wrap(super(Matrix4, self).inv())

    @staticmethod
    @overload
    def prj(arg0: 'float', arg1: 'float'):
        """public static void com.badlogic.gdx.math.Matrix4.prj(float[],float[])"""
        _Matrix4.prj(arg0, arg1)

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.math.Matrix4.getScaleX()"""
        return float._wrap(super(Matrix4, self).getScaleX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Matrix4.toString()"""
        return str._wrap(super(Matrix4, self).toString())

    @overload
    def getRotation(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Matrix4.getRotation(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'._wrap(super(_Matrix4, self).getRotation(arg0))

    @overload
    def avg(self, arg0: 'Matrix4', arg1: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.avg(com.badlogic.gdx.math.Matrix4,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).avg(arg0, _float.valueOf(arg1)))

    @overload
    def trn(self, arg0: float, arg1: float, arg2: float) -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.trn(float,float,float)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).trn(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def getTranslation(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Matrix4.getTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Matrix4, self).getTranslation(arg0))

    @overload
    def mulLeft(self, arg0: 'Matrix4') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.mulLeft(com.badlogic.gdx.math.Matrix4)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).mulLeft(arg0))

    @overload
    def setToTranslation(self, arg0: 'Vector3') -> 'Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.Matrix4.setToTranslation(com.badlogic.gdx.math.Vector3)"""
        return 'Matrix4'._wrap(super(_Matrix4, self).setToTranslation(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.CatmullRomSpline
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.CatmullRomSpline as _CatmullRomSpline
_CatmullRomSpline = _CatmullRomSpline
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CatmullRomSpline():
    """com.badlogic.gdx.math.CatmullRomSpline"""
 
    @staticmethod
    def _wrap(java_value: _CatmullRomSpline) -> 'CatmullRomSpline':
        return CatmullRomSpline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CatmullRomSpline):
        """
        Dynamic initializer for CatmullRomSpline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CatmullRomSpline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CatmullRomSpline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.valueAt(T,float)"""
        return 'Vector'._wrap(super(_CatmullRomSpline, self).valueAt(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.CatmullRomSpline()"""
        val = _CatmullRomSpline()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.CatmullRomSpline()"""
        val = _CatmullRomSpline()
        self.__wrapper = val

    @overload
    def approximate(self, arg0: 'Vector', arg1: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T,int)"""
        return float._wrap(super(_CatmullRomSpline, self).approximate(arg0, _int.valueOf(arg1)))

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approxLength(int)"""
        return float._wrap(super(_CatmullRomSpline, self).approxLength(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.derivative(T,int,float,T[],boolean,T)"""
        return Vector._wrap(_CatmullRomSpline.derivative(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), arg5))

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T)"""
        return float._wrap(super(_CatmullRomSpline, self).approximate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.approximate(T,int,int)"""
        return float._wrap(super(_CatmullRomSpline, self).approximate(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.calculate(T,int,float,T[],boolean,T)"""
        return Vector._wrap(_CatmullRomSpline.calculate(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), arg5))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.derivativeAt(T,int,float)"""
        return 'Vector'._wrap(super(_CatmullRomSpline, self).derivativeAt(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.calculate(T,float,T[],boolean,T)"""
        return Vector._wrap(_CatmullRomSpline.calculate(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.CatmullRomSpline.derivative(T,float,T[],boolean,T)"""
        return Vector._wrap(_CatmullRomSpline.derivative(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.valueAt(T,int,float)"""
        return 'Vector'._wrap(super(_CatmullRomSpline, self).valueAt(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def nearest(self, arg0: 'Vector', arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.math.CatmullRomSpline.nearest(T,int,int)"""
        return int._wrap(super(_CatmullRomSpline, self).nearest(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vector', arg1: bool) -> 'CatmullRomSpline':
        """public com.badlogic.gdx.math.CatmullRomSpline com.badlogic.gdx.math.CatmullRomSpline.set(T[],boolean)"""
        return 'CatmullRomSpline'._wrap(super(_CatmullRomSpline, self).set(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.CatmullRomSpline.locate(T)"""
        return float._wrap(super(_CatmullRomSpline, self).locate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.CatmullRomSpline.derivativeAt(T,float)"""
        return 'Vector'._wrap(super(_CatmullRomSpline, self).derivativeAt(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector', arg1: bool):
        """public com.badlogic.gdx.math.CatmullRomSpline(T[],boolean)"""
        val = _CatmullRomSpline(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def nearest(self, arg0: 'Vector') -> int:
        """public int com.badlogic.gdx.math.CatmullRomSpline.nearest(T)"""
        return int._wrap(super(_CatmullRomSpline, self).nearest(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$SwingIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation_SwingIn
_SwingIn = _Interpolation_SwingIn.SwingIn
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SwingIn():
    """com.badlogic.gdx.math.Interpolation.SwingIn"""
 
    @staticmethod
    def _wrap(java_value: _SwingIn) -> 'SwingIn':
        return SwingIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SwingIn):
        """
        Dynamic initializer for SwingIn.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SwingIn__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SwingIn__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$SwingIn(float)"""
        val = _SwingIn(_float.valueOf(arg0))
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$SwingIn.apply(float)"""
        return float._wrap(super(_SwingIn, self).apply(_float.valueOf(arg0)))

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

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.CumulativeDistribution$CumulativeValue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.CumulativeDistribution as _CumulativeDistribution_CumulativeValue
_CumulativeValue = _CumulativeDistribution_CumulativeValue.CumulativeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CumulativeValue():
    """com.badlogic.gdx.math.CumulativeDistribution.CumulativeValue"""
 
    @staticmethod
    def _wrap(java_value: _CumulativeValue) -> 'CumulativeValue':
        return CumulativeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CumulativeValue):
        """
        Dynamic initializer for CumulativeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CumulativeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CumulativeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: 'CumulativeDistribution', arg1: object, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.CumulativeDistribution$CumulativeValue(T,float,float)"""
        val = _CumulativeValue(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))
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
 
 
# CLASS: com.badlogic.gdx.math.GridPoint3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.GridPoint3 as _GridPoint3
_GridPoint3 = _GridPoint3
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GridPoint3():
    """com.badlogic.gdx.math.GridPoint3"""
 
    @staticmethod
    def _wrap(java_value: _GridPoint3) -> 'GridPoint3':
        return GridPoint3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GridPoint3):
        """
        Dynamic initializer for GridPoint3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GridPoint3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GridPoint3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.add(int,int,int)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).add(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.GridPoint3.equals(java.lang.Object)"""
        return bool._wrap(super(_GridPoint3, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.set(int,int,int)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dst(self, arg0: 'GridPoint3') -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst(com.badlogic.gdx.math.GridPoint3)"""
        return float._wrap(super(_GridPoint3, self).dst(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.GridPoint3()"""
        val = _GridPoint3()
        self.__wrapper = val

    @overload
    def dst2(self, arg0: 'GridPoint3') -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst2(com.badlogic.gdx.math.GridPoint3)"""
        return float._wrap(super(_GridPoint3, self).dst2(arg0))

    @overload
    def set(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.set(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).set(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.GridPoint3.toString()"""
        return str._wrap(super(GridPoint3, self).toString())

    @overload
    def sub(self, arg0: int, arg1: int, arg2: int) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.sub(int,int,int)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).sub(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'GridPoint3'):
        """public com.badlogic.gdx.math.GridPoint3(com.badlogic.gdx.math.GridPoint3)"""
        val = _GridPoint3(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.math.GridPoint3(int,int,int)"""
        val = _GridPoint3(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.add(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).add(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.GridPoint3.hashCode()"""
        return int._wrap(super(GridPoint3, self).hashCode())

    @overload
    def dst(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst(int,int,int)"""
        return float._wrap(super(_GridPoint3, self).dst(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def sub(self, arg0: 'GridPoint3') -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.sub(com.badlogic.gdx.math.GridPoint3)"""
        return 'GridPoint3'._wrap(super(_GridPoint3, self).sub(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.GridPoint3()"""
        val = _GridPoint3()
        self.__wrapper = val

    @overload
    def dst2(self, arg0: int, arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.GridPoint3.dst2(int,int,int)"""
        return float._wrap(super(_GridPoint3, self).dst2(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def cpy(self) -> 'GridPoint3':
        """public com.badlogic.gdx.math.GridPoint3 com.badlogic.gdx.math.GridPoint3.cpy()"""
        return 'GridPoint3'._wrap(super(GridPoint3, self).cpy()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$SwingOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as _Interpolation_SwingOut
_SwingOut = _Interpolation_SwingOut.SwingOut
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SwingOut():
    """com.badlogic.gdx.math.Interpolation.SwingOut"""
 
    @staticmethod
    def _wrap(java_value: _SwingOut) -> 'SwingOut':
        return SwingOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SwingOut):
        """
        Dynamic initializer for SwingOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SwingOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SwingOut__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.math.Interpolation$SwingOut(float)"""
        val = _SwingOut(_float.valueOf(arg0))
        self.__wrapper = val

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

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$SwingOut.apply(float)"""
        return float._wrap(super(_SwingOut, self).apply(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.BSpline
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.math.BSpline as _BSpline
_BSpline = _BSpline
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BSpline():
    """com.badlogic.gdx.math.BSpline"""
 
    @staticmethod
    def _wrap(java_value: _BSpline) -> 'BSpline':
        return BSpline(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BSpline):
        """
        Dynamic initializer for BSpline.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BSpline__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BSpline__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.BSpline.locate(T)"""
        return float._wrap(super(_BSpline, self).locate(arg0))

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic_derivative(T,float,T[],boolean,T)"""
        return Vector._wrap(_BSpline.cubic_derivative(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: int, arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.derivative(T,float,T[],int,boolean,T)"""
        return Vector._wrap(_BSpline.derivative(arg0, _float.valueOf(arg1), arg2, _int.valueOf(arg3), _boolean.valueOf(arg4), arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T)"""
        return float._wrap(super(_BSpline, self).approximate(arg0))

    @overload
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approxLength(int)"""
        return float._wrap(super(_BSpline, self).approxLength(_int.valueOf(arg0)))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.derivativeAt(T,int,float)"""
        return 'Vector'._wrap(super(_BSpline, self).derivativeAt(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: int, arg5: bool, arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.calculate(T,int,float,T[],int,boolean,T)"""
        return Vector._wrap(_BSpline.calculate(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _int.valueOf(arg4), _boolean.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic(T,int,float,T[],boolean,T)"""
        return Vector._wrap(_BSpline.cubic(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), arg5))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.BSpline()"""
        val = _BSpline()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.BSpline()"""
        val = _BSpline()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: int, arg2: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.valueAt(T,int,float)"""
        return 'Vector'._wrap(super(_BSpline, self).valueAt(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calculate(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: int, arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.calculate(T,float,T[],int,boolean,T)"""
        return Vector._wrap(_BSpline.calculate(arg0, _float.valueOf(arg1), arg2, _int.valueOf(arg3), _boolean.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: int, arg5: bool, arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.derivative(T,int,float,T[],int,boolean,T)"""
        return Vector._wrap(_BSpline.derivative(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _int.valueOf(arg4), _boolean.valueOf(arg5), arg6))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def nearest(self, arg0: 'Vector', arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.math.BSpline.nearest(T,int,int)"""
        return int._wrap(super(_BSpline, self).nearest(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def nearest(self, arg0: 'Vector') -> int:
        """public int com.badlogic.gdx.math.BSpline.nearest(T)"""
        return int._wrap(super(_BSpline, self).nearest(arg0))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T,int,int)"""
        return float._wrap(super(_BSpline, self).approximate(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Vector', arg1: int, arg2: bool):
        """public com.badlogic.gdx.math.BSpline(T[],int,boolean)"""
        val = _BSpline(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: int, arg2: float, arg3: 'Vector', arg4: bool, arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic_derivative(T,int,float,T[],boolean,T)"""
        return Vector._wrap(_BSpline.cubic_derivative(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, _boolean.valueOf(arg4), arg5))

    @overload
    def set(self, arg0: 'Vector', arg1: int, arg2: bool) -> 'BSpline':
        """public com.badlogic.gdx.math.BSpline com.badlogic.gdx.math.BSpline.set(T[],int,boolean)"""
        return 'BSpline'._wrap(super(_BSpline, self).set(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.derivativeAt(T,float)"""
        return 'Vector'._wrap(super(_BSpline, self).derivativeAt(arg0, _float.valueOf(arg1)))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.BSpline.valueAt(T,float)"""
        return 'Vector'._wrap(super(_BSpline, self).valueAt(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: bool, arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.BSpline.cubic(T,float,T[],boolean,T)"""
        return Vector._wrap(_BSpline.cubic(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4))

    @overload
    def approximate(self, arg0: 'Vector', arg1: int) -> float:
        """public float com.badlogic.gdx.math.BSpline.approximate(T,int)"""
        return float._wrap(super(_BSpline, self).approximate(arg0, _int.valueOf(arg1)))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Quaternion
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Quaternion as _Quaternion
_Quaternion = _Quaternion
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Quaternion():
    """com.badlogic.gdx.math.Quaternion"""
 
    @staticmethod
    def _wrap(java_value: _Quaternion) -> 'Quaternion':
        return Quaternion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Quaternion):
        """
        Dynamic initializer for Quaternion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Quaternion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Quaternion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).set(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Quaternion()"""
        val = _Quaternion()
        self.__wrapper = val

    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.len2()"""
        return float._wrap(super(Quaternion, self).len2())

    @overload
    def setFromAxis(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxis(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxis(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setFromAxisRad(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxisRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxisRad(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFromCross(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromCross(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromCross(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAngleAround(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAround(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Quaternion, self).getAngleAround(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getYawRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getYawRad()"""
        return float._wrap(super(Quaternion, self).getYawRad())

    @overload
    def getAngleAroundRad(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAroundRad(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Quaternion, self).getAngleAroundRad(arg0))

    @overload
    def add(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.add(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).add(arg0))

    @overload
    def isIdentity(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.isIdentity(float)"""
        return bool._wrap(super(_Quaternion, self).isIdentity(_float.valueOf(arg0)))

    @overload
    def toMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.math.Quaternion.toMatrix(float[])"""
        super(_Quaternion, self).toMatrix(arg0)

    @overload
    def getSwingTwist(self, arg0: 'Vector3', arg1: 'Quaternion', arg2: 'Quaternion'):
        """public void com.badlogic.gdx.math.Quaternion.getSwingTwist(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Quaternion)"""
        super(_Quaternion, self).getSwingTwist(arg0, arg1, arg2)

    @overload
    def setEulerAngles(self, arg0: float, arg1: float, arg2: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setEulerAngles(float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setEulerAngles(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Quaternion.toString()"""
        return str._wrap(super(Quaternion, self).toString())

    @overload
    def nor(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.nor()"""
        return 'Quaternion'._wrap(super(Quaternion, self).nor())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.math.Quaternion(float,float,float,float)"""
        val = _Quaternion(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def mulLeft(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mulLeft(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).mulLeft(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def cpy(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.cpy()"""
        return 'Quaternion'._wrap(super(Quaternion, self).cpy())

    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getPitch()"""
        return float._wrap(super(Quaternion, self).getPitch())

    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.len()"""
        return float._wrap(super(Quaternion, self).len())

    @overload
    def slerp(self, arg0: 'Quaternion', arg1: 'float') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion[],float[])"""
        return 'Quaternion'._wrap(super(_Quaternion, self).slerp(arg0, arg1))

    @overload
    def exp(self, arg0: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.exp(float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).exp(_float.valueOf(arg0)))

    @overload
    def mulLeft(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mulLeft(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).mulLeft(arg0))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.dot(float,float,float,float)"""
        return float._wrap(super(_Quaternion, self).dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getRollRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getRollRad()"""
        return float._wrap(super(Quaternion, self).getRollRad())

    @overload
    def idt(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.idt()"""
        return 'Quaternion'._wrap(super(Quaternion, self).idt())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.dot(float,float,float,float,float,float,float,float)"""
        return float._wrap(_Quaternion.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Quaternion()"""
        val = _Quaternion()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.Quaternion(com.badlogic.gdx.math.Vector3,float)"""
        val = _Quaternion(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setFromAxisRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxisRad(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxisRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Quaternion.hashCode()"""
        return int._wrap(super(Quaternion, self).hashCode())

    @overload
    def transform(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Quaternion.transform(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Quaternion, self).transform(arg0))

    @overload
    def setFromAxis(self, arg0: 'Vector3', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxis(com.badlogic.gdx.math.Vector3,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxis(arg0, _float.valueOf(arg1)))

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngle()"""
        return float._wrap(super(Quaternion, self).getAngle())

    @overload
    def slerp(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion[])"""
        return 'Quaternion'._wrap(super(_Quaternion, self).slerp(arg0))

    @overload
    def getPitchRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getPitchRad()"""
        return float._wrap(super(Quaternion, self).getPitchRad())

    @overload
    def getAxisAngle(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAxisAngle(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Quaternion, self).getAxisAngle(arg0))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).mul(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setFromAxes(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxes(float,float,float,float,float,float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxes(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @overload
    def getAngleRad(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleRad()"""
        return float._wrap(super(Quaternion, self).getAngleRad())

    @overload
    def __init__(self, arg0: 'Quaternion'):
        """public com.badlogic.gdx.math.Quaternion(com.badlogic.gdx.math.Quaternion)"""
        val = _Quaternion(arg0)
        self.__wrapper = val

    @overload
    def setEulerAnglesRad(self, arg0: float, arg1: float, arg2: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setEulerAnglesRad(float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setEulerAnglesRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def getAngleAroundRad(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAroundRad(float,float,float)"""
        return float._wrap(super(_Quaternion, self).getAngleAroundRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setFromMatrix(self, arg0: bool, arg1: 'Matrix4') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(boolean,com.badlogic.gdx.math.Matrix4)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromMatrix(_boolean.valueOf(arg0), arg1))

    @overload
    def setFromAxes(self, arg0: bool, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromAxes(boolean,float,float,float,float,float,float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromAxes(_boolean.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9)))

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.len(float,float,float,float)"""
        return float._wrap(_Quaternion.len(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getRoll()"""
        return float._wrap(super(Quaternion, self).getRoll())

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static final float com.badlogic.gdx.math.Quaternion.len2(float,float,float,float)"""
        return float._wrap(_Quaternion.len2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def conjugate(self) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.conjugate()"""
        return 'Quaternion'._wrap(super(Quaternion, self).conjugate())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.set(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).set(arg0))

    @overload
    def setFromCross(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromCross(float,float,float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromCross(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def getAngleAround(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAngleAround(float,float,float)"""
        return float._wrap(super(_Quaternion, self).getAngleAround(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.equals(java.lang.Object)"""
        return bool._wrap(super(_Quaternion, self).equals(arg0))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.add(float,float,float,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setFromMatrix(self, arg0: bool, arg1: 'Matrix3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(boolean,com.badlogic.gdx.math.Matrix3)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromMatrix(_boolean.valueOf(arg0), arg1))

    @overload
    def getAxisAngleRad(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Quaternion.getAxisAngleRad(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Quaternion, self).getAxisAngleRad(arg0))

    @overload
    def slerp(self, arg0: 'Quaternion', arg1: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.slerp(com.badlogic.gdx.math.Quaternion,float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).slerp(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: 'Quaternion') -> float:
        """public float com.badlogic.gdx.math.Quaternion.dot(com.badlogic.gdx.math.Quaternion)"""
        return float._wrap(super(_Quaternion, self).dot(arg0))

    @overload
    def getSwingTwist(self, arg0: float, arg1: float, arg2: float, arg3: 'Quaternion', arg4: 'Quaternion'):
        """public void com.badlogic.gdx.math.Quaternion.getSwingTwist(float,float,float,com.badlogic.gdx.math.Quaternion,com.badlogic.gdx.math.Quaternion)"""
        super(_Quaternion, self).getSwingTwist(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3, arg4)

    @overload
    def setFromMatrix(self, arg0: 'Matrix3') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(com.badlogic.gdx.math.Matrix3)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromMatrix(arg0))

    @overload
    def isIdentity(self) -> bool:
        """public boolean com.badlogic.gdx.math.Quaternion.isIdentity()"""
        return bool._wrap(super(Quaternion, self).isIdentity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def mul(self, arg0: float) -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(float)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).mul(_float.valueOf(arg0)))

    @overload
    def mul(self, arg0: 'Quaternion') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.mul(com.badlogic.gdx.math.Quaternion)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).mul(arg0))

    @overload
    def getYaw(self) -> float:
        """public float com.badlogic.gdx.math.Quaternion.getYaw()"""
        return float._wrap(super(Quaternion, self).getYaw())

    @overload
    def setFromMatrix(self, arg0: 'Matrix4') -> 'Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.math.Quaternion.setFromMatrix(com.badlogic.gdx.math.Matrix4)"""
        return 'Quaternion'._wrap(super(_Quaternion, self).setFromMatrix(arg0))

    @overload
    def getGimbalPole(self) -> int:
        """public int com.badlogic.gdx.math.Quaternion.getGimbalPole()"""
        return int._wrap(super(Quaternion, self).getGimbalPole()) 
 
 
# CLASS: com.badlogic.gdx.math.Bezier
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

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
import com.badlogic.gdx.math.Bezier as _Bezier
_Bezier = _Bezier
import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Bezier():
    """com.badlogic.gdx.math.Bezier"""
 
    @staticmethod
    def _wrap(java_value: _Bezier) -> 'Bezier':
        return Bezier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Bezier):
        """
        Dynamic initializer for Bezier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Bezier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Bezier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def approxLength(self, arg0: int) -> float:
        """public float com.badlogic.gdx.math.Bezier.approxLength(int)"""
        return float._wrap(super(_Bezier, self).approxLength(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def quadratic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic(T,float,T,T,T,T)"""
        return Vector._wrap(_Bezier.quadratic(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Array', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(com.badlogic.gdx.utils.Array<T>,int,int)"""
        val = _Bezier(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Array', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(com.badlogic.gdx.utils.Array<T>,int,int)"""
        return 'Bezier'._wrap(super(_Bezier, self).set(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Vector', arg1: int, arg2: int):
        """public com.badlogic.gdx.math.Bezier(T[],int,int)"""
        val = _Bezier(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector', arg1: int, arg2: int) -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T[],int,int)"""
        return 'Bezier'._wrap(super(_Bezier, self).set(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Bezier()"""
        val = _Bezier()
        self.__wrapper = val

    @staticmethod
    @overload
    def cubic(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic(T,float,T,T,T,T,T)"""
        return Vector._wrap(_Bezier.cubic(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def locate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.locate(T)"""
        return float._wrap(super(_Bezier, self).locate(arg0))

    @staticmethod
    @overload
    def linear(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear(T,float,T,T,T)"""
        return Vector._wrap(_Bezier.linear(arg0, _float.valueOf(arg1), arg2, arg3, arg4))

    @overload
    def valueAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.valueAt(T,float)"""
        return 'Vector'._wrap(super(_Bezier, self).valueAt(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, *arg0: 'Vector') -> 'Bezier':
        """public com.badlogic.gdx.math.Bezier com.badlogic.gdx.math.Bezier.set(T...)"""
        return 'Bezier'._wrap(super(_Bezier, self).set(arg0))

    @overload
    def __init__(self, *arg0: 'Vector'):
        """public com.badlogic.gdx.math.Bezier(T...)"""
        val = _Bezier(arg0)
        self.__wrapper = val

    @overload
    def approximate(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.math.Bezier.approximate(T)"""
        return float._wrap(super(_Bezier, self).approximate(arg0))

    @staticmethod
    @overload
    def linear_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.linear_derivative(T,float,T,T,T)"""
        return Vector._wrap(_Bezier.linear_derivative(arg0, _float.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def quadratic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.quadratic_derivative(T,float,T,T,T,T)"""
        return Vector._wrap(_Bezier.quadratic_derivative(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5))

    @overload
    def derivativeAt(self, arg0: 'Vector', arg1: float) -> 'Vector':
        """public T com.badlogic.gdx.math.Bezier.derivativeAt(T,float)"""
        return 'Vector'._wrap(super(_Bezier, self).derivativeAt(arg0, _float.valueOf(arg1)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.math.Bezier()"""
        val = _Bezier()
        self.__wrapper = val

    @staticmethod
    @overload
    def cubic_derivative(arg0: 'Vector', arg1: float, arg2: 'Vector', arg3: 'Vector', arg4: 'Vector', arg5: 'Vector', arg6: 'Vector') -> 'Vector':
        """public static <T extends com.badlogic.gdx.math.Vector<T>> T com.badlogic.gdx.math.Bezier.cubic_derivative(T,float,T,T,T,T,T)"""
        return Vector._wrap(_Bezier.cubic_derivative(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$ExpIn
from builtins import str
import com.badlogic.gdx.math.Interpolation as _Interpolation_ExpIn
_ExpIn = _Interpolation_ExpIn.ExpIn
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExpIn():
    """com.badlogic.gdx.math.Interpolation.ExpIn"""
 
    @staticmethod
    def _wrap(java_value: _ExpIn) -> 'ExpIn':
        return ExpIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExpIn):
        """
        Dynamic initializer for ExpIn.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExpIn__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExpIn__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.math.Interpolation$ExpIn(float,float)"""
        val = _ExpIn(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$ExpIn.apply(float)"""
        return float._wrap(super(_ExpIn, self).apply(_float.valueOf(arg0)))

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

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$BounceOut
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.Interpolation as _Interpolation_BounceOut
_BounceOut = _Interpolation_BounceOut.BounceOut
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BounceOut():
    """com.badlogic.gdx.math.Interpolation.BounceOut"""
 
    @staticmethod
    def _wrap(java_value: _BounceOut) -> 'BounceOut':
        return BounceOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BounceOut):
        """
        Dynamic initializer for BounceOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BounceOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BounceOut__wrapper":
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$BounceOut(int)"""
        val = _BounceOut(_int.valueOf(arg0))
        self.__wrapper = val

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
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$BounceOut(float[],float[])"""
        val = _BounceOut(arg0, arg1)
        self.__wrapper = val

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$BounceOut.apply(float)"""
        return float._wrap(super(_BounceOut, self).apply(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Octree
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.ObjectSet as _ObjectSet
_ObjectSet = _ObjectSet
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
import com.badlogic.gdx.math.Octree as _Octree
_Octree = _Octree
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Octree():
    """com.badlogic.gdx.math.Octree"""
 
    @staticmethod
    def _wrap(java_value: _Octree) -> 'Octree':
        return Octree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Octree):
        """
        Dynamic initializer for Octree.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Octree__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Octree__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rayCast(self, arg0: 'Ray', arg1: 'RayCastResult') -> object:
        """public T com.badlogic.gdx.math.Octree.rayCast(com.badlogic.gdx.math.collision.Ray,com.badlogic.gdx.math.Octree$RayCastResult<T>)"""
        return object._wrap(super(_Octree, self).rayCast(arg0, arg1))

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.add(T)"""
        super(_Octree, self).add(arg0)

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
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.remove(T)"""
        super(_Octree, self).remove(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def update(self, arg0: object):
        """public void com.badlogic.gdx.math.Octree.update(T)"""
        super(_Octree, self).update(arg0)

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
    def query(self, arg0: 'Frustum', arg1: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.query(com.badlogic.gdx.math.Frustum,com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'._wrap(super(_Octree, self).query(arg0, arg1))

    @overload
    def getAll(self, arg0: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.getAll(com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'._wrap(super(_Octree, self).getAll(arg0))

    @overload
    def getNodesBoxes(self, arg0: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.math.collision.BoundingBox> com.badlogic.gdx.math.Octree.getNodesBoxes(com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.math.collision.BoundingBox>)"""
        return 'utils.ObjectSet'._wrap(super(_Octree, self).getNodesBoxes(arg0))

    @overload
    def query(self, arg0: 'BoundingBox', arg1: 'ObjectSet') -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<T> com.badlogic.gdx.math.Octree.query(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.utils.ObjectSet<T>)"""
        return 'utils.ObjectSet'._wrap(super(_Octree, self).query(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3', arg2: int, arg3: int, arg4: 'Collider'):
        """public com.badlogic.gdx.math.Octree(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int,com.badlogic.gdx.math.Octree$Collider<T>)"""
        val = _Octree(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), arg4)
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
 
 
# CLASS: com.badlogic.gdx.math.Vector3
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Vector3():
    """com.badlogic.gdx.math.Vector3"""
 
    @staticmethod
    def _wrap(java_value: _Vector3) -> 'Vector3':
        return Vector3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Vector3):
        """
        Dynamic initializer for Vector3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Vector3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Vector3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def add(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).add(arg0))

    @overload
    def rotateRad(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotateRad(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).rotateRad(arg0, _float.valueOf(arg1)))

    @overload
    def lerp(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.lerp(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).lerp(arg0, _float.valueOf(arg1)))

    @overload
    def limit(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.limit(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).limit(_float.valueOf(arg0)))

    @overload
    def isOnLine(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isOnLine(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Vector3, self).isOnLine(arg0, _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'float') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(float[])"""
        return 'Vector3'._wrap(super(_Vector3, self).set(arg0))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.math.Vector3(float[])"""
        val = _Vector3(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def dst(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dst(float,float,float,float,float,float)"""
        return float._wrap(_Vector3.dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def unrotate(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.unrotate(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).unrotate(arg0))

    @overload
    def rotateRad(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotateRad(float,float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).rotateRad(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def dst2(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dst2(float,float,float)"""
        return float._wrap(super(_Vector3, self).dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def prj(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.prj(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).prj(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinear(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).isCollinear(arg0))

    @overload
    def scl(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).scl(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotate(float,float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).rotate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setFromSpherical(self, arg0: float, arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setFromSpherical(float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).setFromSpherical(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def slerp(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.slerp(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).slerp(arg0, _float.valueOf(arg1)))

    @overload
    def setLength2(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setLength2(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).setLength2(_float.valueOf(arg0)))

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rotate(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).rotate(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isUnit(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isUnit()"""
        return bool._wrap(super(Vector3, self).isUnit())

    @overload
    def __init__(self, arg0: 'Vector3'):
        """public com.badlogic.gdx.math.Vector3(com.badlogic.gdx.math.Vector3)"""
        val = _Vector3(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Vector3.toString()"""
        return str._wrap(super(Vector3, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def traMul(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.traMul(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).traMul(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def isZero(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isZero(float)"""
        return bool._wrap(super(_Vector3, self).isZero(_float.valueOf(arg0)))

    @overload
    def fromString(self, arg0: str) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.fromString(java.lang.String)"""
        return 'Vector3'._wrap(super(_Vector3, self).fromString(arg0))

    @overload
    def untransform(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.untransform(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).untransform(arg0))

    @overload
    def epsilonEquals(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).epsilonEquals(arg0))

    @staticmethod
    @overload
    def len2(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.len2(float,float,float)"""
        return float._wrap(_Vector3.len2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def limit2(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.limit2(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).limit2(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Vector2', arg1: float):
        """public com.badlogic.gdx.math.Vector3(com.badlogic.gdx.math.Vector2,float)"""
        val = _Vector3(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).sub(_float.valueOf(arg0)))

    @overload
    def mulAdd(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mulAdd(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).mulAdd(arg0, arg1))

    @overload
    def crs(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.crs(float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).crs(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Vector3()"""
        val = _Vector3()
        self.__wrapper = val

    @overload
    def clamp(self, arg0: float, arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.clamp(float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).clamp(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def isCollinearOpposite(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinearOpposite(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Vector3, self).isCollinearOpposite(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.Vector3.len()"""
        return float._wrap(super(Vector3, self).len())

    @overload
    def sub(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).sub(arg0))

    @overload
    def isPerpendicular(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isPerpendicular(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).isPerpendicular(arg0))

    @overload
    def hasSameDirection(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.hasSameDirection(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).hasSameDirection(arg0))

    @overload
    def traMul(self, arg0: 'Matrix3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.traMul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector3'._wrap(super(_Vector3, self).traMul(arg0))

    @overload
    def isOnLine(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isOnLine(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).isOnLine(arg0))

    @overload
    def isPerpendicular(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isPerpendicular(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Vector3, self).isPerpendicular(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def setToRandomDirection(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setToRandomDirection()"""
        return 'Vector3'._wrap(super(Vector3, self).setToRandomDirection())

    @staticmethod
    @overload
    def len(arg0: float, arg1: float, arg2: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.len(float,float,float)"""
        return float._wrap(_Vector3.len(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def interpolate(self, arg0: 'Vector3', arg1: float, arg2: 'Interpolation') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.interpolate(com.badlogic.gdx.math.Vector3,float,com.badlogic.gdx.math.Interpolation)"""
        return 'Vector3'._wrap(super(_Vector3, self).interpolate(arg0, _float.valueOf(arg1), arg2))

    @overload
    def mulAdd(self, arg0: 'Vector3', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mulAdd(com.badlogic.gdx.math.Vector3,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).mulAdd(arg0, _float.valueOf(arg1)))

    @overload
    def idt(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.idt(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).idt(arg0))

    @overload
    def isCollinear(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinear(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Vector3, self).isCollinear(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def dst2(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dst2(float,float,float,float,float,float)"""
        return float._wrap(_Vector3.dst2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def mul(self, arg0: 'Matrix3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Matrix3)"""
        return 'Vector3'._wrap(super(_Vector3, self).mul(arg0))

    @overload
    def hasOppositeDirection(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.hasOppositeDirection(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).hasOppositeDirection(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.math.Vector3(float,float,float)"""
        val = _Vector3(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def mul4x3(self, arg0: 'float') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul4x3(float[])"""
        return 'Vector3'._wrap(super(_Vector3, self).mul4x3(arg0))

    @overload
    def rot(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.rot(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).rot(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Vector3.hashCode()"""
        return int._wrap(super(Vector3, self).hashCode())

    @overload
    def add(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.add(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).add(_float.valueOf(arg0)))

    @overload
    def scl(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).scl(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).set(arg0))

    @staticmethod
    @overload
    def dot(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> float:
        """public static float com.badlogic.gdx.math.Vector3.dot(float,float,float,float,float,float)"""
        return float._wrap(_Vector3.dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def nor(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.nor()"""
        return 'Vector3'._wrap(super(Vector3, self).nor())

    @override
    @overload
    def setZero(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setZero()"""
        return 'Vector3'._wrap(super(Vector3, self).setZero())

    @overload
    def mul(self, arg0: 'Quaternion') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Quaternion)"""
        return 'Vector3'._wrap(super(_Vector3, self).mul(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Vector3()"""
        val = _Vector3()
        self.__wrapper = val

    @overload
    def epsilonEquals(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Vector3, self).epsilonEquals(arg0, _float.valueOf(arg1)))

    @overload
    def dst(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dst(float,float,float)"""
        return float._wrap(super(_Vector3, self).dst(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def cpy(self) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.cpy()"""
        return 'Vector3'._wrap(super(Vector3, self).cpy())

    @overload
    def set(self, arg0: 'Vector2', arg1: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.set(com.badlogic.gdx.math.Vector2,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).set(arg0, _float.valueOf(arg1)))

    @overload
    def dot(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Vector3.dot(float,float,float)"""
        return float._wrap(super(_Vector3, self).dot(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dst2(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dst2(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Vector3, self).dst2(arg0))

    @overload
    def isUnit(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isUnit(float)"""
        return bool._wrap(super(_Vector3, self).isUnit(_float.valueOf(arg0)))

    @overload
    def dot(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dot(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Vector3, self).dot(arg0))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.sub(float,float,float)"""
        return 'Vector3'._wrap(super(_Vector3, self).sub(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Vector3'._wrap(super(_Vector3, self).mul(arg0))

    @overload
    def dst(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.math.Vector3.dst(com.badlogic.gdx.math.Vector3)"""
        return float._wrap(super(_Vector3, self).dst(arg0))

    @overload
    def setLength(self, arg0: float) -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.setLength(float)"""
        return 'Vector3'._wrap(super(_Vector3, self).setLength(_float.valueOf(arg0)))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(float,float,float)"""
        return bool._wrap(super(_Vector3, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def crs(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.crs(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).crs(arg0))

    @override
    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isZero()"""
        return bool._wrap(super(Vector3, self).isZero())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def scl(self, arg0: 'Vector3') -> 'Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.Vector3.scl(com.badlogic.gdx.math.Vector3)"""
        return 'Vector3'._wrap(super(_Vector3, self).scl(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.equals(java.lang.Object)"""
        return bool._wrap(super(_Vector3, self).equals(arg0))

    @overload
    def epsilonEquals(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.epsilonEquals(float,float,float,float)"""
        return bool._wrap(super(_Vector3, self).epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.Vector3.len2()"""
        return float._wrap(super(Vector3, self).len2())

    @overload
    def isCollinearOpposite(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Vector3.isCollinearOpposite(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Vector3, self).isCollinearOpposite(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Elastic
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.math.Interpolation as _Interpolation_Elastic
_Elastic = _Interpolation_Elastic.Elastic
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Elastic():
    """com.badlogic.gdx.math.Interpolation.Elastic"""
 
    @staticmethod
    def _wrap(java_value: _Elastic) -> 'Elastic':
        return Elastic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Elastic):
        """
        Dynamic initializer for Elastic.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Elastic__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Elastic__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Elastic.apply(float)"""
        return float._wrap(super(_Elastic, self).apply(_float.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public com.badlogic.gdx.math.Interpolation$Elastic(float,float,int,float)"""
        val = _Elastic(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))
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
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$Pow
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.math.Interpolation as _Interpolation_Pow
_Pow = _Interpolation_Pow.Pow
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pow():
    """com.badlogic.gdx.math.Interpolation.Pow"""
 
    @staticmethod
    def _wrap(java_value: _Pow) -> 'Pow':
        return Pow(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pow):
        """
        Dynamic initializer for Pow.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pow__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pow__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$Pow(int)"""
        val = _Pow(_int.valueOf(arg0))
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

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$Pow.apply(float)"""
        return float._wrap(super(_Pow, self).apply(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Frustum
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Frustum as _Frustum
_Frustum = _Frustum
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Frustum():
    """com.badlogic.gdx.math.Frustum"""
 
    @staticmethod
    def _wrap(java_value: _Frustum) -> 'Frustum':
        return Frustum(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Frustum):
        """
        Dynamic initializer for Frustum.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Frustum__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Frustum__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sphereInFrustum(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustum(float,float,float,float)"""
        return bool._wrap(super(_Frustum, self).sphereInFrustum(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def pointInFrustum(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.pointInFrustum(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Frustum, self).pointInFrustum(arg0))

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
    def boundsInFrustum(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(float,float,float,float,float,float)"""
        return bool._wrap(super(_Frustum, self).boundsInFrustum(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

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

    @overload
    def boundsInFrustum(self, arg0: 'Vector3', arg1: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_Frustum, self).boundsInFrustum(arg0, arg1))

    @overload
    def sphereInFrustumWithoutNearFar(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustumWithoutNearFar(float,float,float,float)"""
        return bool._wrap(super(_Frustum, self).sphereInFrustumWithoutNearFar(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def update(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.Frustum.update(com.badlogic.gdx.math.Matrix4)"""
        super(_Frustum, self).update(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def boundsInFrustum(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(super(_Frustum, self).boundsInFrustum(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.Frustum()"""
        val = _Frustum()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sphereInFrustumWithoutNearFar(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustumWithoutNearFar(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Frustum, self).sphereInFrustumWithoutNearFar(arg0, _float.valueOf(arg1)))

    @overload
    def pointInFrustum(self, arg0: float, arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.pointInFrustum(float,float,float)"""
        return bool._wrap(super(_Frustum, self).pointInFrustum(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def boundsInFrustum(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.boundsInFrustum(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(super(_Frustum, self).boundsInFrustum(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.Frustum()"""
        val = _Frustum()
        self.__wrapper = val

    @overload
    def sphereInFrustum(self, arg0: 'Vector3', arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Frustum.sphereInFrustum(com.badlogic.gdx.math.Vector3,float)"""
        return bool._wrap(super(_Frustum, self).sphereInFrustum(arg0, _float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Interpolation$BounceIn
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.Interpolation as _Interpolation_BounceIn
_BounceIn = _Interpolation_BounceIn.BounceIn
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BounceIn():
    """com.badlogic.gdx.math.Interpolation.BounceIn"""
 
    @staticmethod
    def _wrap(java_value: _BounceIn) -> 'BounceIn':
        return BounceIn(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BounceIn):
        """
        Dynamic initializer for BounceIn.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BounceIn__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BounceIn__wrapper":
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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.math.Interpolation$BounceIn(int)"""
        val = _BounceIn(_int.valueOf(arg0))
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'float', arg1: 'float'):
        """public com.badlogic.gdx.math.Interpolation$BounceIn(float[],float[])"""
        val = _BounceIn(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def apply(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation.apply(float,float,float)"""
        return float._wrap(super(_Interpolation, self).apply(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def apply(self, arg0: float) -> float:
        """public float com.badlogic.gdx.math.Interpolation$BounceIn.apply(float)"""
        return float._wrap(super(_BounceIn, self).apply(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.Octree$OctreeNode
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
import com.badlogic.gdx.math.Octree as _Octree_OctreeNode
_OctreeNode = _Octree_OctreeNode.OctreeNode
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OctreeNode():
    """com.badlogic.gdx.math.Octree.OctreeNode"""
 
    @staticmethod
    def _wrap(java_value: _OctreeNode) -> 'OctreeNode':
        return OctreeNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OctreeNode):
        """
        Dynamic initializer for OctreeNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OctreeNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OctreeNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())