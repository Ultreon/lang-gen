from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.maps.objects.EllipseMapObject as __EllipseMapObject
__EllipseMapObject = __EllipseMapObject
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Ellipse as __Ellipse
__Ellipse = __Ellipse
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class EllipseMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.EllipseMapObject"""
 
    @staticmethod
    def __wrap(java_value: __EllipseMapObject) -> 'EllipseMapObject':
        return EllipseMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EllipseMapObject):
        """
        Dynamic initializer for EllipseMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

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
    def getEllipse(self) -> 'math.Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.maps.objects.EllipseMapObject.getEllipse()"""
        return 'math.Ellipse'.__wrap(super(EllipseMapObject, self).getEllipse())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject(float,float,float,float)"""
        val = __EllipseMapObject(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

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
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = __EllipseMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = __EllipseMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.objects.EllipseMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.maps.objects.EllipseMapObject as __EllipseMapObject
__EllipseMapObject = __EllipseMapObject
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Ellipse as __Ellipse
__Ellipse = __Ellipse
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class EllipseMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.EllipseMapObject"""
 
    @staticmethod
    def __wrap(java_value: __EllipseMapObject) -> 'EllipseMapObject':
        return EllipseMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EllipseMapObject):
        """
        Dynamic initializer for EllipseMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

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
    def getEllipse(self) -> 'math.Ellipse':
        """public com.badlogic.gdx.math.Ellipse com.badlogic.gdx.maps.objects.EllipseMapObject.getEllipse()"""
        return 'math.Ellipse'.__wrap(super(EllipseMapObject, self).getEllipse())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject(float,float,float,float)"""
        val = __EllipseMapObject(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

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
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = __EllipseMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.EllipseMapObject()"""
        val = __EllipseMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.objects.EllipseMapObject 
 
 
# CLASS: com.badlogic.gdx.maps.objects.PolylineMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Polyline as __Polyline
__Polyline = __Polyline
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.objects.PolylineMapObject as __PolylineMapObject
__PolylineMapObject = __PolylineMapObject
import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PolylineMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.PolylineMapObject"""
 
    @staticmethod
    def __wrap(java_value: __PolylineMapObject) -> 'PolylineMapObject':
        return PolylineMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolylineMapObject):
        """
        Dynamic initializer for PolylineMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

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
    def setPolyline(self, arg0: 'Polyline'):
        """public void com.badlogic.gdx.maps.objects.PolylineMapObject.setPolyline(com.badlogic.gdx.math.Polyline)"""
        super(__PolylineMapObject, self).setPolyline(arg0)

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

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
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject()"""
        val = __PolylineMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject()"""
        val = __PolylineMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Polyline'):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject(com.badlogic.gdx.math.Polyline)"""
        val = __PolylineMapObject(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPolyline(self) -> 'math.Polyline':
        """public com.badlogic.gdx.math.Polyline com.badlogic.gdx.maps.objects.PolylineMapObject.getPolyline()"""
        return 'math.Polyline'.__wrap(super(PolylineMapObject, self).getPolyline())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.maps.objects.PolylineMapObject(float[])"""
        val = __PolylineMapObject(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.RectangleMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.maps.objects.RectangleMapObject as __RectangleMapObject
__RectangleMapObject = __RectangleMapObject
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class RectangleMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.RectangleMapObject"""
 
    @staticmethod
    def __wrap(java_value: __RectangleMapObject) -> 'RectangleMapObject':
        return RectangleMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RectangleMapObject):
        """
        Dynamic initializer for RectangleMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.maps.objects.RectangleMapObject(float,float,float,float)"""
        val = __RectangleMapObject(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.objects.RectangleMapObject.getRectangle()"""
        return 'math.Rectangle'.__wrap(super(RectangleMapObject, self).getRectangle())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

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
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.RectangleMapObject()"""
        val = __RectangleMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.RectangleMapObject()"""
        val = __RectangleMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.TextureMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.maps.objects.TextureMapObject as __TextureMapObject
__TextureMapObject = __TextureMapObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class TextureMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.TextureMapObject"""
 
    @staticmethod
    def __wrap(java_value: __TextureMapObject) -> 'TextureMapObject':
        return TextureMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureMapObject):
        """
        Dynamic initializer for TextureMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureMapObject, self).setTextureRegion(arg0)

    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(TextureMapObject, self).getTextureRegion())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float.__wrap(super(TextureMapObject, self).getX())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float.__wrap(super(TextureMapObject, self).getScaleY())

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(__TextureMapObject, self).setOriginX(__float.valueOf(arg0))

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(__TextureMapObject, self).setScaleX(__float.valueOf(arg0))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float.__wrap(super(TextureMapObject, self).getOriginY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(__TextureMapObject, self).setScaleY(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(__TextureMapObject, self).setY(__float.valueOf(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float.__wrap(super(TextureMapObject, self).getOriginX())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.TextureMapObject()"""
        val = __TextureMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(__TextureMapObject, self).setOriginY(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float.__wrap(super(TextureMapObject, self).getRotation())

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(__TextureMapObject, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(__TextureMapObject, self).setX(__float.valueOf(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float.__wrap(super(TextureMapObject, self).getY())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.maps.objects.TextureMapObject(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __TextureMapObject(arg0)
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
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float.__wrap(super(TextureMapObject, self).getScaleX())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.TextureMapObject()"""
        val = __TextureMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.CircleMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import com.badlogic.gdx.math.Circle as __Circle
__Circle = __Circle
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.objects.CircleMapObject as __CircleMapObject
__CircleMapObject = __CircleMapObject
import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class CircleMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.CircleMapObject"""
 
    @staticmethod
    def __wrap(java_value: __CircleMapObject) -> 'CircleMapObject':
        return CircleMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircleMapObject):
        """
        Dynamic initializer for CircleMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

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
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = __CircleMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.CircleMapObject()"""
        val = __CircleMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCircle(self) -> 'math.Circle':
        """public com.badlogic.gdx.math.Circle com.badlogic.gdx.maps.objects.CircleMapObject.getCircle()"""
        return 'math.Circle'.__wrap(super(CircleMapObject, self).getCircle())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.maps.objects.CircleMapObject(float,float,float)"""
        val = __CircleMapObject(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.objects.PolygonMapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import java.lang.Long as __long
import com.badlogic.gdx.maps.objects.PolygonMapObject as __PolygonMapObject
__PolygonMapObject = __PolygonMapObject
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
import com.badlogic.gdx.math.Polygon as __Polygon
__Polygon = __Polygon
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PolygonMapObject(pygdx.__MapObject, maps.MapObject):
    """com.badlogic.gdx.maps.objects.PolygonMapObject"""
 
    @staticmethod
    def __wrap(java_value: __PolygonMapObject) -> 'PolygonMapObject':
        return PolygonMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonMapObject):
        """
        Dynamic initializer for PolygonMapObject.
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
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(maps.MapObject, self).getColor())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Polygon'):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject(com.badlogic.gdx.math.Polygon)"""
        val = __PolygonMapObject(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapObject, self).getProperties())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject(float[])"""
        val = __PolygonMapObject(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPolygon(self, arg0: 'Polygon'):
        """public void com.badlogic.gdx.maps.objects.PolygonMapObject.setPolygon(com.badlogic.gdx.math.Polygon)"""
        super(__PolygonMapObject, self).setPolygon(arg0)

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(maps.MapObject, self).getOpacity())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject()"""
        val = __PolygonMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPolygon(self) -> 'math.Polygon':
        """public com.badlogic.gdx.math.Polygon com.badlogic.gdx.maps.objects.PolygonMapObject.getPolygon()"""
        return 'math.Polygon'.__wrap(super(PolygonMapObject, self).getPolygon())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(maps.MapObject, self).getName())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__maps.MapObject, self).setColor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.objects.PolygonMapObject()"""
        val = __PolygonMapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

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
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0))