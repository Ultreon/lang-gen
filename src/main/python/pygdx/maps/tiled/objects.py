from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __string
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject as __TiledMapTileMapObject
__TiledMapTileMapObject = __TiledMapTileMapObject
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.maps.objects.TextureMapObject as __TextureMapObject
__TextureMapObject = __TextureMapObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TiledMapTileMapObject(maps.__TextureMapObject, objects.TextureMapObject):
    """com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileMapObject) -> 'TiledMapTileMapObject':
        return TiledMapTileMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileMapObject):
        """
        Dynamic initializer for TiledMapTileMapObject.
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
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getScaleX())

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getOriginX())

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
    def getTile(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.getTile()"""
        return 'tiled.TiledMapTile'.__wrap(super(TiledMapTileMapObject, self).getTile())

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__objects.TextureMapObject, self).setTextureRegion(arg0)

    @overload
    def __init__(self, arg0: 'TiledMapTile', arg1: bool, arg2: bool):
        """public com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject(com.badlogic.gdx.maps.tiled.TiledMapTile,boolean,boolean)"""
        val = __TiledMapTileMapObject(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTile(self, arg0: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(__TiledMapTileMapObject, self).setTile(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(objects.TextureMapObject, self).getTextureRegion())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getY())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(__objects.TextureMapObject, self).setOriginX(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(__objects.TextureMapObject, self).setX(__float.valueOf(arg0))

    @overload
    def setFlipHorizontally(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipHorizontally(boolean)"""
        super(__TiledMapTileMapObject, self).setFlipHorizontally(__boolean.valueOf(arg0))

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipHorizontally()"""
        return bool.__wrap(super(TiledMapTileMapObject, self).isFlipHorizontally())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(__objects.TextureMapObject, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @overload
    def isFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipVertically()"""
        return bool.__wrap(super(TiledMapTileMapObject, self).isFlipVertically())

    @override
    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(__objects.TextureMapObject, self).setScaleX(__float.valueOf(arg0))

    @overload
    def setFlipVertically(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipVertically(boolean)"""
        super(__TiledMapTileMapObject, self).setFlipVertically(__boolean.valueOf(arg0))

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
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getScaleY())

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(__objects.TextureMapObject, self).setScaleY(__float.valueOf(arg0))

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
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float.__wrap(super(objects.TextureMapObject, self).getRotation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(__objects.TextureMapObject, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(__objects.TextureMapObject, self).setOriginY(__float.valueOf(arg0))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getOriginY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.maps.MapObject as __MapObject
__MapObject = __MapObject
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __string
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject as __TiledMapTileMapObject
__TiledMapTileMapObject = __TiledMapTileMapObject
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.maps.objects.TextureMapObject as __TextureMapObject
__TextureMapObject = __TextureMapObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TiledMapTileMapObject(maps.__TextureMapObject, objects.TextureMapObject):
    """com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileMapObject) -> 'TiledMapTileMapObject':
        return TiledMapTileMapObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileMapObject):
        """
        Dynamic initializer for TiledMapTileMapObject.
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
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getScaleX())

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getOriginX())

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
    def getTile(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.getTile()"""
        return 'tiled.TiledMapTile'.__wrap(super(TiledMapTileMapObject, self).getTile())

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__objects.TextureMapObject, self).setTextureRegion(arg0)

    @overload
    def __init__(self, arg0: 'TiledMapTile', arg1: bool, arg2: bool):
        """public com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject(com.badlogic.gdx.maps.tiled.TiledMapTile,boolean,boolean)"""
        val = __TiledMapTileMapObject(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTile(self, arg0: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(__TiledMapTileMapObject, self).setTile(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.objects.TextureMapObject.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(objects.TextureMapObject, self).getTextureRegion())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getY())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapObject.setName(java.lang.String)"""
        super(__maps.MapObject, self).setName(arg0)

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginX(float)"""
        super(__objects.TextureMapObject, self).setOriginX(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setX(float)"""
        super(__objects.TextureMapObject, self).setX(__float.valueOf(arg0))

    @overload
    def setFlipHorizontally(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipHorizontally(boolean)"""
        super(__TiledMapTileMapObject, self).setFlipHorizontally(__boolean.valueOf(arg0))

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapObject.setOpacity(float)"""
        super(__maps.MapObject, self).setOpacity(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getX()"""
        return float.__wrap(super(objects.TextureMapObject, self).getX())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipHorizontally()"""
        return bool.__wrap(super(TiledMapTileMapObject, self).isFlipHorizontally())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setRotation(float)"""
        super(__objects.TextureMapObject, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapObject.isVisible()"""
        return bool.__wrap(super(maps.MapObject, self).isVisible())

    @overload
    def isFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.isFlipVertically()"""
        return bool.__wrap(super(TiledMapTileMapObject, self).isFlipVertically())

    @override
    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleX(float)"""
        super(__objects.TextureMapObject, self).setScaleX(__float.valueOf(arg0))

    @overload
    def setFlipVertically(self, arg0: bool):
        """public void com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject.setFlipVertically(boolean)"""
        super(__TiledMapTileMapObject, self).setFlipVertically(__boolean.valueOf(arg0))

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
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getScaleY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getScaleY())

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setScaleY(float)"""
        super(__objects.TextureMapObject, self).setScaleY(__float.valueOf(arg0))

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
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getRotation()"""
        return float.__wrap(super(objects.TextureMapObject, self).getRotation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setY(float)"""
        super(__objects.TextureMapObject, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.maps.objects.TextureMapObject.setOriginY(float)"""
        super(__objects.TextureMapObject, self).setOriginY(__float.valueOf(arg0))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.maps.objects.TextureMapObject.getOriginY()"""
        return float.__wrap(super(objects.TextureMapObject, self).getOriginY())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapObject.setVisible(boolean)"""
        super(__maps.MapObject, self).setVisible(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.objects.TiledMapTileMapObject