from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
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

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
import com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer as __IsometricTiledMapRenderer
__IsometricTiledMapRenderer = __IsometricTiledMapRenderer
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class IsometricTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __IsometricTiledMapRenderer) -> 'IsometricTiledMapRenderer':
        return IsometricTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IsometricTiledMapRenderer):
        """
        Dynamic initializer for IsometricTiledMapRenderer.
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
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__IsometricTiledMapRenderer, self).renderTileLayer(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __IsometricTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __IsometricTiledMapRenderer(arg0)
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
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0)

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
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

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
import com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer as __IsometricTiledMapRenderer
__IsometricTiledMapRenderer = __IsometricTiledMapRenderer
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class IsometricTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __IsometricTiledMapRenderer) -> 'IsometricTiledMapRenderer':
        return IsometricTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IsometricTiledMapRenderer):
        """
        Dynamic initializer for IsometricTiledMapRenderer.
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
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__IsometricTiledMapRenderer, self).renderTileLayer(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __IsometricTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __IsometricTiledMapRenderer(arg0)
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
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0)

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.IsometricTiledMapRenderer 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
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

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer as __IsometricStaggeredTiledMapRenderer
__IsometricStaggeredTiledMapRenderer = __IsometricStaggeredTiledMapRenderer
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class IsometricStaggeredTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __IsometricStaggeredTiledMapRenderer) -> 'IsometricStaggeredTiledMapRenderer':
        return IsometricStaggeredTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IsometricStaggeredTiledMapRenderer):
        """
        Dynamic initializer for IsometricStaggeredTiledMapRenderer.
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
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricStaggeredTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __IsometricStaggeredTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__IsometricStaggeredTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __IsometricStaggeredTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.IsometricStaggeredTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __IsometricStaggeredTiledMapRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.tiled.TiledMapRenderer as __TiledMapRenderer
__TiledMapRenderer = __TiledMapRenderer
from builtins import float
from abc import abstractmethod, ABC
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class BatchTiledMapRenderer(ABC):
    """com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __BatchTiledMapRenderer) -> 'BatchTiledMapRenderer':
        return BatchTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BatchTiledMapRenderer):
        """
        Dynamic initializer for BatchTiledMapRenderer.
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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

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
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __BatchTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __BatchTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __BatchTiledMapRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __BatchTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

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
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer as __OrthoCachedTiledMapRenderer
__OrthoCachedTiledMapRenderer = __OrthoCachedTiledMapRenderer
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.graphics.g2d.SpriteCache as __SpriteCache
__SpriteCache = __SpriteCache
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

 
class OrthoCachedTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __OrthoCachedTiledMapRenderer) -> 'OrthoCachedTiledMapRenderer':
        return OrthoCachedTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrthoCachedTiledMapRenderer):
        """
        Dynamic initializer for OrthoCachedTiledMapRenderer.
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
    def setBlending(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setBlending(boolean)"""
        super(__OrthoCachedTiledMapRenderer, self).setBlending(__boolean.valueOf(arg0))

    @overload
    def getSpriteCache(self) -> 'g2d.SpriteCache':
        """public com.badlogic.gdx.graphics.g2d.SpriteCache com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.getSpriteCache()"""
        return 'g2d.SpriteCache'.__wrap(super(OrthoCachedTiledMapRenderer, self).getSpriteCache())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: int):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,int)"""
        val = __OrthoCachedTiledMapRenderer(arg0, __float.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__OrthoCachedTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setMaxTileSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setMaxTileSize(float,float)"""
        super(__OrthoCachedTiledMapRenderer, self).setMaxTileSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__OrthoCachedTiledMapRenderer, self).setView(arg0)

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__OrthoCachedTiledMapRenderer, self).renderObject(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __OrthoCachedTiledMapRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setOverCache(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.setOverCache(float)"""
        super(__OrthoCachedTiledMapRenderer, self).setOverCache(__float.valueOf(arg0))

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__OrthoCachedTiledMapRenderer, self).renderObjects(arg0)

    @overload
    def invalidateCache(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.invalidateCache()"""
        super(OrthoCachedTiledMapRenderer, self).invalidateCache()

    @overload
    def isCached(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.isCached()"""
        return bool.__wrap(super(OrthoCachedTiledMapRenderer, self).isCached())

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.render(int[])"""
        super(__OrthoCachedTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__OrthoCachedTiledMapRenderer, self).renderImageLayer(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__OrthoCachedTiledMapRenderer, self).renderTileLayer(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __OrthoCachedTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
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

import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer as __HexagonalTiledMapRenderer
__HexagonalTiledMapRenderer = __HexagonalTiledMapRenderer
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class HexagonalTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __HexagonalTiledMapRenderer) -> 'HexagonalTiledMapRenderer':
        return HexagonalTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HexagonalTiledMapRenderer):
        """
        Dynamic initializer for HexagonalTiledMapRenderer.
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
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __HexagonalTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __HexagonalTiledMapRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.dispose()"""
        super(BatchTiledMapRenderer, self).dispose()

    @override
    @overload
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

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
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __HexagonalTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__HexagonalTiledMapRenderer, self).renderTileLayer(arg0)

    @override
    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.HexagonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __HexagonalTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
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

import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer as __OrthogonalTiledMapRenderer
__OrthogonalTiledMapRenderer = __OrthogonalTiledMapRenderer
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer as __BatchTiledMapRenderer
__BatchTiledMapRenderer = __BatchTiledMapRenderer
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
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import int
 
class OrthogonalTiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __OrthogonalTiledMapRenderer) -> 'OrthogonalTiledMapRenderer':
        return OrthogonalTiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrthogonalTiledMapRenderer):
        """
        Dynamic initializer for OrthogonalTiledMapRenderer.
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
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(BatchTiledMapRenderer, self).getBatch())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __OrthogonalTiledMapRenderer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def render(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.render(int[])"""
        super(__BatchTiledMapRenderer, self).render(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'TiledMap'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap)"""
        val = __OrthogonalTiledMapRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float)"""
        val = __OrthogonalTiledMapRenderer(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        super(__BatchTiledMapRenderer, self).setView(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getViewBounds(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getViewBounds()"""
        return 'math.Rectangle'.__wrap(super(BatchTiledMapRenderer, self).getViewBounds())

    @override
    @overload
    def renderObject(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        super(__BatchTiledMapRenderer, self).renderObject(arg0)

    @override
    @overload
    def renderObjects(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        super(__BatchTiledMapRenderer, self).renderObjects(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMap(self, arg0: 'TiledMap'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setMap(com.badlogic.gdx.maps.tiled.TiledMap)"""
        super(__BatchTiledMapRenderer, self).setMap(arg0)

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
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        super(__BatchTiledMapRenderer, self).renderImageLayer(arg0)

    @override
    @overload
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public void com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        super(__OrthogonalTiledMapRenderer, self).renderTileLayer(arg0)

    @overload
    def __init__(self, arg0: 'TiledMap', arg1: float, arg2: 'Batch'):
        """public com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer(com.badlogic.gdx.maps.tiled.TiledMap,float,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __OrthogonalTiledMapRenderer(arg0, __float.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getUnitScale(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getUnitScale()"""
        return float.__wrap(super(BatchTiledMapRenderer, self).getUnitScale())

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
    def getMap(self) -> 'tiled.TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.getMap()"""
        return 'tiled.TiledMap'.__wrap(super(BatchTiledMapRenderer, self).getMap())

    @override
    @overload
    def setView(self, arg0: 'OrthographicCamera'):
        """public void com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        super(__BatchTiledMapRenderer, self).setView(arg0)