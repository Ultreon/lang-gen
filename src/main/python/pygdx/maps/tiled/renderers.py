from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
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
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer as _OrthogonalTiledMapRenderer
_OrthogonalTiledMapRenderer = _OrthogonalTiledMapRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OrthogonalTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _OrthogonalTiledMapRenderer) -> 'OrthogonalTiledMapRenderer':
        return OrthogonalTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrthogonalTiledMapRenderer):
        """
        Dynamic initializer for OrthogonalTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrthogonalTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrthogonalTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _OrthogonalTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _OrthogonalTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_OrthogonalTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _OrthogonalTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _OrthogonalTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
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
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer as _OrthogonalTiledMapRenderer
_OrthogonalTiledMapRenderer = _OrthogonalTiledMapRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OrthogonalTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _OrthogonalTiledMapRenderer) -> 'OrthogonalTiledMapRenderer':
        return OrthogonalTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrthogonalTiledMapRenderer):
        """
        Dynamic initializer for OrthogonalTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrthogonalTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrthogonalTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _OrthogonalTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _OrthogonalTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_OrthogonalTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _OrthogonalTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _OrthogonalTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
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
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer as _IsometricTiledMapRenderer
_IsometricTiledMapRenderer = _IsometricTiledMapRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IsometricTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _IsometricTiledMapRenderer) -> 'IsometricTiledMapRenderer':
        return IsometricTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IsometricTiledMapRenderer):
        """
        Dynamic initializer for IsometricTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IsometricTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IsometricTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_IsometricTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _IsometricTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _IsometricTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _IsometricTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _IsometricTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
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
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer as _HexagonalTiledMapRenderer
_HexagonalTiledMapRenderer = _HexagonalTiledMapRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HexagonalTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _HexagonalTiledMapRenderer) -> 'HexagonalTiledMapRenderer':
        return HexagonalTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HexagonalTiledMapRenderer):
        """
        Dynamic initializer for HexagonalTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HexagonalTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HexagonalTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _HexagonalTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _HexagonalTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _HexagonalTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _HexagonalTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_HexagonalTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer as _IsometricStaggeredTiledMapRenderer
_IsometricStaggeredTiledMapRenderer = _IsometricStaggeredTiledMapRenderer
from builtins import float
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
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
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IsometricStaggeredTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _IsometricStaggeredTiledMapRenderer) -> 'IsometricStaggeredTiledMapRenderer':
        return IsometricStaggeredTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IsometricStaggeredTiledMapRenderer):
        """
        Dynamic initializer for IsometricStaggeredTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IsometricStaggeredTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IsometricStaggeredTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _IsometricStaggeredTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_IsometricStaggeredTiledMapRenderer, self).renderTileLayer(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _IsometricStaggeredTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _IsometricStaggeredTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _IsometricStaggeredTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer
from pyquantum_helper import import_once as _import_once
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
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer as _OrthoCachedTiledMapRenderer
_OrthoCachedTiledMapRenderer = _OrthoCachedTiledMapRenderer
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g2d.SpriteCache as _SpriteCache
_SpriteCache = _SpriteCache
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

import java.lang.Class as _Class
_Class = _Class
 
class OrthoCachedTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _OrthoCachedTiledMapRenderer) -> 'OrthoCachedTiledMapRenderer':
        return OrthoCachedTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrthoCachedTiledMapRenderer):
        """
        Dynamic initializer for OrthoCachedTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrthoCachedTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrthoCachedTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_OrthoCachedTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.render(int[])"""
        super(_OrthoCachedTiledMapRenderer, self).render(arg0)

    @overload
    def getSpriteCache(self) -> 'g2d.SpriteCache':
        """public com.badlogic.gdx.graphics.g2d.SpriteCache com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.getSpriteCache()"""
        return 'g2d.SpriteCache'._wrap(super(OrthoCachedTiledMapRenderer, self).getSpriteCache())

    @overload
    def setMaxTileSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setMaxTileSize(float,float)"""
        super(_OrthoCachedTiledMapRenderer, self).setMaxTileSize(_float.valueOf(arg0), _float.valueOf(arg1))

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

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_OrthoCachedTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _OrthoCachedTiledMapRenderer(arg0)
        self.__wrapper = val

    @overload
    def invalidateCache(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.invalidateCache()"""
        super(OrthoCachedTiledMapRenderer, self).invalidateCache()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_OrthoCachedTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def isCached(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.isCached()"""
        return bool._wrap(super(OrthoCachedTiledMapRenderer, self).isCached())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_OrthoCachedTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(_OrthoCachedTiledMapRenderer, self).renderTileLayer(arg0)

    @overload
    def setOverCache(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setOverCache(float)"""
        super(_OrthoCachedTiledMapRenderer, self).setOverCache(_float.valueOf(arg0))

    @overload
    def setBlending(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setBlending(boolean)"""
        super(_OrthoCachedTiledMapRenderer, self).setBlending(_boolean.valueOf(arg0))

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_OrthoCachedTiledMapRenderer, self).renderObject(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _OrthoCachedTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: int):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,int)"""
        val = _OrthoCachedTiledMapRenderer(arg0, _float.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.render()"""
        super(OrthoCachedTiledMapRenderer, self).render()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.dispose()"""
        super(OrthoCachedTiledMapRenderer, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
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
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as _BatchTiledMapRenderer
_BatchTiledMapRenderer = _BatchTiledMapRenderer
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.lang.Float as _float
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.TiledMapRenderer as _TiledMapRenderer
_TiledMapRenderer = _TiledMapRenderer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BatchTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _BatchTiledMapRenderer) -> 'BatchTiledMapRenderer':
        return BatchTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BatchTiledMapRenderer):
        """
        Dynamic initializer for BatchTiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BatchTiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BatchTiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = _BatchTiledMapRenderer(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(_BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(_BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(_BatchTiledMapRenderer, self).setView(arg0)

    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float._wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @overload
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'._wrap(super(BatchTiledMapRenderer, self).getMap())

    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'._wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

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
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _BatchTiledMapRenderer(arg0, _float.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(_BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'._wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(_BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(_BatchTiledMapRenderer, self).setView(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(_BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = _BatchTiledMapRenderer(arg0)
        self.__wrapper = val

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render()"""
        super(BatchTiledMapRenderer, self).render()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _BatchTiledMapRenderer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())