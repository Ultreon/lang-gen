from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.maps.objects.CircleMapObject as _CircleMapObject
_CircleMapObject = _CircleMapObject
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import com.badlogic.gdx.math.Circle as _Circle
_Circle = _Circle
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CircleMapObject():
    """com.badlogic.gdx.maps.objects.CircleMapObject"""
 
    @staticmethod
    def _wrap(java_value: _CircleMapObject) -> 'CircleMapObject':
        return CircleMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircleMapObject):
        """
        Dynamic initializer for CircleMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircleMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircleMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.maps.objects.CircleMapObject(float,float,float)"""
        val = _CircleMapObject(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def getCircle(self) -> 'math.Circle':
        """public com.badlogic.gdx.math.Circle com.badlogic.gdx.maps.objects.CircleMapObject.getCircle()"""
        return 'math.Circle'._wrap(super(CircleMapObject, self).getCircle())

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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = _CircleMapObject()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = _CircleMapObject()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.objects.CircleMapObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.maps.objects.CircleMapObject as _CircleMapObject
_CircleMapObject = _CircleMapObject
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import com.badlogic.gdx.math.Circle as _Circle
_Circle = _Circle
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CircleMapObject():
    """com.badlogic.gdx.maps.objects.CircleMapObject"""
 
    @staticmethod
    def _wrap(java_value: _CircleMapObject) -> 'CircleMapObject':
        return CircleMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircleMapObject):
        """
        Dynamic initializer for CircleMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircleMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircleMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.maps.objects.CircleMapObject(float,float,float)"""
        val = _CircleMapObject(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def getCircle(self) -> 'math.Circle':
        """public com.badlogic.gdx.math.Circle com.badlogic.gdx.maps.objects.CircleMapObject.getCircle()"""
        return 'math.Circle'._wrap(super(CircleMapObject, self).getCircle())

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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = _CircleMapObject()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = _CircleMapObject()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.objects.CircleMapObject 
 
 
# CLASS: com.badlogic.gdx.maps.objects.EllipseMapObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import com.badlogic.gdx.maps.objects.EllipseMapObject as _EllipseMapObject
_EllipseMapObject = _EllipseMapObject
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.math.Ellipse as _Ellipse
_Ellipse = _Ellipse
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EllipseMapObject():
    """com.badlogic.gdx.maps.objects.EllipseMapObject"""
 
    @staticmethod
    def _wrap(java_value: _EllipseMapObject) -> 'EllipseMapObject':
        return EllipseMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EllipseMapObject):
        """
        Dynamic initializer for EllipseMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EllipseMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EllipseMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getEllipse(self) -> 'math.Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.maps.objects.EllipseMapObject.getEllipse()"""
        return 'math.Ellipse'._wrap(super(EllipseMapObject, self).getEllipse())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = _EllipseMapObject()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = _EllipseMapObject()
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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject(float,float,float,float)"""
        val = _EllipseMapObject(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.PolylineMapObject
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Polyline as _Polyline
_Polyline = _Polyline
from builtins import str
import com.badlogic.gdx.maps.objects.PolylineMapObject as _PolylineMapObject
_PolylineMapObject = _PolylineMapObject
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolylineMapObject():
    """com.badlogic.gdx.maps.objects.PolylineMapObject"""
 
    @staticmethod
    def _wrap(java_value: _PolylineMapObject) -> 'PolylineMapObject':
        return PolylineMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolylineMapObject):
        """
        Dynamic initializer for PolylineMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolylineMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolylineMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject()"""
        val = _PolylineMapObject()
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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setPolyline(self, arg0: 'Polyline'):
        """public void com.badlogic.gdx.maps.objects.PolylineMapObject.setPolyline(com.badlogic.gdx.math.Polyline)"""
        super(_PolylineMapObject, self).setPolyline(arg0)

    @overload
    def __init__(self, arg0: 'Polyline'):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject(com.badlogic.gdx.math.Polyline)"""
        val = _PolylineMapObject(arg0)
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject(float[])"""
        val = _PolylineMapObject(arg0)
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
    def getPolyline(self) -> 'math.Polyline':
        """public com.badlogic.gdx.math.Polyline com.badlogic.gdx.maps.objects.PolylineMapObject.getPolyline()"""
        return 'math.Polyline'._wrap(super(PolylineMapObject, self).getPolyline())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject()"""
        val = _PolylineMapObject()
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
 
 
# CLASS: com.badlogic.gdx.maps.objects.PolygonMapObject
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.math.Polygon as _Polygon
_Polygon = _Polygon
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.maps.objects.PolygonMapObject as _PolygonMapObject
_PolygonMapObject = _PolygonMapObject
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolygonMapObject():
    """com.badlogic.gdx.maps.objects.PolygonMapObject"""
 
    @staticmethod
    def _wrap(java_value: _PolygonMapObject) -> 'PolygonMapObject':
        return PolygonMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolygonMapObject):
        """
        Dynamic initializer for PolygonMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolygonMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolygonMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject(float[])"""
        val = _PolygonMapObject(arg0)
        self.__wrapper = val

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def getPolygon(self) -> 'math.Polygon':
        """public com.badlogic.gdx.math.Polygon com.badlogic.gdx.maps.objects.PolygonMapObject.getPolygon()"""
        return 'math.Polygon'._wrap(super(PolygonMapObject, self).getPolygon())

    @overload
    def setPolygon(self, arg0: 'Polygon'):
        """public void com.badlogic.gdx.maps.objects.PolygonMapObject.setPolygon(com.badlogic.gdx.math.Polygon)"""
        super(_PolygonMapObject, self).setPolygon(arg0)

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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Polygon'):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject(com.badlogic.gdx.math.Polygon)"""
        val = _PolygonMapObject(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject()"""
        val = _PolygonMapObject()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject()"""
        val = _PolygonMapObject()
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
 
 
# CLASS: com.badlogic.gdx.maps.objects.RectangleMapObject
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.maps.objects.RectangleMapObject as _RectangleMapObject
_RectangleMapObject = _RectangleMapObject
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RectangleMapObject():
    """com.badlogic.gdx.maps.objects.RectangleMapObject"""
 
    @staticmethod
    def _wrap(java_value: _RectangleMapObject) -> 'RectangleMapObject':
        return RectangleMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RectangleMapObject):
        """
        Dynamic initializer for RectangleMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RectangleMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RectangleMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

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
        """public com.badlogic.gdx.maps.objects.RectangleMapObject()"""
        val = _RectangleMapObject()
        self.__wrapper = val

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.objects.RectangleMapObject.getRectangle()"""
        return 'math.Rectangle'._wrap(super(RectangleMapObject, self).getRectangle())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.RectangleMapObject()"""
        val = _RectangleMapObject()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.maps.objects.RectangleMapObject(float,float,float,float)"""
        val = _RectangleMapObject(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.TextureMapObject
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import com.badlogic.gdx.maps.objects.TextureMapObject as _TextureMapObject
_TextureMapObject = _TextureMapObject
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureMapObject():
    """com.badlogic.gdx.maps.objects.TextureMapObject"""
 
    @staticmethod
    def _wrap(java_value: _TextureMapObject) -> 'TextureMapObject':
        return TextureMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureMapObject):
        """
        Dynamic initializer for TextureMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(TextureMapObject, self).getTextureRegion())

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(_TextureMapObject, self).setScaleX(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(_TextureMapObject, self).setY(_float.valueOf(arg0))

    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(_TextureMapObject, self).setOriginY(_float.valueOf(arg0))

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(_maps.MapObject, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapObject, self).getProperties())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.maps.objects.TextureMapObject(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _TextureMapObject(arg0)
        self.__wrapper = val

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float._wrap(super(TextureMapObject, self).getY())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.TextureMapObject()"""
        val = _TextureMapObject()
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str._wrap(super(maps.MapObject, self).getName())

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
        """public com.badlogic.gdx.maps.objects.TextureMapObject()"""
        val = _TextureMapObject()
        self.__wrapper = val

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_maps.MapObject, self).setColor(arg0)

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureMapObject, self).setTextureRegion(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool._wrap(super(maps.MapObject, self).isVisible())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float._wrap(super(TextureMapObject, self).getX())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(_maps.MapObject, self).setName(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(_maps.MapObject, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float._wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(_TextureMapObject, self).setScaleY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(_TextureMapObject, self).setX(_float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float._wrap(super(TextureMapObject, self).getScaleX())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'._wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(_TextureMapObject, self).setOriginX(_float.valueOf(arg0))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float._wrap(super(TextureMapObject, self).getOriginY())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float._wrap(super(TextureMapObject, self).getScaleY())

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(_TextureMapObject, self).setRotation(_float.valueOf(arg0))

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
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float._wrap(super(TextureMapObject, self).getOriginX())

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float._wrap(super(TextureMapObject, self).getRotation())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())