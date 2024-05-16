from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import box2dLight.DirectionalLight as _DirectionalLight
_DirectionalLight = _DirectionalLight
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectionalLight():
    """box2dLight.DirectionalLight"""
 
    @staticmethod
    def _wrap(java_value: _DirectionalLight) -> 'DirectionalLight':
        return DirectionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectionalLight):
        """
        Dynamic initializer for DirectionalLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectionalLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectionalLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def setIgnoreBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.setIgnoreBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_DirectionalLight, self).setIgnoreBody(arg0)

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.DirectionalLight.getY()"""
        return float._wrap(super(DirectionalLight, self).getY())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

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
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.DirectionalLight.setPosition(float,float)"""
        super(_DirectionalLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float):
        """public box2dLight.DirectionalLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float)"""
        val = _DirectionalLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.DirectionalLight.contains(float,float)"""
        return bool._wrap(super(_DirectionalLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.DirectionalLight.getBody()"""
        return 'box2d.Body'._wrap(super(DirectionalLight, self).getBody())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_DirectionalLight, self).attachToBody(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.DirectionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_DirectionalLight, self).setPosition(arg0)

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'._wrap(super(Light, self).getPosition())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.DirectionalLight.getX()"""
        return float._wrap(super(DirectionalLight, self).getX())

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDirection(float)"""
        super(_DirectionalLight, self).setDirection(_float.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.DirectionalLight.getIgnoreAttachedBody()"""
        return bool._wrap(super(DirectionalLight, self).getIgnoreAttachedBody())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDistance(float)"""
        super(_DirectionalLight, self).setDistance(_float.valueOf(arg0))

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.DirectionalLight.setIgnoreAttachedBody(boolean)"""
        super(_DirectionalLight, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: box2dLight.DirectionalLight
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
import box2dLight.DirectionalLight as _DirectionalLight
_DirectionalLight = _DirectionalLight
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectionalLight():
    """box2dLight.DirectionalLight"""
 
    @staticmethod
    def _wrap(java_value: _DirectionalLight) -> 'DirectionalLight':
        return DirectionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectionalLight):
        """
        Dynamic initializer for DirectionalLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectionalLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectionalLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def setIgnoreBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.setIgnoreBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_DirectionalLight, self).setIgnoreBody(arg0)

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.DirectionalLight.getY()"""
        return float._wrap(super(DirectionalLight, self).getY())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

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
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.DirectionalLight.setPosition(float,float)"""
        super(_DirectionalLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float):
        """public box2dLight.DirectionalLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float)"""
        val = _DirectionalLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.DirectionalLight.contains(float,float)"""
        return bool._wrap(super(_DirectionalLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.DirectionalLight.getBody()"""
        return 'box2d.Body'._wrap(super(DirectionalLight, self).getBody())

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.DirectionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_DirectionalLight, self).attachToBody(arg0)

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.DirectionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_DirectionalLight, self).setPosition(arg0)

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'._wrap(super(Light, self).getPosition())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.DirectionalLight.getX()"""
        return float._wrap(super(DirectionalLight, self).getX())

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDirection(float)"""
        super(_DirectionalLight, self).setDirection(_float.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.DirectionalLight.getIgnoreAttachedBody()"""
        return bool._wrap(super(DirectionalLight, self).getIgnoreAttachedBody())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.DirectionalLight.setDistance(float)"""
        super(_DirectionalLight, self).setDistance(_float.valueOf(arg0))

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.DirectionalLight.setIgnoreAttachedBody(boolean)"""
        super(_DirectionalLight, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: box2dLight.DirectionalLight 
 
 
# CLASS: box2dLight.ChainLight
from pyquantum_helper import import_once as _import_once
import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import box2dLight.ChainLight as _ChainLight
_ChainLight = _ChainLight
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChainLight():
    """box2dLight.ChainLight"""
 
    @staticmethod
    def _wrap(java_value: _ChainLight) -> 'ChainLight':
        return ChainLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChainLight):
        """
        Dynamic initializer for ChainLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChainLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChainLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

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
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.ChainLight.getBody()"""
        return 'box2d.Body'._wrap(super(ChainLight, self).getBody())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @overload
    def update(self):
        """public void box2dLight.ChainLight.update()"""
        super(ChainLight, self).update()

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: int, arg5: 'float'):
        """public box2dLight.ChainLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,int,float[])"""
        val = _ChainLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _int.valueOf(arg4), arg5)
        self.__wrapper = val

    @overload
    def debugRender(self, arg0: 'ShapeRenderer'):
        """public void box2dLight.ChainLight.debugRender(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(_ChainLight, self).debugRender(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def updateChain(self):
        """public void box2dLight.ChainLight.updateChain()"""
        super(ChainLight, self).updateChain()

    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.ChainLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_ChainLight, self).attachToBody(arg0)

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.ChainLight.getY()"""
        return float._wrap(super(ChainLight, self).getY())

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.ChainLight.setDirection(float)"""
        super(_ChainLight, self).setDirection(_float.valueOf(arg0))

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'._wrap(super(Light, self).getPosition())

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.ChainLight.getX()"""
        return float._wrap(super(ChainLight, self).getX())

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float):
        """public void box2dLight.ChainLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float)"""
        super(_ChainLight, self).attachToBody(arg0, _float.valueOf(arg1))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: int):
        """public box2dLight.ChainLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,int)"""
        val = _ChainLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _int.valueOf(arg4))
        self.__wrapper = val

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.ChainLight.contains(float,float)"""
        return bool._wrap(super(_ChainLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(_Light, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.ChainLight.setPosition(float,float)"""
        super(_ChainLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool._wrap(super(Light, self).getIgnoreAttachedBody())

    @overload
    def render(self):
        """public void box2dLight.ChainLight.render()"""
        super(ChainLight, self).render()

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.ChainLight.setDistance(float)"""
        super(_ChainLight, self).setDistance(_float.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.ChainLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_ChainLight, self).setPosition(arg0) 
 
 
# CLASS: box2dLight.Spinor
import box2dLight.Spinor as _Spinor
_Spinor = _Spinor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import box2dLight.Spinor as Spinor
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
 
class Spinor():
    """box2dLight.Spinor"""
 
    @staticmethod
    def _wrap(java_value: _Spinor) -> 'Spinor':
        return Spinor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Spinor):
        """
        Dynamic initializer for Spinor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Spinor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Spinor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.add(float)"""
        return 'Spinor'._wrap(super(_Spinor, self).add(_float.valueOf(arg0)))

    @overload
    def slerp(self, arg0: 'Spinor', arg1: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.slerp(box2dLight.Spinor,float)"""
        return 'Spinor'._wrap(super(_Spinor, self).slerp(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: float):
        """public box2dLight.Spinor(float)"""
        val = _Spinor(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def len(self) -> float:
        """public float box2dLight.Spinor.len()"""
        return float._wrap(super(Spinor, self).len())

    @overload
    def nor(self) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.nor()"""
        return 'Spinor'._wrap(super(Spinor, self).nor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.add(box2dLight.Spinor)"""
        return 'Spinor'._wrap(super(_Spinor, self).add(arg0))

    @overload
    def sub(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.sub(box2dLight.Spinor)"""
        return 'Spinor'._wrap(super(_Spinor, self).sub(arg0))

    @overload
    def invert(self) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.invert()"""
        return 'Spinor'._wrap(super(Spinor, self).invert())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def len2(self) -> float:
        """public float box2dLight.Spinor.len2()"""
        return float._wrap(super(Spinor, self).len2())

    @overload
    def angle(self) -> float:
        """public float box2dLight.Spinor.angle()"""
        return float._wrap(super(Spinor, self).angle())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: float, arg1: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(float,float)"""
        return 'Spinor'._wrap(super(_Spinor, self).set(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def mul(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.mul(box2dLight.Spinor)"""
        return 'Spinor'._wrap(super(_Spinor, self).mul(arg0))

    @overload
    def scale(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.scale(float)"""
        return 'Spinor'._wrap(super(_Spinor, self).scale(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(box2dLight.Spinor)"""
        return 'Spinor'._wrap(super(_Spinor, self).set(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public box2dLight.Spinor(float,float)"""
        val = _Spinor(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Spinor'):
        """public box2dLight.Spinor(box2dLight.Spinor)"""
        val = _Spinor(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public box2dLight.Spinor()"""
        val = _Spinor()
        self.__wrapper = val

    @overload
    def sub(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.sub(float)"""
        return 'Spinor'._wrap(super(_Spinor, self).sub(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def lerp(self, arg0: 'Spinor', arg1: float, arg2: 'Spinor') -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.lerp(box2dLight.Spinor,float,box2dLight.Spinor)"""
        return 'Spinor'._wrap(super(_Spinor, self).lerp(arg0, _float.valueOf(arg1), arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: float) -> 'Spinor':
        """public box2dLight.Spinor box2dLight.Spinor.set(float)"""
        return 'Spinor'._wrap(super(_Spinor, self).set(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String box2dLight.Spinor.toString()"""
        return str._wrap(super(Spinor, self).toString())

    @overload
    def __init__(self):
        """public box2dLight.Spinor()"""
        val = _Spinor()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: box2dLight.RayHandler
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import box2dLight.RayHandler as _RayHandler
_RayHandler = _RayHandler
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RayHandler():
    """box2dLight.RayHandler"""
 
    @staticmethod
    def _wrap(java_value: _RayHandler) -> 'RayHandler':
        return RayHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RayHandler):
        """
        Dynamic initializer for RayHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RayHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RayHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'World', arg1: int, arg2: int):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World,int,int)"""
        val = _RayHandler(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def setCombinedMatrix(self, arg0: 'OrthographicCamera'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_RayHandler, self).setCombinedMatrix(arg0)

    @overload
    def getLightMapBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer box2dLight.RayHandler.getLightMapBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(RayHandler, self).getLightMapBuffer())

    @overload
    def useDefaultViewport(self):
        """public void box2dLight.RayHandler.useDefaultViewport()"""
        super(RayHandler, self).useDefaultViewport()

    @overload
    def prepareRender(self):
        """public void box2dLight.RayHandler.prepareRender()"""
        super(RayHandler, self).prepareRender()

    @overload
    def setAmbientLight(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.RayHandler.setAmbientLight(float,float,float,float)"""
        super(_RayHandler, self).setAmbientLight(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4'):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(_RayHandler, self).setCombinedMatrix(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setCulling(self, arg0: bool):
        """public void box2dLight.RayHandler.setCulling(boolean)"""
        super(_RayHandler, self).setCulling(_boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def resizeFBO(self, arg0: int, arg1: int):
        """public void box2dLight.RayHandler.resizeFBO(int,int)"""
        super(_RayHandler, self).resizeFBO(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def render(self):
        """public void box2dLight.RayHandler.render()"""
        super(RayHandler, self).render()

    @overload
    def setBlurNum(self, arg0: int):
        """public void box2dLight.RayHandler.setBlurNum(int)"""
        super(_RayHandler, self).setBlurNum(_int.valueOf(arg0))

    @overload
    def useCustomViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void box2dLight.RayHandler.useCustomViewport(int,int,int,int)"""
        super(_RayHandler, self).useCustomViewport(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setBlur(self, arg0: bool):
        """public void box2dLight.RayHandler.setBlur(boolean)"""
        super(_RayHandler, self).setBlur(_boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.RayHandler.dispose()"""
        super(RayHandler, self).dispose()

    @overload
    def getLightMapTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture box2dLight.RayHandler.getLightMapTexture()"""
        return 'graphics.Texture'._wrap(super(RayHandler, self).getLightMapTexture())

    @overload
    def setAmbientLight(self, arg0: float):
        """public void box2dLight.RayHandler.setAmbientLight(float)"""
        super(_RayHandler, self).setAmbientLight(_float.valueOf(arg0))

    @staticmethod
    @overload
    def setGammaCorrection(arg0: bool):
        """public static void box2dLight.RayHandler.setGammaCorrection(boolean)"""
        _RayHandler.setGammaCorrection(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def removeAll(self):
        """public void box2dLight.RayHandler.removeAll()"""
        super(RayHandler, self).removeAll()

    @overload
    def pointAtShadow(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtShadow(float,float)"""
        return bool._wrap(super(_RayHandler, self).pointAtShadow(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setAmbientLight(self, arg0: 'Color'):
        """public void box2dLight.RayHandler.setAmbientLight(com.badlogic.gdx.graphics.Color)"""
        super(_RayHandler, self).setAmbientLight(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def renderOnly(self):
        """public void box2dLight.RayHandler.renderOnly()"""
        super(RayHandler, self).renderOnly()

    @overload
    def __init__(self, arg0: 'World'):
        """public box2dLight.RayHandler(com.badlogic.gdx.physics.box2d.World)"""
        val = _RayHandler(arg0)
        self.__wrapper = val

    @overload
    def update(self):
        """public void box2dLight.RayHandler.update()"""
        super(RayHandler, self).update()

    @overload
    def setLightShader(self, arg0: 'ShaderProgram'):
        """public void box2dLight.RayHandler.setLightShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(_RayHandler, self).setLightShader(arg0)

    @overload
    def setCombinedMatrix(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void box2dLight.RayHandler.setCombinedMatrix(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_RayHandler, self).setCombinedMatrix(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setLightMapRendering(self, arg0: bool):
        """public void box2dLight.RayHandler.setLightMapRendering(boolean)"""
        super(_RayHandler, self).setLightMapRendering(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def getGammaCorrection() -> bool:
        """public static boolean box2dLight.RayHandler.getGammaCorrection()"""
        return bool._wrap(_RayHandler.getGammaCorrection())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def useDiffuseLight(arg0: bool):
        """public static void box2dLight.RayHandler.useDiffuseLight(boolean)"""
        _RayHandler.useDiffuseLight(_boolean.valueOf(arg0))

    @overload
    def setWorld(self, arg0: 'World'):
        """public void box2dLight.RayHandler.setWorld(com.badlogic.gdx.physics.box2d.World)"""
        super(_RayHandler, self).setWorld(arg0)

    @overload
    def updateAndRender(self):
        """public void box2dLight.RayHandler.updateAndRender()"""
        super(RayHandler, self).updateAndRender()

    @overload
    def pointAtLight(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.RayHandler.pointAtLight(float,float)"""
        return bool._wrap(super(_RayHandler, self).pointAtLight(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setShadows(self, arg0: bool):
        """public void box2dLight.RayHandler.setShadows(boolean)"""
        super(_RayHandler, self).setShadows(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: box2dLight.BlendFunc
import box2dLight.BlendFunc as _BlendFunc
_BlendFunc = _BlendFunc
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlendFunc():
    """box2dLight.BlendFunc"""
 
    @staticmethod
    def _wrap(java_value: _BlendFunc) -> 'BlendFunc':
        return BlendFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlendFunc):
        """
        Dynamic initializer for BlendFunc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlendFunc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlendFunc__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def apply(self):
        """public void box2dLight.BlendFunc.apply()"""
        super(BlendFunc, self).apply()

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
    def set(self, arg0: int, arg1: int):
        """public void box2dLight.BlendFunc.set(int,int)"""
        super(_BlendFunc, self).set(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def __init__(self, arg0: int, arg1: int):
        """public box2dLight.BlendFunc(int,int)"""
        val = _BlendFunc(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def reset(self):
        """public void box2dLight.BlendFunc.reset()"""
        super(BlendFunc, self).reset()

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
 
 
# CLASS: box2dLight.PointLight
from pyquantum_helper import import_once as _import_once
import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import box2dLight.PositionalLight as _PositionalLight
_PositionalLight = _PositionalLight
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import box2dLight.PointLight as _PointLight
_PointLight = _PointLight
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointLight():
    """box2dLight.PointLight"""
 
    @staticmethod
    def _wrap(java_value: _PointLight) -> 'PointLight':
        return PointLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointLight):
        """
        Dynamic initializer for PointLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_PositionalLight, self).attachToBody(arg0)

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float):
        """public box2dLight.PointLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float)"""
        val = _PointLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_PositionalLight, self).setPosition(arg0)

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool._wrap(super(_PositionalLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.PointLight.setDirection(float)"""
        super(_PointLight, self).setDirection(_float.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'._wrap(super(PositionalLight, self).getBody())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'._wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float._wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float._wrap(super(PositionalLight, self).getX())

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int):
        """public box2dLight.PointLight(box2dLight.RayHandler,int)"""
        val = _PointLight(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.PointLight.setDistance(float)"""
        super(_PointLight, self).setDistance(_float.valueOf(arg0))

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(_Light, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(_PositionalLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool._wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @overload
    def update(self):
        """public void box2dLight.PointLight.update()"""
        super(PointLight, self).update() 
 
 
# CLASS: box2dLight.ConeLight
from pyquantum_helper import import_once as _import_once
import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import box2dLight.PositionalLight as _PositionalLight
_PositionalLight = _PositionalLight
import box2dLight.ConeLight as _ConeLight
_ConeLight = _ConeLight
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConeLight():
    """box2dLight.ConeLight"""
 
    @staticmethod
    def _wrap(java_value: _ConeLight) -> 'ConeLight':
        return ConeLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConeLight):
        """
        Dynamic initializer for ConeLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConeLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConeLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_PositionalLight, self).attachToBody(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_PositionalLight, self).setPosition(arg0)

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool._wrap(super(_PositionalLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'._wrap(super(PositionalLight, self).getBody())

    @overload
    def setConeDegree(self, arg0: float):
        """public void box2dLight.ConeLight.setConeDegree(float)"""
        super(_ConeLight, self).setConeDegree(_float.valueOf(arg0))

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setDirection(self, arg0: float):
        """public void box2dLight.ConeLight.setDirection(float)"""
        super(_ConeLight, self).setDirection(_float.valueOf(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @overload
    def update(self):
        """public void box2dLight.ConeLight.update()"""
        super(ConeLight, self).update()

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void box2dLight.ConeLight.setDistance(float)"""
        super(_ConeLight, self).setDistance(_float.valueOf(arg0))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'._wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float._wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float._wrap(super(PositionalLight, self).getX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(_Light, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(_PositionalLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool._wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public box2dLight.ConeLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float,float,float)"""
        val = _ConeLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @overload
    def getConeDegree(self) -> float:
        """public float box2dLight.ConeLight.getConeDegree()"""
        return float._wrap(super(ConeLight, self).getConeDegree()) 
 
 
# CLASS: box2dLight.PositionalLight
from pyquantum_helper import import_once as _import_once
import box2dLight.Light as _Light
_Light = _Light
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.physics.box2d.Body as _Body
_Body = _Body
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import box2dLight.PositionalLight as _PositionalLight
_PositionalLight = _PositionalLight
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PositionalLight():
    """box2dLight.PositionalLight"""
 
    @staticmethod
    def _wrap(java_value: _PositionalLight) -> 'PositionalLight':
        return PositionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PositionalLight):
        """
        Dynamic initializer for PositionalLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PositionalLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PositionalLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def attachToBody(self, arg0: 'Body'):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        super(_PositionalLight, self).attachToBody(arg0)

    @override
    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float, arg5: float, arg6: float):
        """public box2dLight.PositionalLight(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float,float,float)"""
        val = _PositionalLight(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @abstractmethod
    def setDistance(self, arg0: float):
        """public abstract void box2dLight.Light.setDistance(float)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: 'Vector2'):
        """public void box2dLight.PositionalLight.setPosition(com.badlogic.gdx.math.Vector2)"""
        super(_PositionalLight, self).setPosition(arg0)

    @override
    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.PositionalLight.contains(float,float)"""
        return bool._wrap(super(_PositionalLight, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @override
    @overload
    def getBody(self) -> 'box2d.Body':
        """public com.badlogic.gdx.physics.box2d.Body box2dLight.PositionalLight.getBody()"""
        return 'box2d.Body'._wrap(super(PositionalLight, self).getBody())

    @override
    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @override
    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @override
    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @override
    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @override
    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @override
    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(_Light, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void box2dLight.PositionalLight.setPosition(float,float)"""
        super(_PositionalLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def attachToBody(self, arg0: 'Body', arg1: float, arg2: float, arg3: float):
        """public void box2dLight.PositionalLight.attachToBody(com.badlogic.gdx.physics.box2d.Body,float,float,float)"""
        super(_PositionalLight, self).attachToBody(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

    @override
    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @abstractmethod
    def setDirection(self, arg0: float):
        """public abstract void box2dLight.Light.setDirection(float)"""
        pass

    @override
    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @override
    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool._wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.PositionalLight.getPosition()"""
        return 'math.Vector2'._wrap(super(PositionalLight, self).getPosition())

    @override
    @overload
    def getY(self) -> float:
        """public float box2dLight.PositionalLight.getY()"""
        return float._wrap(super(PositionalLight, self).getY())

    @override
    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float box2dLight.PositionalLight.getX()"""
        return float._wrap(super(PositionalLight, self).getX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: box2dLight.Light
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
from pyquantum_helper import override
import box2dLight.Light as _Light
_Light = _Light
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = _import_once("pygdx.physics.box2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import box2dLight.RayHandler as RayHandler
import java.lang.Short as _short
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Light():
    """box2dLight.Light"""
 
    @staticmethod
    def _wrap(java_value: _Light) -> 'Light':
        return Light(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Light):
        """
        Dynamic initializer for Light.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Light__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Light__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getY(self, ):
        """public abstract float box2dLight.Light.getY()"""
        pass

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean box2dLight.Light.contains(float,float)"""
        return bool._wrap(super(_Light, self).contains(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setSoftnessLength(self, arg0: float):
        """public void box2dLight.Light.setSoftnessLength(float)"""
        super(_Light, self).setSoftnessLength(_float.valueOf(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color box2dLight.Light.getColor()"""
        return 'graphics.Color'._wrap(super(Light, self).getColor())

    @abstractmethod
    def setDistance(self, arg0: float):
        """public abstract void box2dLight.Light.setDistance(float)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: bool):
        """public void box2dLight.Light.remove(boolean)"""
        super(_Light, self).remove(_boolean.valueOf(arg0))

    @overload
    def setStaticLight(self, arg0: bool):
        """public void box2dLight.Light.setStaticLight(boolean)"""
        super(_Light, self).setStaticLight(_boolean.valueOf(arg0))

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
    def setContactFilter(self, arg0: int, arg1: int, arg2: int):
        """public void box2dLight.Light.setContactFilter(short,short,short)"""
        super(_Light, self).setContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @overload
    def isXray(self) -> bool:
        """public boolean box2dLight.Light.isXray()"""
        return bool._wrap(super(Light, self).isXray())

    @overload
    def __init__(self, arg0: 'RayHandler', arg1: int, arg2: 'Color', arg3: float, arg4: float):
        """public box2dLight.Light(box2dLight.RayHandler,int,com.badlogic.gdx.graphics.Color,float,float)"""
        val = _Light(arg0, _int.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4))
        self.__wrapper = val

    @overload
    def getPosition(self) -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 box2dLight.Light.getPosition()"""
        return 'math.Vector2'._wrap(super(Light, self).getPosition())

    @overload
    def setIgnoreAttachedBody(self, arg0: bool):
        """public void box2dLight.Light.setIgnoreAttachedBody(boolean)"""
        super(_Light, self).setIgnoreAttachedBody(_boolean.valueOf(arg0))

    @overload
    def setXray(self, arg0: bool):
        """public void box2dLight.Light.setXray(boolean)"""
        super(_Light, self).setXray(_boolean.valueOf(arg0))

    @overload
    def getRayNum(self) -> int:
        """public int box2dLight.Light.getRayNum()"""
        return int._wrap(super(Light, self).getRayNum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def getBody(self, ):
        """public abstract com.badlogic.gdx.physics.box2d.Body box2dLight.Light.getBody()"""
        pass

    @overload
    def setContactFilter(self, arg0: 'Filter'):
        """public void box2dLight.Light.setContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        super(_Light, self).setContactFilter(arg0)

    @overload
    def getIgnoreAttachedBody(self) -> bool:
        """public boolean box2dLight.Light.getIgnoreAttachedBody()"""
        return bool._wrap(super(Light, self).getIgnoreAttachedBody())

    @override
    @overload
    def dispose(self):
        """public void box2dLight.Light.dispose()"""
        super(Light, self).dispose()

    @abstractmethod
    def setPosition(self, arg0: float, arg1: float):
        """public abstract void box2dLight.Light.setPosition(float,float)"""
        pass

    @overload
    def add(self, arg0: 'RayHandler'):
        """public void box2dLight.Light.add(box2dLight.RayHandler)"""
        super(_Light, self).add(arg0)

    @overload
    def remove(self):
        """public void box2dLight.Light.remove()"""
        super(Light, self).remove()

    @abstractmethod
    def setPosition(self, arg0: 'Vector2'):
        """public abstract void box2dLight.Light.setPosition(com.badlogic.gdx.math.Vector2)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def setDirection(self, arg0: float):
        """public abstract void box2dLight.Light.setDirection(float)"""
        pass

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void box2dLight.Light.setColor(float,float,float,float)"""
        super(_Light, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: int, arg1: int, arg2: int):
        """public static void box2dLight.Light.setGlobalContactFilter(short,short,short)"""
        _Light.setGlobalContactFilter(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2))

    @overload
    def setActive(self, arg0: bool):
        """public void box2dLight.Light.setActive(boolean)"""
        super(_Light, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGlobalContactFilter(arg0: 'Filter'):
        """public static void box2dLight.Light.setGlobalContactFilter(com.badlogic.gdx.physics.box2d.Filter)"""
        _Light.setGlobalContactFilter(arg0)

    @overload
    def getDirection(self) -> float:
        """public float box2dLight.Light.getDirection()"""
        return float._wrap(super(Light, self).getDirection())

    @overload
    def isStaticLight(self) -> bool:
        """public boolean box2dLight.Light.isStaticLight()"""
        return bool._wrap(super(Light, self).isStaticLight())

    @overload
    def setSoft(self, arg0: bool):
        """public void box2dLight.Light.setSoft(boolean)"""
        super(_Light, self).setSoft(_boolean.valueOf(arg0))

    @abstractmethod
    def attachToBody(self, arg0: 'Body'):
        """public abstract void box2dLight.Light.attachToBody(com.badlogic.gdx.physics.box2d.Body)"""
        pass

    @overload
    def isActive(self) -> bool:
        """public boolean box2dLight.Light.isActive()"""
        return bool._wrap(super(Light, self).isActive())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void box2dLight.Light.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Light, self).setColor(arg0)

    @abstractmethod
    def getX(self, ):
        """public abstract float box2dLight.Light.getX()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSoftShadowLength(self) -> float:
        """public float box2dLight.Light.getSoftShadowLength()"""
        return float._wrap(super(Light, self).getSoftShadowLength())

    @overload
    def getDistance(self) -> float:
        """public float box2dLight.Light.getDistance()"""
        return float._wrap(super(Light, self).getDistance())

    @overload
    def isSoft(self) -> bool:
        """public boolean box2dLight.Light.isSoft()"""
        return bool._wrap(super(Light, self).isSoft())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())