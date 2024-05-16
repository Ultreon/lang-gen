from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver_AssetManagerImageResolver
__AssetManagerImageResolver = __ImageResolver_AssetManagerImageResolver.AssetManagerImageResolver
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetManagerImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.AssetManagerImageResolver"""
 
    @staticmethod
    def __wrap(java_value: __AssetManagerImageResolver) -> 'AssetManagerImageResolver':
        return AssetManagerImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetManagerImageResolver):
        """
        Dynamic initializer for AssetManagerImageResolver.
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
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__AssetManagerImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'AssetManager'):
        """public com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver(com.badlogic.gdx.assets.AssetManager)"""
        val = __AssetManagerImageResolver(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver_AssetManagerImageResolver
__AssetManagerImageResolver = __ImageResolver_AssetManagerImageResolver.AssetManagerImageResolver
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetManagerImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.AssetManagerImageResolver"""
 
    @staticmethod
    def __wrap(java_value: __AssetManagerImageResolver) -> 'AssetManagerImageResolver':
        return AssetManagerImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetManagerImageResolver):
        """
        Dynamic initializer for AssetManagerImageResolver.
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
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__AssetManagerImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'AssetManager'):
        """public com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver(com.badlogic.gdx.assets.AssetManager)"""
        val = __AssetManagerImageResolver(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$AssetManagerImageResolver 
 
 
# CLASS: com.badlogic.gdx.maps.MapRenderer
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.MapRenderer as __MapRenderer
__MapRenderer = __MapRenderer
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class MapRenderer(ABC):
    """com.badlogic.gdx.maps.MapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __MapRenderer) -> 'MapRenderer':
        return MapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapRenderer):
        """
        Dynamic initializer for MapRenderer.
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
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        pass

    @abstractmethod
    def render(self, arg0: 'int'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render(int[])"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render()"""
        pass

    @abstractmethod
    def setView(self, arg0: 'OrthographicCamera'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.MapLayers
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.MapLayer as __MapLayer
__MapLayer = __MapLayer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.MapLayers as __MapLayers
__MapLayers = __MapLayers
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MapLayers():
    """com.badlogic.gdx.maps.MapLayers"""
 
    @staticmethod
    def __wrap(java_value: __MapLayers) -> 'MapLayers':
        return MapLayers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapLayers):
        """
        Dynamic initializer for MapLayers.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.maps.MapLayers.iterator()"""
        return 'Iterator'.__wrap(super(MapLayers, self).iterator())

    @overload
    def getByType(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapLayers.getByType(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'.__wrap(super(__MapLayers, self).getByType(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getIndex(self, arg0: 'MapLayer') -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getIndex(com.badlogic.gdx.maps.MapLayer)"""
        return int.__wrap(super(__MapLayers, self).getIndex(arg0))

    @overload
    def remove(self, arg0: int):
        """public void com.badlogic.gdx.maps.MapLayers.remove(int)"""
        super(__MapLayers, self).remove(__int.valueOf(arg0))

    @overload
    def getByType(self, arg0: 'Class') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapLayer> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapLayers.getByType(java.lang.Class<T>)"""
        return 'utils.Array'.__wrap(super(__MapLayers, self).getByType(arg0))

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
    def getCount(self) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getCount()"""
        return int.__wrap(super(MapLayers, self).getCount())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def get(self, arg0: int) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayers.get(int)"""
        return 'MapLayer'.__wrap(super(__MapLayers, self).get(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapLayers()"""
        val = __MapLayers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayers.add(com.badlogic.gdx.maps.MapLayer)"""
        super(__MapLayers, self).add(arg0)

    @overload
    def get(self, arg0: str) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayers.get(java.lang.String)"""
        return 'MapLayer'.__wrap(super(__MapLayers, self).get(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapLayers()"""
        val = __MapLayers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.size()"""
        return int.__wrap(super(MapLayers, self).size())

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
    def remove(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayers.remove(com.badlogic.gdx.maps.MapLayer)"""
        super(__MapLayers, self).remove(arg0)

    @overload
    def getIndex(self, arg0: str) -> int:
        """public int com.badlogic.gdx.maps.MapLayers.getIndex(java.lang.String)"""
        return int.__wrap(super(__MapLayers, self).getIndex(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: com.badlogic.gdx.maps.MapLayer
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.maps.MapLayer as __MapLayer
__MapLayer = __MapLayer
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
 
class MapLayer():
    """com.badlogic.gdx.maps.MapLayer"""
 
    @staticmethod
    def __wrap(java_value: __MapLayer) -> 'MapLayer':
        return MapLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapLayer):
        """
        Dynamic initializer for MapLayer.
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
        """public com.badlogic.gdx.maps.MapLayer()"""
        val = __MapLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(__MapLayer, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def getObjects(self) -> 'MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'MapObjects'.__wrap(super(MapLayer, self).getObjects())

    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(__MapLayer, self).setParallaxX(__float.valueOf(arg0))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str.__wrap(super(MapLayer, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float.__wrap(super(MapLayer, self).getParallaxX())

    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(__MapLayer, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float.__wrap(super(MapLayer, self).getOffsetY())

    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float.__wrap(super(MapLayer, self).getRenderOffsetX())

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
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool.__wrap(super(MapLayer, self).isVisible())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapLayer()"""
        val = __MapLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float.__wrap(super(MapLayer, self).getParallaxY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(__MapLayer, self).setParent(arg0)

    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'MapProperties'.__wrap(super(MapLayer, self).getProperties())

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
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(__MapLayer, self).setOffsetY(__float.valueOf(arg0))

    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float.__wrap(super(MapLayer, self).getOpacity())

    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapLayer.invalidateRenderOffset()"""
        super(MapLayer, self).invalidateRenderOffset()

    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float.__wrap(super(MapLayer, self).getRenderOffsetY())

    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(__MapLayer, self).setOffsetX(__float.valueOf(arg0))

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(__MapLayer, self).setName(arg0)

    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float.__wrap(super(MapLayer, self).getOffsetX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getParent(self) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'MapLayer'.__wrap(super(MapLayer, self).getParent())

    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(__MapLayer, self).setParallaxY(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.Map
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.Map as __Map
__Map = __Map
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.MapLayers as __MapLayers
__MapLayers = __MapLayers
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Map():
    """com.badlogic.gdx.maps.Map"""
 
    @staticmethod
    def __wrap(java_value: __Map) -> 'Map':
        return Map(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Map):
        """
        Dynamic initializer for Map.
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
    def getLayers(self) -> 'MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.Map.getLayers()"""
        return 'MapLayers'.__wrap(super(Map, self).getLayers())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.Map()"""
        val = __Map()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.Map.getProperties()"""
        return 'MapProperties'.__wrap(super(Map, self).getProperties())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.Map()"""
        val = __Map()
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
    def dispose(self):
        """public void com.badlogic.gdx.maps.Map.dispose()"""
        super(Map, self).dispose()

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
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$DirectImageResolver
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver_DirectImageResolver
__DirectImageResolver = __ImageResolver_DirectImageResolver.DirectImageResolver
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DirectImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.DirectImageResolver"""
 
    @staticmethod
    def __wrap(java_value: __DirectImageResolver) -> 'DirectImageResolver':
        return DirectImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectImageResolver):
        """
        Dynamic initializer for DirectImageResolver.
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
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$DirectImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__DirectImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.maps.ImageResolver$DirectImageResolver(com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Texture>)"""
        val = __DirectImageResolver(arg0)
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
 
 
# CLASS: com.badlogic.gdx.maps.MapObjects
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
import java.util.Iterator as Iterator
import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MapObjects():
    """com.badlogic.gdx.maps.MapObjects"""
 
    @staticmethod
    def __wrap(java_value: __MapObjects) -> 'MapObjects':
        return MapObjects(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapObjects):
        """
        Dynamic initializer for MapObjects.
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
    def get(self, arg0: int) -> 'MapObject':
        """public com.badlogic.gdx.maps.MapObject com.badlogic.gdx.maps.MapObjects.get(int)"""
        return 'MapObject'.__wrap(super(__MapObjects, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getByType(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapObjects.getByType(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'.__wrap(super(__MapObjects, self).getByType(arg0, arg1))

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getCount()"""
        return int.__wrap(super(MapObjects, self).getCount())

    @overload
    def getIndex(self, arg0: 'MapObject') -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getIndex(com.badlogic.gdx.maps.MapObject)"""
        return int.__wrap(super(__MapObjects, self).getIndex(arg0))

    @overload
    def getByType(self, arg0: 'Class') -> 'utils.Array':
        """public <T extends com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.maps.MapObjects.getByType(java.lang.Class<T>)"""
        return 'utils.Array'.__wrap(super(__MapObjects, self).getByType(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.MapObjects.add(com.badlogic.gdx.maps.MapObject)"""
        super(__MapObjects, self).add(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: 'MapObject'):
        """public void com.badlogic.gdx.maps.MapObjects.remove(com.badlogic.gdx.maps.MapObject)"""
        super(__MapObjects, self).remove(arg0)

    @overload
    def get(self, arg0: str) -> 'MapObject':
        """public com.badlogic.gdx.maps.MapObject com.badlogic.gdx.maps.MapObjects.get(java.lang.String)"""
        return 'MapObject'.__wrap(super(__MapObjects, self).get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getIndex(self, arg0: str) -> int:
        """public int com.badlogic.gdx.maps.MapObjects.getIndex(java.lang.String)"""
        return int.__wrap(super(__MapObjects, self).getIndex(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapObjects()"""
        val = __MapObjects()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.MapObjects.iterator()"""
        return 'Iterator'.__wrap(super(MapObjects, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def remove(self, arg0: int):
        """public void com.badlogic.gdx.maps.MapObjects.remove(int)"""
        super(__MapObjects, self).remove(__int.valueOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapObjects()"""
        val = __MapObjects()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver_TextureAtlasImageResolver
__TextureAtlasImageResolver = __ImageResolver_TextureAtlasImageResolver.TextureAtlasImageResolver
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TextureAtlasImageResolver():
    """com.badlogic.gdx.maps.ImageResolver.TextureAtlasImageResolver"""
 
    @staticmethod
    def __wrap(java_value: __TextureAtlasImageResolver) -> 'TextureAtlasImageResolver':
        return TextureAtlasImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAtlasImageResolver):
        """
        Dynamic initializer for TextureAtlasImageResolver.
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
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__TextureAtlasImageResolver, self).getImage(arg0))

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
    def __init__(self, arg0: 'TextureAtlas'):
        """public com.badlogic.gdx.maps.ImageResolver$TextureAtlasImageResolver(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        val = __TextureAtlasImageResolver(arg0)
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
 
 
# CLASS: com.badlogic.gdx.maps.MapObject
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
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
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class MapObject():
    """com.badlogic.gdx.maps.MapObject"""
 
    @staticmethod
    def __wrap(java_value: __MapObject) -> 'MapObject':
        return MapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapObject):
        """
        Dynamic initializer for MapObject.
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
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapObject.getOpacity()"""
        return float.__wrap(super(MapObject, self).getOpacity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapObject.getName()"""
        return str.__wrap(super(MapObject, self).getName())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.maps.MapObject.getColor()"""
        return 'graphics.Color'.__wrap(super(MapObject, self).getColor())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.maps.MapObject.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__MapObject, self).setColor(arg0)

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__MapObject, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapObject()"""
        val = __MapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapObject()"""
        val = __MapObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(MapObject, self).isVisible())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__MapObject, self).setName(arg0)

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
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapObject.getProperties()"""
        return 'MapProperties'.__wrap(super(MapObject, self).getProperties())

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
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__MapObject, self).setOpacity(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.MapProperties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MapProperties():
    """com.badlogic.gdx.maps.MapProperties"""
 
    @staticmethod
    def __wrap(java_value: __MapProperties) -> 'MapProperties':
        return MapProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapProperties):
        """
        Dynamic initializer for MapProperties.
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
    def remove(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapProperties.remove(java.lang.String)"""
        super(__MapProperties, self).remove(arg0)

    @overload
    def getValues(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.Object> com.badlogic.gdx.maps.MapProperties.getValues()"""
        return 'Iterator'.__wrap(super(MapProperties, self).getValues())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def get(self, arg0: str) -> object:
        """public java.lang.Object com.badlogic.gdx.maps.MapProperties.get(java.lang.String)"""
        return object.__wrap(super(__MapProperties, self).get(arg0))

    @overload
    def getKeys(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> com.badlogic.gdx.maps.MapProperties.getKeys()"""
        return 'Iterator'.__wrap(super(MapProperties, self).getKeys())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapProperties()"""
        val = __MapProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.maps.MapProperties.clear()"""
        super(MapProperties, self).clear()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.MapProperties()"""
        val = __MapProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putAll(self, arg0: 'MapProperties'):
        """public void com.badlogic.gdx.maps.MapProperties.putAll(com.badlogic.gdx.maps.MapProperties)"""
        super(__MapProperties, self).putAll(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def put(self, arg0: str, arg1: object):
        """public void com.badlogic.gdx.maps.MapProperties.put(java.lang.String,java.lang.Object)"""
        super(__MapProperties, self).put(arg0, arg1)

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
    def get(self, arg0: str, arg1: object, arg2: 'Class') -> object:
        """public <T> T com.badlogic.gdx.maps.MapProperties.get(java.lang.String,T,java.lang.Class<T>)"""
        return object.__wrap(super(__MapProperties, self).get(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def containsKey(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.maps.MapProperties.containsKey(java.lang.String)"""
        return bool.__wrap(super(__MapProperties, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: str, arg1: 'Class') -> object:
        """public <T> T com.badlogic.gdx.maps.MapProperties.get(java.lang.String,java.lang.Class<T>)"""
        return object.__wrap(super(__MapProperties, self).get(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.ImageResolver
from abc import abstractmethod, ABC
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver
__ImageResolver = __ImageResolver
 
class ImageResolver(ABC):
    """com.badlogic.gdx.maps.ImageResolver"""
 
    @staticmethod
    def __wrap(java_value: __ImageResolver) -> 'ImageResolver':
        return ImageResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageResolver):
        """
        Dynamic initializer for ImageResolver.
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
    def getImage(self, arg0: str):
        """public abstract com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver.getImage(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.MapGroupLayer
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.maps.MapGroupLayer as __MapGroupLayer
__MapGroupLayer = __MapGroupLayer
import com.badlogic.gdx.maps.MapLayer as __MapLayer
__MapLayer = __MapLayer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.MapLayers as __MapLayers
__MapLayers = __MapLayers
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MapGroupLayer():
    """com.badlogic.gdx.maps.MapGroupLayer"""
 
    @staticmethod
    def __wrap(java_value: __MapGroupLayer) -> 'MapGroupLayer':
        return MapGroupLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapGroupLayer):
        """
        Dynamic initializer for MapGroupLayer.
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
        """public com.badlogic.gdx.maps.MapGroupLayer()"""
        val = __MapGroupLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(__MapLayer, self).setOffsetX(__float.valueOf(arg0))

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(__MapLayer, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(__MapLayer, self).setName(arg0)

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(__MapLayer, self).setOffsetY(__float.valueOf(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool.__wrap(super(MapLayer, self).isVisible())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float.__wrap(super(MapLayer, self).getParallaxY())

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float.__wrap(super(MapLayer, self).getRenderOffsetX())

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float.__wrap(super(MapLayer, self).getOffsetY())

    @overload
    def getLayers(self) -> 'MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.MapGroupLayer.getLayers()"""
        return 'MapLayers'.__wrap(super(MapGroupLayer, self).getLayers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float.__wrap(super(MapLayer, self).getRenderOffsetY())

    @override
    @overload
    def getObjects(self) -> 'MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'MapObjects'.__wrap(super(MapLayer, self).getObjects())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(__MapLayer, self).setParallaxY(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(__MapLayer, self).setParallaxX(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.MapGroupLayer()"""
        val = __MapGroupLayer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'MapProperties'.__wrap(super(MapLayer, self).getProperties())

    @override
    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float.__wrap(super(MapLayer, self).getParallaxX())

    @override
    @overload
    def getParent(self) -> 'MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'MapLayer'.__wrap(super(MapLayer, self).getParent())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(__MapLayer, self).setVisible(__boolean.valueOf(arg0))

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
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float.__wrap(super(MapLayer, self).getOpacity())

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(__MapLayer, self).setParent(arg0)

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float.__wrap(super(MapLayer, self).getOffsetX())

    @override
    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapGroupLayer.invalidateRenderOffset()"""
        super(MapGroupLayer, self).invalidateRenderOffset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str.__wrap(super(MapLayer, self).getName())