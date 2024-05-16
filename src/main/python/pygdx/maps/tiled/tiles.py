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
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile_BlendMode
_BlendMode = _TiledMapTile_BlendMode.BlendMode
import com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile as _AnimatedTiledMapTile
_AnimatedTiledMapTile = _AnimatedTiledMapTile
import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as _StaticTiledMapTile
_StaticTiledMapTile = _StaticTiledMapTile
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
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
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnimatedTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile"""
 
    @staticmethod
    def _wrap(java_value: _AnimatedTiledMapTile) -> 'AnimatedTiledMapTile':
        return AnimatedTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimatedTiledMapTile):
        """
        Dynamic initializer for AnimatedTiledMapTile.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimatedTiledMapTile__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimatedTiledMapTile__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetX(float)"""
        super(_AnimatedTiledMapTile, self).setOffsetX(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getId()"""
        return int._wrap(super(AnimatedTiledMapTile, self).getId())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetX()"""
        return float._wrap(super(AnimatedTiledMapTile, self).getOffsetX())

    @overload
    def __init__(self, arg0: 'IntArray', arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(com.badlogic.gdx.utils.IntArray,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = _AnimatedTiledMapTile(arg0, arg1)
        self.__wrapper = val

    @overload
    def getAnimationIntervals(self) -> List[int]:
        """public int[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getAnimationIntervals()"""
        return List[int]._wrap(super(AnimatedTiledMapTile, self).getAnimationIntervals())

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(float,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = _AnimatedTiledMapTile(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetY()"""
        return float._wrap(super(AnimatedTiledMapTile, self).getOffsetY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetY(float)"""
        super(_AnimatedTiledMapTile, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'._wrap(super(AnimatedTiledMapTile, self).getBlendMode())

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getProperties()"""
        return 'maps.MapProperties'._wrap(super(AnimatedTiledMapTile, self).getProperties())

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_AnimatedTiledMapTile, self).setTextureRegion(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(AnimatedTiledMapTile, self).getTextureRegion())

        @staticmethod
        @overload
        def updateAnimationBaseTime():
            """public static void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.updateAnimationBaseTime()"""
            _AnimatedTiledMapTile.updateAnimationBaseTime()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCurrentFrame(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrame()"""
        return 'tiled.TiledMapTile'._wrap(super(AnimatedTiledMapTile, self).getCurrentFrame())

    @overload
    def setAnimationIntervals(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setAnimationIntervals(int[])"""
        super(_AnimatedTiledMapTile, self).setAnimationIntervals(arg0)

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getObjects()"""
        return 'maps.MapObjects'._wrap(super(AnimatedTiledMapTile, self).getObjects())

    @overload
    def getCurrentFrameIndex(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrameIndex()"""
        return int._wrap(super(AnimatedTiledMapTile, self).getCurrentFrameIndex())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFrameTiles(self) -> List['StaticTiledMapTile']:
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getFrameTiles()"""
        return List['StaticTiledMapTile']._wrap(super(AnimatedTiledMapTile, self).getFrameTiles())

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setId(int)"""
        super(_AnimatedTiledMapTile, self).setId(_int.valueOf(arg0))

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
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(_AnimatedTiledMapTile, self).setBlendMode(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile_BlendMode
_BlendMode = _TiledMapTile_BlendMode.BlendMode
import com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile as _AnimatedTiledMapTile
_AnimatedTiledMapTile = _AnimatedTiledMapTile
import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as _StaticTiledMapTile
_StaticTiledMapTile = _StaticTiledMapTile
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
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
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnimatedTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile"""
 
    @staticmethod
    def _wrap(java_value: _AnimatedTiledMapTile) -> 'AnimatedTiledMapTile':
        return AnimatedTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnimatedTiledMapTile):
        """
        Dynamic initializer for AnimatedTiledMapTile.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnimatedTiledMapTile__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnimatedTiledMapTile__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetX(float)"""
        super(_AnimatedTiledMapTile, self).setOffsetX(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getId()"""
        return int._wrap(super(AnimatedTiledMapTile, self).getId())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetX()"""
        return float._wrap(super(AnimatedTiledMapTile, self).getOffsetX())

    @overload
    def __init__(self, arg0: 'IntArray', arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(com.badlogic.gdx.utils.IntArray,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = _AnimatedTiledMapTile(arg0, arg1)
        self.__wrapper = val

    @overload
    def getAnimationIntervals(self) -> List[int]:
        """public int[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getAnimationIntervals()"""
        return List[int]._wrap(super(AnimatedTiledMapTile, self).getAnimationIntervals())

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile(float,com.badlogic.gdx.utils.Array<com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile>)"""
        val = _AnimatedTiledMapTile(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getOffsetY()"""
        return float._wrap(super(AnimatedTiledMapTile, self).getOffsetY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setOffsetY(float)"""
        super(_AnimatedTiledMapTile, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'._wrap(super(AnimatedTiledMapTile, self).getBlendMode())

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getProperties()"""
        return 'maps.MapProperties'._wrap(super(AnimatedTiledMapTile, self).getProperties())

    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_AnimatedTiledMapTile, self).setTextureRegion(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(AnimatedTiledMapTile, self).getTextureRegion())

        @staticmethod
        @overload
        def updateAnimationBaseTime():
            """public static void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.updateAnimationBaseTime()"""
            _AnimatedTiledMapTile.updateAnimationBaseTime()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCurrentFrame(self) -> 'tiled.TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrame()"""
        return 'tiled.TiledMapTile'._wrap(super(AnimatedTiledMapTile, self).getCurrentFrame())

    @overload
    def setAnimationIntervals(self, arg0: 'int'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setAnimationIntervals(int[])"""
        super(_AnimatedTiledMapTile, self).setAnimationIntervals(arg0)

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getObjects()"""
        return 'maps.MapObjects'._wrap(super(AnimatedTiledMapTile, self).getObjects())

    @overload
    def getCurrentFrameIndex(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getCurrentFrameIndex()"""
        return int._wrap(super(AnimatedTiledMapTile, self).getCurrentFrameIndex())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFrameTiles(self) -> List['StaticTiledMapTile']:
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile[] com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.getFrameTiles()"""
        return List['StaticTiledMapTile']._wrap(super(AnimatedTiledMapTile, self).getFrameTiles())

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setId(int)"""
        super(_AnimatedTiledMapTile, self).setId(_int.valueOf(arg0))

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
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(_AnimatedTiledMapTile, self).setBlendMode(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile
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
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile_BlendMode
_BlendMode = _TiledMapTile_BlendMode.BlendMode
from builtins import float
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile as _StaticTiledMapTile
_StaticTiledMapTile = _StaticTiledMapTile
import java.lang.Float as _float
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.Integer as _int
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
try:
    from pygdx.maps import tiled
except ImportError:
    tiled = _import_once("pygdx.maps.tiled")

import java.lang.Class as _Class
_Class = _Class
 
class StaticTiledMapTile():
    """com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile"""
 
    @staticmethod
    def _wrap(java_value: _StaticTiledMapTile) -> 'StaticTiledMapTile':
        return StaticTiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StaticTiledMapTile):
        """
        Dynamic initializer for StaticTiledMapTile.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StaticTiledMapTile__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StaticTiledMapTile__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_StaticTiledMapTile, self).setTextureRegion(arg0)

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getOffsetX()"""
        return float._wrap(super(StaticTiledMapTile, self).getOffsetX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setId(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setId(int)"""
        super(_StaticTiledMapTile, self).setId(_int.valueOf(arg0))

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setOffsetY(float)"""
        super(_StaticTiledMapTile, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getId(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getId()"""
        return int._wrap(super(StaticTiledMapTile, self).getId())

    @override
    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(StaticTiledMapTile, self).getTextureRegion())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setOffsetX(float)"""
        super(_StaticTiledMapTile, self).setOffsetX(_float.valueOf(arg0))

    @override
    @overload
    def setBlendMode(self, arg0: 'BlendMode'):
        """public void com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        super(_StaticTiledMapTile, self).setBlendMode(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getObjects()"""
        return 'maps.MapObjects'._wrap(super(StaticTiledMapTile, self).getObjects())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _StaticTiledMapTile(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'StaticTiledMapTile'):
        """public com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile(com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile)"""
        val = _StaticTiledMapTile(arg0)
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getProperties()"""
        return 'maps.MapProperties'._wrap(super(StaticTiledMapTile, self).getProperties())

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getOffsetY()"""
        return float._wrap(super(StaticTiledMapTile, self).getOffsetY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getBlendMode(self) -> 'tiled.TiledMapTile$BlendMode':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile.getBlendMode()"""
        return 'tiled.TiledMapTile$BlendMode'._wrap(super(StaticTiledMapTile, self).getBlendMode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())