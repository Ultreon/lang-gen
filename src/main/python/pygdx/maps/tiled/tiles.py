from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile as __AnimatedTiledMapTile
__AnimatedTiledMapTile = __AnimatedTiledMapTile
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile_BlendMode
__BlendMode = __TiledMapTile_BlendMode.BlendMode
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as __StaticTiledMapTile
__StaticTiledMapTile = __StaticTiledMapTile
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

from typing import List
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class AnimatedTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile"""
 
    @staticmethod
    def __wrap(java_value: __AnimatedTiledMapTile) -> 'AnimatedTiledMapTile':
        return AnimatedTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimatedTiledMapTile):
        """
        Dynamic initializer for AnimatedTiledMapTile.
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
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetX()"""
        return float.__wrap(super(AnimatedTiledMapTile, self).getOffsetX())

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetY(float)"""
        super(__AnimatedTiledMapTile, self).setOffsetY(__float.valueOf(arg0))

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetX(float)"""
        super(__AnimatedTiledMapTile, self).setOffsetX(__float.valueOf(arg0))

    @overload
    def getAnimationIntervals(self) -> List[int]:
        """public int[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getAnimationIntervals()"""
        return List[int].__wrap(super(AnimatedTiledMapTile, self).getAnimationIntervals())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAnimationIntervals(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setAnimationIntervals(int[])"""
        super(__AnimatedTiledMapTile, self).setAnimationIntervals(arg0)

    @overload
    def getCurrentFrameIndex(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrameIndex()"""
        return int.__wrap(super(AnimatedTiledMapTile, self).getCurrentFrameIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetY()"""
        return float.__wrap(super(AnimatedTiledMapTile, self).getOffsetY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getId()"""
        return int.__wrap(super(AnimatedTiledMapTile, self).getId())

    @override
    @overload
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(__AnimatedTiledMapTile, self).setBlendMode(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setId(int)"""
        super(__AnimatedTiledMapTile, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(AnimatedTiledMapTile, self).getTextureRegion())

    @overload
    def __init__(self, arg0: 'IntArray', arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(com.badlogic.gdx.utils.IntArray,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = __AnimatedTiledMapTile(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__AnimatedTiledMapTile, self).setTextureRegion(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(float,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = __AnimatedTiledMapTile(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFrameTiles(self) -> List['StaticTiledMapTile']:
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getFrameTiles()"""
        return List['StaticTiledMapTile'].__wrap(super(AnimatedTiledMapTile, self).getFrameTiles())

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'.__wrap(super(AnimatedTiledMapTile, self).getBlendMode())

    @overload
    def getCurrentFrame(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrame()"""
        return 'tiled.TiledMapTile'.__wrap(super(AnimatedTiledMapTile, self).getCurrentFrame())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getObjects()"""
        return 'maps.MapObjects'.__wrap(super(AnimatedTiledMapTile, self).getObjects())

        @staticmethod
        @overload
        def updateAnimationBaseTime():
            """public static void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.updateAnimationBaseTime()"""
            __AnimatedTiledMapTile.updateAnimationBaseTime()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(AnimatedTiledMapTile, self).getProperties())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile as __AnimatedTiledMapTile
__AnimatedTiledMapTile = __AnimatedTiledMapTile
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile_BlendMode
__BlendMode = __TiledMapTile_BlendMode.BlendMode
from builtins import bool
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as __StaticTiledMapTile
__StaticTiledMapTile = __StaticTiledMapTile
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

from typing import List
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class AnimatedTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile"""
 
    @staticmethod
    def __wrap(java_value: __AnimatedTiledMapTile) -> 'AnimatedTiledMapTile':
        return AnimatedTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnimatedTiledMapTile):
        """
        Dynamic initializer for AnimatedTiledMapTile.
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
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetX()"""
        return float.__wrap(super(AnimatedTiledMapTile, self).getOffsetX())

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetY(float)"""
        super(__AnimatedTiledMapTile, self).setOffsetY(__float.valueOf(arg0))

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetX(float)"""
        super(__AnimatedTiledMapTile, self).setOffsetX(__float.valueOf(arg0))

    @overload
    def getAnimationIntervals(self) -> List[int]:
        """public int[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getAnimationIntervals()"""
        return List[int].__wrap(super(AnimatedTiledMapTile, self).getAnimationIntervals())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAnimationIntervals(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setAnimationIntervals(int[])"""
        super(__AnimatedTiledMapTile, self).setAnimationIntervals(arg0)

    @overload
    def getCurrentFrameIndex(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrameIndex()"""
        return int.__wrap(super(AnimatedTiledMapTile, self).getCurrentFrameIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetY()"""
        return float.__wrap(super(AnimatedTiledMapTile, self).getOffsetY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getId()"""
        return int.__wrap(super(AnimatedTiledMapTile, self).getId())

    @override
    @overload
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(__AnimatedTiledMapTile, self).setBlendMode(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setId(int)"""
        super(__AnimatedTiledMapTile, self).setId(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(AnimatedTiledMapTile, self).getTextureRegion())

    @overload
    def __init__(self, arg0: 'IntArray', arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(com.badlogic.gdx.utils.IntArray,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = __AnimatedTiledMapTile(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__AnimatedTiledMapTile, self).setTextureRegion(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(float,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = __AnimatedTiledMapTile(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFrameTiles(self) -> List['StaticTiledMapTile']:
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getFrameTiles()"""
        return List['StaticTiledMapTile'].__wrap(super(AnimatedTiledMapTile, self).getFrameTiles())

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'.__wrap(super(AnimatedTiledMapTile, self).getBlendMode())

    @overload
    def getCurrentFrame(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrame()"""
        return 'tiled.TiledMapTile'.__wrap(super(AnimatedTiledMapTile, self).getCurrentFrame())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getObjects()"""
        return 'maps.MapObjects'.__wrap(super(AnimatedTiledMapTile, self).getObjects())

        @staticmethod
        @overload
        def updateAnimationBaseTime():
            """public static void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.updateAnimationBaseTime()"""
            __AnimatedTiledMapTile.updateAnimationBaseTime()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(AnimatedTiledMapTile, self).getProperties())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as __StaticTiledMapTile
__StaticTiledMapTile = __StaticTiledMapTile
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
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
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile_BlendMode
__BlendMode = __TiledMapTile_BlendMode.BlendMode
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = __import_once__("pygdx.maps.tiled")

 
class StaticTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile"""
 
    @staticmethod
    def __wrap(java_value: __StaticTiledMapTile) -> 'StaticTiledMapTile':
        return StaticTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StaticTiledMapTile):
        """
        Dynamic initializer for StaticTiledMapTile.
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

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getOffsetY()"""
        return float.__wrap(super(StaticTiledMapTile, self).getOffsetY())

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(StaticTiledMapTile, self).getProperties())

    @override
    @overload
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(__StaticTiledMapTile, self).setBlendMode(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setOffsetY(float)"""
        super(__StaticTiledMapTile, self).setOffsetY(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __StaticTiledMapTile(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setOffsetX(float)"""
        super(__StaticTiledMapTile, self).setOffsetX(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setId(int)"""
        super(__StaticTiledMapTile, self).setId(__int.valueOf(arg0))

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
    def __init__(self, arg0: 'StaticTiledMapTile'):
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile(com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile)"""
        val = __StaticTiledMapTile(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getId()"""
        return int.__wrap(super(StaticTiledMapTile, self).getId())

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__StaticTiledMapTile, self).setTextureRegion(arg0)

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getObjects()"""
        return 'maps.MapObjects'.__wrap(super(StaticTiledMapTile, self).getObjects())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getOffsetX()"""
        return float.__wrap(super(StaticTiledMapTile, self).getOffsetX())

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'.__wrap(super(StaticTiledMapTile, self).getBlendMode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(StaticTiledMapTile, self).getTextureRegion())