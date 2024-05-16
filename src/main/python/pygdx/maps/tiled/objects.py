from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject as _TiledMapTileMapObject
_TiledMapTileMapObject = _TiledMapTileMapObject
import com.badlogic.gdx.maps.objects.TextureMapObject as _TextureMapObject
_TextureMapObject = _TextureMapObject
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapTileMapObject():
    """com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTileMapObject) -> 'TiledMapTileMapObject':
        return TiledMapTileMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTileMapObject):
        """
        Dynamic initializer for TiledMapTileMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTileMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTileMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipVertically()"""
        return bool._wrap(super(TiledMapTileMapObject, self).isFlipVertically())

    @overload
    def __init__(self, arg0: 'TiledMapTile', arg1: bool, arg2: bool):
        """public com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject(com.badlogic.gdx.maps.tiled.TiledMapTile,boolean,boolean)"""
        val = _TiledMapTileMapObject(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float._wrap(super(objects.TextureMapObject, self).getRotation())

    @overload
    def setFlipVertically(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipVertically(boolean)"""
        super(_TiledMapTileMapObject, self).setFlipVertically(_boolean.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float._wrap(super(objects.TextureMapObject, self).getY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float._wrap(super(objects.TextureMapObject, self).getScaleX())

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
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float._wrap(super(objects.TextureMapObject, self).getX())

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(_objects.TextureMapObject, self).setOriginY(_float.valueOf(arg0))

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
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(_objects.TextureMapObject, self).setScaleX(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setFlipHorizontally(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipHorizontally(boolean)"""
        super(_TiledMapTileMapObject, self).setFlipHorizontally(_boolean.valueOf(arg0))

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
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float._wrap(super(objects.TextureMapObject, self).getOriginX())

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(objects.TextureMapObject, self).getTextureRegion())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(_objects.TextureMapObject, self).setRotation(_float.valueOf(arg0))

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

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float._wrap(super(objects.TextureMapObject, self).getOriginY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(_objects.TextureMapObject, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(_objects.TextureMapObject, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(_objects.TextureMapObject, self).setScaleY(_float.valueOf(arg0))

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float._wrap(super(objects.TextureMapObject, self).getScaleY())

    @overload
    def getTile(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.getTile()"""
        return 'tiled.TiledMapTile'._wrap(super(TiledMapTileMapObject, self).getTile())

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
    def setTile(self, arg0: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(_TiledMapTileMapObject, self).setTile(arg0)

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(_objects.TextureMapObject, self).setOriginX(_float.valueOf(arg0))

    @overload
    def isFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipHorizontally()"""
        return bool._wrap(super(TiledMapTileMapObject, self).isFlipHorizontally())

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
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_objects.TextureMapObject, self).setTextureRegion(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject as _TiledMapTileMapObject
_TiledMapTileMapObject = _TiledMapTileMapObject
import com.badlogic.gdx.maps.objects.TextureMapObject as _TextureMapObject
_TextureMapObject = _TextureMapObject
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapObject as _MapObject
_MapObject = _MapObject
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapTileMapObject():
    """com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTileMapObject) -> 'TiledMapTileMapObject':
        return TiledMapTileMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTileMapObject):
        """
        Dynamic initializer for TiledMapTileMapObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTileMapObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTileMapObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipVertically()"""
        return bool._wrap(super(TiledMapTileMapObject, self).isFlipVertically())

    @overload
    def __init__(self, arg0: 'TiledMapTile', arg1: bool, arg2: bool):
        """public com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject(com.badlogic.gdx.maps.tiled.TiledMapTile,boolean,boolean)"""
        val = _TiledMapTileMapObject(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float._wrap(super(objects.TextureMapObject, self).getRotation())

    @overload
    def setFlipVertically(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipVertically(boolean)"""
        super(_TiledMapTileMapObject, self).setFlipVertically(_boolean.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float._wrap(super(objects.TextureMapObject, self).getY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float._wrap(super(objects.TextureMapObject, self).getScaleX())

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
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float._wrap(super(objects.TextureMapObject, self).getX())

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(_objects.TextureMapObject, self).setOriginY(_float.valueOf(arg0))

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
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(_objects.TextureMapObject, self).setScaleX(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setFlipHorizontally(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipHorizontally(boolean)"""
        super(_TiledMapTileMapObject, self).setFlipHorizontally(_boolean.valueOf(arg0))

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
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float._wrap(super(objects.TextureMapObject, self).getOriginX())

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(objects.TextureMapObject, self).getTextureRegion())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(_objects.TextureMapObject, self).setRotation(_float.valueOf(arg0))

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

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float._wrap(super(objects.TextureMapObject, self).getOriginY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(_objects.TextureMapObject, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(_objects.TextureMapObject, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(_objects.TextureMapObject, self).setScaleY(_float.valueOf(arg0))

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float._wrap(super(objects.TextureMapObject, self).getScaleY())

    @overload
    def getTile(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.getTile()"""
        return 'tiled.TiledMapTile'._wrap(super(TiledMapTileMapObject, self).getTile())

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
    def setTile(self, arg0: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(_TiledMapTileMapObject, self).setTile(arg0)

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(_objects.TextureMapObject, self).setOriginX(_float.valueOf(arg0))

    @overload
    def isFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipHorizontally()"""
        return bool._wrap(super(TiledMapTileMapObject, self).isFlipHorizontally())

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
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_objects.TextureMapObject, self).setTextureRegion(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject