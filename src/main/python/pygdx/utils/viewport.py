from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.viewport.FitViewport as __FitViewport
__FitViewport = __FitViewport
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.utils.viewport.ScalingViewport as __ScalingViewport
__ScalingViewport = __ScalingViewport
from builtins import float
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class FitViewport():
    """com.badlogic.gdx.utils.viewport.FitViewport"""
 
    @staticmethod
    def __wrap(java_value: __FitViewport) -> 'FitViewport':
        return FitViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FitViewport):
        """
        Dynamic initializer for FitViewport.
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
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __FitViewport(__float.valueOf(arg0), __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(__ScalingViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float)"""
        val = __FitViewport(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ScalingViewport, self).setScaling(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'.__wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FitViewport
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.viewport.FitViewport as __FitViewport
__FitViewport = __FitViewport
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.utils.viewport.ScalingViewport as __ScalingViewport
__ScalingViewport = __ScalingViewport
from builtins import float
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class FitViewport():
    """com.badlogic.gdx.utils.viewport.FitViewport"""
 
    @staticmethod
    def __wrap(java_value: __FitViewport) -> 'FitViewport':
        return FitViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FitViewport):
        """
        Dynamic initializer for FitViewport.
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
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __FitViewport(__float.valueOf(arg0), __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(__ScalingViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FitViewport(float,float)"""
        val = __FitViewport(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ScalingViewport, self).setScaling(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'.__wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FitViewport 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ExtendViewport
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
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
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.viewport.ExtendViewport as __ExtendViewport
__ExtendViewport = __ExtendViewport
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ExtendViewport():
    """com.badlogic.gdx.utils.viewport.ExtendViewport"""
 
    @staticmethod
    def __wrap(java_value: __ExtendViewport) -> 'ExtendViewport':
        return ExtendViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExtendViewport):
        """
        Dynamic initializer for ExtendViewport.
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
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @overload
    def setMinWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMinWorldHeight(float)"""
        super(__ExtendViewport, self).setMinWorldHeight(__float.valueOf(arg0))

    @overload
    def setMinWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMinWorldWidth(float)"""
        super(__ExtendViewport, self).setMinWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def getMinWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMinWorldWidth()"""
        return float.__wrap(super(ExtendViewport, self).getMinWorldWidth())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def getMaxWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMaxWorldWidth()"""
        return float.__wrap(super(ExtendViewport, self).getMaxWorldWidth())

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getMaxWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMaxWorldHeight()"""
        return float.__wrap(super(ExtendViewport, self).getMaxWorldHeight())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float)"""
        val = __ExtendViewport(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __ExtendViewport(__float.valueOf(arg0), __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @overload
    def getMinWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ExtendViewport.getMinWorldHeight()"""
        return float.__wrap(super(ExtendViewport, self).getMinWorldHeight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ExtendViewport, self).setScaling(arg0)

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @overload
    def setMaxWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMaxWorldWidth(float)"""
        super(__ExtendViewport, self).setMaxWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @overload
    def setMaxWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.setMaxWorldHeight(float)"""
        super(__ExtendViewport, self).setMaxWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __ExtendViewport(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.utils.viewport.ExtendViewport(float,float,float,float)"""
        val = __ExtendViewport(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ExtendViewport.update(int,int,boolean)"""
        super(__ExtendViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.StretchViewport
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.utils.viewport.ScalingViewport as __ScalingViewport
__ScalingViewport = __ScalingViewport
from builtins import float
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.viewport.StretchViewport as __StretchViewport
__StretchViewport = __StretchViewport
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class StretchViewport():
    """com.badlogic.gdx.utils.viewport.StretchViewport"""
 
    @staticmethod
    def __wrap(java_value: __StretchViewport) -> 'StretchViewport':
        return StretchViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StretchViewport):
        """
        Dynamic initializer for StretchViewport.
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
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.StretchViewport(float,float)"""
        val = __StretchViewport(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(__ScalingViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ScalingViewport, self).setScaling(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.StretchViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __StretchViewport(__float.valueOf(arg0), __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'.__wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply() 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ScalingViewport
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.utils.viewport.ScalingViewport as __ScalingViewport
__ScalingViewport = __ScalingViewport
from builtins import float
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ScalingViewport():
    """com.badlogic.gdx.utils.viewport.ScalingViewport"""
 
    @staticmethod
    def __wrap(java_value: __ScalingViewport) -> 'ScalingViewport':
        return ScalingViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScalingViewport):
        """
        Dynamic initializer for ScalingViewport.
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
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(__ScalingViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'.__wrap(super(ScalingViewport, self).getScaling())

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Scaling', arg1: float, arg2: float, arg3: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ScalingViewport(com.badlogic.gdx.utils.Scaling,float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __ScalingViewport(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ScalingViewport, self).setScaling(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Scaling', arg1: float, arg2: float):
        """public com.badlogic.gdx.utils.viewport.ScalingViewport(com.badlogic.gdx.utils.Scaling,float,float)"""
        val = __ScalingViewport(arg0, __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply() 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.ScreenViewport
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.viewport.ScreenViewport as __ScreenViewport
__ScreenViewport = __ScreenViewport
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ScreenViewport():
    """com.badlogic.gdx.utils.viewport.ScreenViewport"""
 
    @staticmethod
    def __wrap(java_value: __ScreenViewport) -> 'ScreenViewport':
        return ScreenViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScreenViewport):
        """
        Dynamic initializer for ScreenViewport.
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
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def getUnitsPerPixel(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.ScreenViewport.getUnitsPerPixel()"""
        return float.__wrap(super(ScreenViewport, self).getUnitsPerPixel())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @overload
    def setUnitsPerPixel(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.ScreenViewport.setUnitsPerPixel(float)"""
        super(__ScreenViewport, self).setUnitsPerPixel(__float.valueOf(arg0))

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScreenViewport.update(int,int,boolean)"""
        super(__ScreenViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport()"""
        val = __ScreenViewport()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport()"""
        val = __ScreenViewport()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.ScreenViewport(com.badlogic.gdx.graphics.Camera)"""
        val = __ScreenViewport(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.FillViewport
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.utils.viewport.FillViewport as __FillViewport
__FillViewport = __FillViewport
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.utils.viewport.ScalingViewport as __ScalingViewport
__ScalingViewport = __ScalingViewport
from builtins import float
import com.badlogic.gdx.utils.Scaling as __Scaling
__Scaling = __Scaling
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class FillViewport():
    """com.badlogic.gdx.utils.viewport.FillViewport"""
 
    @staticmethod
    def __wrap(java_value: __FillViewport) -> 'FillViewport':
        return FillViewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FillViewport):
        """
        Dynamic initializer for FillViewport.
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
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @override
    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @override
    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @override
    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @override
    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @override
    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @override
    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.update(int,int,boolean)"""
        super(__ScalingViewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @override
    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: 'Camera'):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float,com.badlogic.gdx.graphics.Camera)"""
        val = __FillViewport(__float.valueOf(arg0), __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.utils.viewport.FillViewport(float,float)"""
        val = __FillViewport(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setScaling(self, arg0: 'Scaling'):
        """public void com.badlogic.gdx.utils.viewport.ScalingViewport.setScaling(com.badlogic.gdx.utils.Scaling)"""
        super(__ScalingViewport, self).setScaling(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))

    @override
    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @override
    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

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
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @override
    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @override
    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @override
    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @override
    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getScaling(self) -> 'utils.Scaling':
        """public com.badlogic.gdx.utils.Scaling com.badlogic.gdx.utils.viewport.ScalingViewport.getScaling()"""
        return 'utils.Scaling'.__wrap(super(ScalingViewport, self).getScaling())

    @override
    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply() 
 
 
# CLASS: com.badlogic.gdx.utils.viewport.Viewport
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
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
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Viewport(ABC):
    """com.badlogic.gdx.utils.viewport.Viewport"""
 
    @staticmethod
    def __wrap(java_value: __Viewport) -> 'Viewport':
        return Viewport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Viewport):
        """
        Dynamic initializer for Viewport.
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
    def project(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).project(arg0))

    @overload
    def setWorldHeight(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldHeight(float)"""
        super(__Viewport, self).setWorldHeight(__float.valueOf(arg0))

    @overload
    def setScreenWidth(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenWidth(int)"""
        super(__Viewport, self).setScreenWidth(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.viewport.Viewport()"""
        val = __Viewport()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).project(arg0))

    @overload
    def getWorldWidth(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldWidth()"""
        return float.__wrap(super(Viewport, self).getWorldWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRightGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterWidth()"""
        return int.__wrap(super(Viewport, self).getRightGutterWidth())

    @overload
    def setWorldWidth(self, arg0: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldWidth(float)"""
        super(__Viewport, self).setWorldWidth(__float.valueOf(arg0))

    @overload
    def update(self, arg0: int, arg1: int):
        """public final void com.badlogic.gdx.utils.viewport.Viewport.update(int,int)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).toScreenCoordinates(arg0, arg1))

    @overload
    def setScreenX(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenX(int)"""
        super(__Viewport, self).setScreenX(__int.valueOf(arg0))

    @overload
    def getTopGutterY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterY()"""
        return int.__wrap(super(Viewport, self).getTopGutterY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.utils.viewport.Viewport.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Viewport, self).getCamera())

    @overload
    def update(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.update(int,int,boolean)"""
        super(__Viewport, self).update(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def getScreenY(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenY()"""
        return int.__wrap(super(Viewport, self).getScreenY())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.viewport.Viewport()"""
        val = __Viewport()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.utils.viewport.Viewport.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Viewport, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def getWorldHeight(self) -> float:
        """public float com.badlogic.gdx.utils.viewport.Viewport.getWorldHeight()"""
        return float.__wrap(super(Viewport, self).getWorldHeight())

    @overload
    def getRightGutterX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getRightGutterX()"""
        return int.__wrap(super(Viewport, self).getRightGutterX())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getScreenWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenWidth()"""
        return int.__wrap(super(Viewport, self).getScreenWidth())

    @overload
    def setScreenSize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenSize(int,int)"""
        super(__Viewport, self).setScreenSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getScreenX(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenX()"""
        return int.__wrap(super(Viewport, self).getScreenX())

    @overload
    def setScreenBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenBounds(int,int,int,int)"""
        super(__Viewport, self).setScreenBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def apply(self, arg0: bool):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply(boolean)"""
        super(__Viewport, self).apply(__boolean.valueOf(arg0))

    @overload
    def getBottomGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getBottomGutterHeight()"""
        return int.__wrap(super(Viewport, self).getBottomGutterHeight())

    @overload
    def setWorldSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setWorldSize(float,float)"""
        super(__Viewport, self).setWorldSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def apply(self):
        """public void com.badlogic.gdx.utils.viewport.Viewport.apply()"""
        super(Viewport, self).apply()

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__Viewport, self).setCamera(arg0)

    @overload
    def setScreenHeight(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenHeight(int)"""
        super(__Viewport, self).setScreenHeight(__int.valueOf(arg0))

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
    def getScreenHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getScreenHeight()"""
        return int.__wrap(super(Viewport, self).getScreenHeight())

    @overload
    def getLeftGutterWidth(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getLeftGutterWidth()"""
        return int.__wrap(super(Viewport, self).getLeftGutterWidth())

    @overload
    def unproject(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.utils.viewport.Viewport.unproject(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Viewport, self).unproject(arg0))

    @overload
    def setScreenPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenPosition(int,int)"""
        super(__Viewport, self).setScreenPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getTopGutterHeight(self) -> int:
        """public int com.badlogic.gdx.utils.viewport.Viewport.getTopGutterHeight()"""
        return int.__wrap(super(Viewport, self).getTopGutterHeight())

    @overload
    def calculateScissors(self, arg0: 'Matrix4', arg1: 'Rectangle', arg2: 'Rectangle'):
        """public void com.badlogic.gdx.utils.viewport.Viewport.calculateScissors(com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Viewport, self).calculateScissors(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setScreenY(self, arg0: int):
        """public void com.badlogic.gdx.utils.viewport.Viewport.setScreenY(int)"""
        super(__Viewport, self).setScreenY(__int.valueOf(arg0))