from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.Scaling as _Scaling
_Scaling = _Scaling
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.utils.viewport.ScalingViewport as _ScalingViewport
_ScalingViewport = _ScalingViewport
from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.utils.viewport.FillViewport as _FillViewport
_FillViewport = _FillViewport
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FillViewport():
    """com.badlogic.gdx.utils.viewport.FillViewport"""
 
    @staticmethod
    def _wrap(java_value: _FillViewport) -> 'FillViewport':
        return FillViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FillViewport):
        """
        Dynamic initializer for FillViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FillViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FillViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'._wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _FillViewport(_float.valueOf(arg0), _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(_ScalingViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float)"""
        val = _FillViewport(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FillViewport
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.Scaling as _Scaling
_Scaling = _Scaling
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.utils.viewport.ScalingViewport as _ScalingViewport
_ScalingViewport = _ScalingViewport
from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.utils.viewport.FillViewport as _FillViewport
_FillViewport = _FillViewport
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FillViewport():
    """com.badlogic.gdx.utils.viewport.FillViewport"""
 
    @staticmethod
    def _wrap(java_value: _FillViewport) -> 'FillViewport':
        return FillViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FillViewport):
        """
        Dynamic initializer for FillViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FillViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FillViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'._wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _FillViewport(_float.valueOf(arg0), _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(_ScalingViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float)"""
        val = _FillViewport(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FillViewport 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.Viewport
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
from builtins import float
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Viewport():
    """com.badlogic.gdx.utils.viewport.Viewport"""
 
    @staticmethod
    def _wrap(java_value: _Viewport) -> 'Viewport':
        return Viewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Viewport):
        """
        Dynamic initializer for Viewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Viewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Viewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.update(int,int,boolean)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.viewport.Viewport()"""
        val = _Viewport()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.viewport.Viewport()"""
        val = _Viewport()
        self.__wrapper = val

    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FitViewport
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.Scaling as _Scaling
_Scaling = _Scaling
import java.lang.Boolean as _boolean
import com.badlogic.gdx.utils.viewport.FitViewport as _FitViewport
_FitViewport = _FitViewport
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.utils.viewport.ScalingViewport as _ScalingViewport
_ScalingViewport = _ScalingViewport
from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FitViewport():
    """com.badlogic.gdx.utils.viewport.FitViewport"""
 
    @staticmethod
    def _wrap(java_value: _FitViewport) -> 'FitViewport':
        return FitViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FitViewport):
        """
        Dynamic initializer for FitViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FitViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FitViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _FitViewport(_float.valueOf(arg0), _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'._wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(_ScalingViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float)"""
        val = _FitViewport(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.StretchViewport
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.Scaling as _Scaling
_Scaling = _Scaling
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.utils.viewport.ScalingViewport as _ScalingViewport
_ScalingViewport = _ScalingViewport
from builtins import bool
import com.badlogic.gdx.utils.viewport.StretchViewport as _StretchViewport
_StretchViewport = _StretchViewport
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StretchViewport():
    """com.badlogic.gdx.utils.viewport.StretchViewport"""
 
    @staticmethod
    def _wrap(java_value: _StretchViewport) -> 'StretchViewport':
        return StretchViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StretchViewport):
        """
        Dynamic initializer for StretchViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StretchViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StretchViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'._wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.StretchViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _StretchViewport(_float.valueOf(arg0), _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.StretchViewport(float,float)"""
        val = _StretchViewport(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(_ScalingViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ExtendViewport
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
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
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
from builtins import float
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import com.badlogic.gdx.utils.viewport.ExtendViewport as _ExtendViewport
_ExtendViewport = _ExtendViewport
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExtendViewport():
    """com.badlogic.gdx.utils.viewport.ExtendViewport"""
 
    @staticmethod
    def _wrap(java_value: _ExtendViewport) -> 'ExtendViewport':
        return ExtendViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtendViewport):
        """
        Dynamic initializer for ExtendViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtendViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtendViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @overload
    def getMaxWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMaxWorldHeight()"""
        return float._wrap(super(ExtendViewport, self).getMaxWorldHeight())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _ExtendViewport(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.update(int,int,boolean)"""
        super(_ExtendViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ExtendViewport, self).setScaling(arg0)

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @overload
    def getMinWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMinWorldHeight()"""
        return float._wrap(super(ExtendViewport, self).getMinWorldHeight())

    @overload
    def setMaxWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMaxWorldWidth(float)"""
        super(_ExtendViewport, self).setMaxWorldWidth(_float.valueOf(arg0))

    @overload
    def setMinWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMinWorldWidth(float)"""
        super(_ExtendViewport, self).setMinWorldWidth(_float.valueOf(arg0))

    @overload
    def getMinWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMinWorldWidth()"""
        return float._wrap(super(ExtendViewport, self).getMinWorldWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @overload
    def setMaxWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMaxWorldHeight(float)"""
        super(_ExtendViewport, self).setMaxWorldHeight(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float)"""
        val = _ExtendViewport(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMaxWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMaxWorldWidth()"""
        return float._wrap(super(ExtendViewport, self).getMaxWorldWidth())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,float,float)"""
        val = _ExtendViewport(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @overload
    def setMinWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMinWorldHeight(float)"""
        super(_ExtendViewport, self).setMinWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _ExtendViewport(_float.valueOf(arg0), _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ScalingViewport
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.Scaling as _Scaling
_Scaling = _Scaling
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.utils.viewport.ScalingViewport as _ScalingViewport
_ScalingViewport = _ScalingViewport
from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScalingViewport():
    """com.badlogic.gdx.utils.viewport.ScalingViewport"""
 
    @staticmethod
    def _wrap(java_value: _ScalingViewport) -> 'ScalingViewport':
        return ScalingViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScalingViewport):
        """
        Dynamic initializer for ScalingViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScalingViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScalingViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(_ScalingViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @overload
    def __init__(self, arg0: 'Scaling', arg1: float, arg2: float):
        """public com.badlogic.gdx.utils.viewport.ScalingViewport(com.badlogic.gdx.utils.Scaling,float,float)"""
        val = _ScalingViewport(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'._wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Scaling', arg1: float, arg2: float, arg3: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ScalingViewport(com.badlogic.gdx.utils.Scaling,float,float,com.badlogic.gdx.graphics.Camera)"""
        val = _ScalingViewport(arg0, _float.valueOf(arg1), _float.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(_ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ScreenViewport
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
from builtins import float
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.utils.viewport.ScreenViewport as _ScreenViewport
_ScreenViewport = _ScreenViewport
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScreenViewport():
    """com.badlogic.gdx.utils.viewport.ScreenViewport"""
 
    @staticmethod
    def _wrap(java_value: _ScreenViewport) -> 'ScreenViewport':
        return ScreenViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScreenViewport):
        """
        Dynamic initializer for ScreenViewport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScreenViewport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScreenViewport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float._wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int._wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int._wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(_Viewport, self).setScreenWidth(_int.valueOf(arg0))

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'._wrap(super(_Viewport, self).getPickRay(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int._wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(_Viewport, self).setWorldHeight(_float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int._wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(_Viewport, self).setScreenBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int._wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScreenViewport.update(int,int,boolean)"""
        super(_ScreenViewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setUnitsPerPixel(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ScreenViewport.setUnitsPerPixel(float)"""
        super(_ScreenViewport, self).setUnitsPerPixel(_float.valueOf(arg0))

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float._wrap(super(Viewport, self).getWorldWidth())

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport(com.badlogic.gdx.graphics.Camera)"""
        val = _ScreenViewport(arg0)
        self.__wrapper = val

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Viewport, self).calculateScissors(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport()"""
        val = _ScreenViewport()
        self.__wrapper = val

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(_Viewport, self).setScreenY(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(_Viewport, self).update(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(_Viewport, self).setScreenSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int._wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(_Viewport, self).apply(_boolean.valueOf(arg0))

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(_Viewport, self).setWorldWidth(_float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int._wrap(super(Viewport, self).getBottomGutterHeight())

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int._wrap(super(Viewport, self).getScreenX())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).unproject(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int._wrap(super(Viewport, self).getTopGutterHeight())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport()"""
        val = _ScreenViewport()
        self.__wrapper = val

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(_Viewport, self).setScreenHeight(_int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(_Viewport, self).setWorldSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getUnitsPerPixel(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ScreenViewport.getUnitsPerPixel()"""
        return float._wrap(super(ScreenViewport, self).getUnitsPerPixel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'._wrap(super(Viewport, self).getCamera())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_Viewport, self).setCamera(arg0)

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int._wrap(super(Viewport, self).getScreenWidth())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Viewport, self).project(arg0))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(_Viewport, self).setScreenPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(_Viewport, self).setScreenX(_int.valueOf(arg0))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Viewport, self).project(arg0))