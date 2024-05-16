from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.TiledMapTileSet as __TiledMapTileSet
__TiledMapTileSet = __TiledMapTileSet
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TiledMapTileSet(__Iterable, Iterable):
    """com.badlogic.gdx.maps.tiled.TiledMapTileSet"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileSet) -> 'TiledMapTileSet':
        return TiledMapTileSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileSet):
        """
        Dynamic initializer for TiledMapTileSet.
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
        """public java.util.Iterator<com.badlogic.gdx.maps.tiled.TiledMapTile> com.badlogic.gdx.maps.tiled.TiledMapTileSet.iterator()"""
        return 'Iterator'.__wrap(super(TiledMapTileSet, self).iterator())

    @overload
    def putTile(self, arg0: int, arg1: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.putTile(int,com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(__TiledMapTileSet, self).putTile(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = __TiledMapTileSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = __TiledMapTileSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.TiledMapTileSet.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(TiledMapTileSet, self).getProperties())

    @overload
    def getTile(self, arg0: int) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileSet.getTile(int)"""
        return 'TiledMapTile'.__wrap(super(__TiledMapTileSet, self).getTile(__int.valueOf(arg0)))

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.setName(java.lang.String)"""
        super(__TiledMapTileSet, self).setName(arg0)

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileSet.size()"""
        return int.__wrap(super(TiledMapTileSet, self).size())

    @overload
    def removeTile(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.removeTile(int)"""
        super(__TiledMapTileSet, self).removeTile(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.tiled.TiledMapTileSet.getName()"""
        return str.__wrap(super(TiledMapTileSet, self).getName())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileSet
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.MapProperties as __MapProperties
__MapProperties = __MapProperties
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.TiledMapTileSet as __TiledMapTileSet
__TiledMapTileSet = __TiledMapTileSet
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TiledMapTileSet(__Iterable, Iterable):
    """com.badlogic.gdx.maps.tiled.TiledMapTileSet"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileSet) -> 'TiledMapTileSet':
        return TiledMapTileSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileSet):
        """
        Dynamic initializer for TiledMapTileSet.
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
        """public java.util.Iterator<com.badlogic.gdx.maps.tiled.TiledMapTile> com.badlogic.gdx.maps.tiled.TiledMapTileSet.iterator()"""
        return 'Iterator'.__wrap(super(TiledMapTileSet, self).iterator())

    @overload
    def putTile(self, arg0: int, arg1: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.putTile(int,com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(__TiledMapTileSet, self).putTile(__int.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = __TiledMapTileSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = __TiledMapTileSet()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.TiledMapTileSet.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(TiledMapTileSet, self).getProperties())

    @overload
    def getTile(self, arg0: int) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileSet.getTile(int)"""
        return 'TiledMapTile'.__wrap(super(__TiledMapTileSet, self).getTile(__int.valueOf(arg0)))

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.setName(java.lang.String)"""
        super(__TiledMapTileSet, self).setName(arg0)

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileSet.size()"""
        return int.__wrap(super(TiledMapTileSet, self).size())

    @overload
    def removeTile(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.removeTile(int)"""
        super(__TiledMapTileSet, self).removeTile(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.tiled.TiledMapTileSet.getName()"""
        return str.__wrap(super(TiledMapTileSet, self).getName())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileSet 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as __AsynchronousAssetLoader
__AsynchronousAssetLoader = __AsynchronousAssetLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as __AtlasTmxMapLoader
__AtlasTmxMapLoader = __AtlasTmxMapLoader
from typing import List
import java.lang.Long as __long
import com.badlogic.gdx.utils.IntMap as __IntMap
__IntMap = __IntMap
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
import java.lang.Integer as __int
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as __BaseTmxMapLoader
__BaseTmxMapLoader = __BaseTmxMapLoader
from builtins import int
 
class AtlasTmxMapLoader(__BaseTmxMapLoader, BaseTmxMapLoader):
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader"""
 
    @staticmethod
    def __wrap(java_value: __AtlasTmxMapLoader) -> 'AtlasTmxMapLoader':
        return AtlasTmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtlasTmxMapLoader):
        """
        Dynamic initializer for AtlasTmxMapLoader.
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
    def load(self, arg0: str, arg1: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'.__wrap(super(__AtlasTmxMapLoader, self).load(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'.__wrap(super(__AtlasTmxMapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = __AtlasTmxMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'.__wrap(super(BaseTmxMapLoader, self).getIdToObject())

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

    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int].__wrap(__BaseTmxMapLoader.getTileIds(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String)"""
        return 'TiledMap'.__wrap(super(__AtlasTmxMapLoader, self).load(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = __AtlasTmxMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __AtlasTmxMapLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters'):
        """public void com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        super(__AtlasTmxMapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'.__wrap(super(__BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as __BaseTmxMapLoader_Parameters
__Parameters = __BaseTmxMapLoader_Parameters.Parameters
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Parameters(pygdx.__AssetLoaderParameters, assets.AssetLoaderParameters):
    """com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.Parameters"""
 
    @staticmethod
    def __wrap(java_value: __Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parameters):
        """
        Dynamic initializer for Parameters.
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
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters()"""
        val = __Parameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters()"""
        val = __Parameters()
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileSets
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.TiledMapTileSets as __TiledMapTileSets
__TiledMapTileSets = __TiledMapTileSets
import com.badlogic.gdx.maps.tiled.TiledMapTileSet as __TiledMapTileSet
__TiledMapTileSet = __TiledMapTileSet
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TiledMapTileSets(__Iterable, Iterable):
    """com.badlogic.gdx.maps.tiled.TiledMapTileSets"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileSets) -> 'TiledMapTileSets':
        return TiledMapTileSets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileSets):
        """
        Dynamic initializer for TiledMapTileSets.
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
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets()"""
        val = __TiledMapTileSets()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTileSet(self, arg0: str) -> 'TiledMapTileSet':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTileSet(java.lang.String)"""
        return 'TiledMapTileSet'.__wrap(super(__TiledMapTileSets, self).getTileSet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.tiled.TiledMapTileSet> com.badlogic.gdx.maps.tiled.TiledMapTileSets.iterator()"""
        return 'Iterator'.__wrap(super(TiledMapTileSets, self).iterator())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets()"""
        val = __TiledMapTileSets()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeTileSet(self, arg0: 'TiledMapTileSet'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.removeTileSet(com.badlogic.gdx.maps.tiled.TiledMapTileSet)"""
        super(__TiledMapTileSets, self).removeTileSet(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addTileSet(self, arg0: 'TiledMapTileSet'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.addTileSet(com.badlogic.gdx.maps.tiled.TiledMapTileSet)"""
        super(__TiledMapTileSets, self).addTileSet(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getTileSet(self, arg0: int) -> 'TiledMapTileSet':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTileSet(int)"""
        return 'TiledMapTileSet'.__wrap(super(__TiledMapTileSets, self).getTileSet(__int.valueOf(arg0)))

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
    def removeTileSet(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.removeTileSet(int)"""
        super(__TiledMapTileSets, self).removeTileSet(__int.valueOf(arg0))

    @overload
    def getTile(self, arg0: int) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTile(int)"""
        return 'TiledMapTile'.__wrap(super(__TiledMapTileSets, self).getTile(__int.valueOf(arg0)))

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileLayer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as __TiledMapTileLayer_Cell
__Cell = __TiledMapTileLayer_Cell.Cell
import com.badlogic.gdx.maps.MapObjects as __MapObjects
__MapObjects = __MapObjects
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

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
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as __TiledMapTileLayer
__TiledMapTileLayer = __TiledMapTileLayer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TiledMapTileLayer(pygdx.__MapLayer, maps.MapLayer):
    """com.badlogic.gdx.maps.tiled.TiledMapTileLayer"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTileLayer) -> 'TiledMapTileLayer':
        return TiledMapTileLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTileLayer):
        """
        Dynamic initializer for TiledMapTileLayer.
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
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(__maps.MapLayer, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def setCell(self, arg0: int, arg1: int, arg2: 'Cell'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileLayer.setCell(int,int,com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell)"""
        super(__TiledMapTileLayer, self).setCell(__int.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float.__wrap(super(maps.MapLayer, self).getOffsetX())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str.__wrap(super(maps.MapLayer, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getWidth()"""
        return int.__wrap(super(TiledMapTileLayer, self).getWidth())

    @override
    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapLayer.invalidateRenderOffset()"""
        super(maps.MapLayer, self).invalidateRenderOffset()

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(__maps.MapLayer, self).setParallaxX(__float.valueOf(arg0))

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(__maps.MapLayer, self).setOffsetY(__float.valueOf(arg0))

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(__maps.MapLayer, self).setParent(arg0)

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float.__wrap(super(maps.MapLayer, self).getOffsetY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float.__wrap(super(maps.MapLayer, self).getParallaxY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getTileWidth(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getTileWidth()"""
        return int.__wrap(super(TiledMapTileLayer, self).getTileWidth())

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getHeight()"""
        return int.__wrap(super(TiledMapTileLayer, self).getHeight())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float.__wrap(super(maps.MapLayer, self).getOpacity())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getTileHeight(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getTileHeight()"""
        return int.__wrap(super(TiledMapTileLayer, self).getTileHeight())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(__maps.MapLayer, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getCell(self, arg0: int, arg1: int) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getCell(int,int)"""
        return 'Cell'.__wrap(super(__TiledMapTileLayer, self).getCell(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(__maps.MapLayer, self).setName(arg0)

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(__maps.MapLayer, self).setParallaxY(__float.valueOf(arg0))

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'maps.MapObjects'.__wrap(super(maps.MapLayer, self).getObjects())

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float.__wrap(super(maps.MapLayer, self).getRenderOffsetX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float.__wrap(super(maps.MapLayer, self).getParallaxX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getParent(self) -> 'maps.MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'maps.MapLayer'.__wrap(super(maps.MapLayer, self).getParent())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool.__wrap(super(maps.MapLayer, self).isVisible())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer(int,int,int,int)"""
        val = __TiledMapTileLayer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapLayer, self).getProperties())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(__maps.MapLayer, self).setOffsetX(__float.valueOf(arg0))

    @override
    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float.__wrap(super(maps.MapLayer, self).getRenderOffsetY()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
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
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as __AtlasTmxMapLoader_AtlasResolver_AssetManagerAtlasResolver
__AssetManagerAtlasResolver = __AtlasTmxMapLoader_AtlasResolver_AssetManagerAtlasResolver.AtlasResolver.AssetManagerAtlasResolver
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetManagerAtlasResolver(__AtlasResolver, AtlasResolver):
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver.AssetManagerAtlasResolver"""
 
    @staticmethod
    def __wrap(java_value: __AssetManagerAtlasResolver) -> 'AssetManagerAtlasResolver':
        return AssetManagerAtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetManagerAtlasResolver):
        """
        Dynamic initializer for AssetManagerAtlasResolver.
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
    def __init__(self, arg0: 'AssetManager', arg1: str):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver(com.badlogic.gdx.assets.AssetManager,java.lang.String)"""
        val = __AssetManagerAtlasResolver(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__AssetManagerAtlasResolver, self).getImage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getAtlas(self) -> 'g2d.TextureAtlas':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver.getAtlas()"""
        return 'g2d.TextureAtlas'.__wrap(super(AssetManagerAtlasResolver, self).getAtlas())

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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.BaseTmxMapLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as __AsynchronousAssetLoader
__AsynchronousAssetLoader = __AsynchronousAssetLoader
from abc import abstractmethod, ABC
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

from typing import List
import java.lang.Long as __long
import com.badlogic.gdx.utils.IntMap as __IntMap
__IntMap = __IntMap
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as __BaseTmxMapLoader
__BaseTmxMapLoader = __BaseTmxMapLoader
from builtins import bool
from builtins import int
 
class BaseTmxMapLoader(ABC, assets.__AsynchronousAssetLoader, loaders.AsynchronousAssetLoader):
    """com.badlogic.gdx.maps.tiled.BaseTmxMapLoader"""
 
    @staticmethod
    def __wrap(java_value: __BaseTmxMapLoader) -> 'BaseTmxMapLoader':
        return BaseTmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseTmxMapLoader):
        """
        Dynamic initializer for BaseTmxMapLoader.
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public abstract void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @abstractmethod
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public abstract T com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'.__wrap(super(BaseTmxMapLoader, self).getIdToObject())

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

    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int].__wrap(__BaseTmxMapLoader.getTileIds(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __BaseTmxMapLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'.__wrap(super(__BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.maps.tiled.TmxMapLoader as __TmxMapLoader_Parameters
__Parameters = __TmxMapLoader_Parameters.Parameters
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Parameters(__Parameters, Parameters):
    """com.badlogic.gdx.maps.tiled.TmxMapLoader.Parameters"""
 
    @staticmethod
    def __wrap(java_value: __Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parameters):
        """
        Dynamic initializer for Parameters.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters()"""
        val = __Parameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters()"""
        val = __Parameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTile
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from abc import abstractmethod, ABC
 
class TiledMapTile(ABC):
    """com.badlogic.gdx.maps.tiled.TiledMapTile"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapTile) -> 'TiledMapTile':
        return TiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapTile):
        """
        Dynamic initializer for TiledMapTile.
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
    def setBlendMode(self, arg0: 'BlendMode'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapTile.setBlendMode(com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode)"""
        pass

    @abstractmethod
    def getBlendMode(self, ):
        """public abstract com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.TiledMapTile.getBlendMode()"""
        pass

    @abstractmethod
    def setOffsetX(self, arg0: float):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapTile.setOffsetX(float)"""
        pass

    @abstractmethod
    def getObjects(self, ):
        """public abstract com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.tiled.TiledMapTile.getObjects()"""
        pass

    @abstractmethod
    def setId(self, arg0: int):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapTile.setId(int)"""
        pass

    @abstractmethod
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapTile.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        pass

    @abstractmethod
    def getOffsetX(self, ):
        """public abstract float com.badlogic.gdx.maps.tiled.TiledMapTile.getOffsetX()"""
        pass

    @abstractmethod
    def getOffsetY(self, ):
        """public abstract float com.badlogic.gdx.maps.tiled.TiledMapTile.getOffsetY()"""
        pass

    @abstractmethod
    def getId(self, ):
        """public abstract int com.badlogic.gdx.maps.tiled.TiledMapTile.getId()"""
        pass

    @abstractmethod
    def setOffsetY(self, arg0: float):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapTile.setOffsetY(float)"""
        pass

    @abstractmethod
    def getProperties(self, ):
        """public abstract com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.TiledMapTile.getProperties()"""
        pass

    @abstractmethod
    def getTextureRegion(self, ):
        """public abstract com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.TiledMapTile.getTextureRegion()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

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
import com.badlogic.gdx.maps.tiled.TiledMapTileSets as __TiledMapTileSets
__TiledMapTileSets = __TiledMapTileSets
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TiledMap(pygdx.__Map, maps.Map):
    """com.badlogic.gdx.maps.tiled.TiledMap"""
 
    @staticmethod
    def __wrap(java_value: __TiledMap) -> 'TiledMap':
        return TiledMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMap):
        """
        Dynamic initializer for TiledMap.
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
    def setOwnedResources(self, arg0: 'Array'):
        """public void com.badlogic.gdx.maps.tiled.TiledMap.setOwnedResources(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.utils.Disposable>)"""
        super(__TiledMap, self).setOwnedResources(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.TiledMap.dispose()"""
        super(TiledMap, self).dispose()

    @override
    @overload
    def getLayers(self) -> 'maps.MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.Map.getLayers()"""
        return 'maps.MapLayers'.__wrap(super(maps.Map, self).getLayers())

    @overload
    def getTileSets(self) -> 'TiledMapTileSets':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets com.badlogic.gdx.maps.tiled.TiledMap.getTileSets()"""
        return 'TiledMapTileSets'.__wrap(super(TiledMap, self).getTileSets())

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
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.Map.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.Map, self).getProperties())

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
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMap()"""
        val = __TiledMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMap()"""
        val = __TiledMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as __TiledMapTileLayer_Cell
__Cell = __TiledMapTileLayer_Cell.Cell
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile
__TiledMapTile = __TiledMapTile
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Cell():
    """com.badlogic.gdx.maps.tiled.TiledMapTileLayer.Cell"""
 
    @staticmethod
    def __wrap(java_value: __Cell) -> 'Cell':
        return Cell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cell):
        """
        Dynamic initializer for Cell.
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
    def getFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getFlipVertically()"""
        return bool.__wrap(super(Cell, self).getFlipVertically())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell()"""
        val = __Cell()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell()"""
        val = __Cell()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFlipHorizontally(self, arg0: bool) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setFlipHorizontally(boolean)"""
        return 'Cell'.__wrap(super(__Cell, self).setFlipHorizontally(__boolean.valueOf(arg0)))

    @overload
    def getFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getFlipHorizontally()"""
        return bool.__wrap(super(Cell, self).getFlipHorizontally())

    @overload
    def getTile(self) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getTile()"""
        return 'TiledMapTile'.__wrap(super(Cell, self).getTile())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setTile(self, arg0: 'TiledMapTile') -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        return 'Cell'.__wrap(super(__Cell, self).setTile(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setRotation(self, arg0: int) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setRotation(int)"""
        return 'Cell'.__wrap(super(__Cell, self).setRotation(__int.valueOf(arg0)))

    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getRotation()"""
        return int.__wrap(super(Cell, self).getRotation())

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
    def setFlipVertically(self, arg0: bool) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setFlipVertically(boolean)"""
        return 'Cell'.__wrap(super(__Cell, self).setFlipVertically(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as __AtlasTmxMapLoader_AtlasResolver_DirectAtlasResolver
__DirectAtlasResolver = __AtlasTmxMapLoader_AtlasResolver_DirectAtlasResolver.AtlasResolver.DirectAtlasResolver
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
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
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DirectAtlasResolver(__AtlasResolver, AtlasResolver):
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver.DirectAtlasResolver"""
 
    @staticmethod
    def __wrap(java_value: __DirectAtlasResolver) -> 'DirectAtlasResolver':
        return DirectAtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectAtlasResolver):
        """
        Dynamic initializer for DirectAtlasResolver.
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

    @override
    @overload
    def getAtlas(self) -> 'g2d.TextureAtlas':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver.getAtlas()"""
        return 'g2d.TextureAtlas'.__wrap(super(DirectAtlasResolver, self).getAtlas())

    @overload
    def __init__(self, arg0: 'TextureAtlas'):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        val = __DirectAtlasResolver(arg0)
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
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'.__wrap(super(__DirectAtlasResolver, self).getImage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TmxMapLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as __AsynchronousAssetLoader
__AsynchronousAssetLoader = __AsynchronousAssetLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from typing import List
import java.lang.Long as __long
import com.badlogic.gdx.utils.IntMap as __IntMap
__IntMap = __IntMap
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
import com.badlogic.gdx.maps.tiled.TmxMapLoader as __TmxMapLoader
__TmxMapLoader = __TmxMapLoader
import java.lang.Integer as __int
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as __BaseTmxMapLoader
__BaseTmxMapLoader = __BaseTmxMapLoader
from builtins import int
 
class TmxMapLoader(__BaseTmxMapLoader, BaseTmxMapLoader):
    """com.badlogic.gdx.maps.tiled.TmxMapLoader"""
 
    @staticmethod
    def __wrap(java_value: __TmxMapLoader) -> 'TmxMapLoader':
        return TmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TmxMapLoader):
        """
        Dynamic initializer for TmxMapLoader.
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters'):
        """public void com.badlogic.gdx.maps.tiled.TmxMapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        super(__TmxMapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.load(java.lang.String)"""
        return 'TiledMap'.__wrap(super(__TmxMapLoader, self).load(arg0))

    @override
    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'.__wrap(super(BaseTmxMapLoader, self).getIdToObject())

    @overload
    def load(self, arg0: str, arg1: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.load(java.lang.String,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        return 'TiledMap'.__wrap(super(__TmxMapLoader, self).load(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader()"""
        val = __TmxMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int].__wrap(__BaseTmxMapLoader.getTileIds(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader()"""
        val = __TmxMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        return 'TiledMap'.__wrap(super(__TmxMapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __TmxMapLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'.__wrap(super(__BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapRenderer
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.maps.tiled.TiledMapRenderer as __TiledMapRenderer
__TiledMapRenderer = __TiledMapRenderer
import com.badlogic.gdx.maps.MapRenderer as __MapRenderer
__MapRenderer = __MapRenderer
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import maps
except ImportError:
    maps = __import_once__("pygdx.maps")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class TiledMapRenderer(ABC, pygdx.__MapRenderer, maps.MapRenderer):
    """com.badlogic.gdx.maps.tiled.TiledMapRenderer"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapRenderer) -> 'TiledMapRenderer':
        return TiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapRenderer):
        """
        Dynamic initializer for TiledMapRenderer.
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
    def renderImageLayer(self, arg0: 'TiledMapImageLayer'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderImageLayer(com.badlogic.gdx.maps.tiled.TiledMapImageLayer)"""
        pass

    @abstractmethod
    def setView(self, arg0: 'Matrix4', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.math.Matrix4,float,float,float,float)"""
        pass

    @abstractmethod
    def renderObjects(self, arg0: 'MapLayer'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderObjects(com.badlogic.gdx.maps.MapLayer)"""
        pass

    @abstractmethod
    def renderObject(self, arg0: 'MapObject'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderObject(com.badlogic.gdx.maps.MapObject)"""
        pass

    @abstractmethod
    def render(self, arg0: 'int'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render(int[])"""
        pass

    @abstractmethod
    def renderTileLayer(self, arg0: 'TiledMapTileLayer'):
        """public abstract void com.badlogic.gdx.maps.tiled.TiledMapRenderer.renderTileLayer(com.badlogic.gdx.maps.tiled.TiledMapTileLayer)"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render()"""
        pass

    @abstractmethod
    def setView(self, arg0: 'OrthographicCamera'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as __AtlasTmxMapLoader_AtlasResolver
__AtlasResolver = __AtlasTmxMapLoader_AtlasResolver.AtlasResolver
from abc import abstractmethod, ABC
import com.badlogic.gdx.maps.ImageResolver as __ImageResolver
__ImageResolver = __ImageResolver
 
class AtlasResolver(ABC, pygdx.__ImageResolver, maps.ImageResolver):
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver"""
 
    @staticmethod
    def __wrap(java_value: __AtlasResolver) -> 'AtlasResolver':
        return AtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtlasResolver):
        """
        Dynamic initializer for AtlasResolver.
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
    def getAtlas(self, ):
        """public abstract com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver.getAtlas()"""
        pass

    @abstractmethod
    def getImage(self, arg0: str):
        """public abstract com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.ImageResolver.getImage(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.maps.tiled.TideMapLoader as __TideMapLoader_Parameters
__Parameters = __TideMapLoader_Parameters.Parameters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Parameters(pygdx.__AssetLoaderParameters, assets.AssetLoaderParameters):
    """com.badlogic.gdx.maps.tiled.TideMapLoader.Parameters"""
 
    @staticmethod
    def __wrap(java_value: __Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parameters):
        """
        Dynamic initializer for Parameters.
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
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters()"""
        val = __Parameters()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters()"""
        val = __Parameters()
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapImageLayer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
import com.badlogic.gdx.maps.tiled.TiledMapImageLayer as __TiledMapImageLayer
__TiledMapImageLayer = __TiledMapImageLayer
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
 
class TiledMapImageLayer(pygdx.__MapLayer, maps.MapLayer):
    """com.badlogic.gdx.maps.tiled.TiledMapImageLayer"""
 
    @staticmethod
    def __wrap(java_value: __TiledMapImageLayer) -> 'TiledMapImageLayer':
        return TiledMapImageLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledMapImageLayer):
        """
        Dynamic initializer for TiledMapImageLayer.
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
    def __init__(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public com.badlogic.gdx.maps.tiled.TiledMapImageLayer(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        val = __TiledMapImageLayer(arg0, __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(__maps.MapLayer, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float.__wrap(super(maps.MapLayer, self).getOffsetX())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str.__wrap(super(maps.MapLayer, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def invalidateRenderOffset(self):
        """public void com.badlogic.gdx.maps.MapLayer.invalidateRenderOffset()"""
        super(maps.MapLayer, self).invalidateRenderOffset()

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(__maps.MapLayer, self).setParallaxX(__float.valueOf(arg0))

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(__maps.MapLayer, self).setOffsetY(__float.valueOf(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getX()"""
        return float.__wrap(super(TiledMapImageLayer, self).getX())

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TiledMapImageLayer, self).setTextureRegion(arg0)

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(__maps.MapLayer, self).setParent(arg0)

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float.__wrap(super(maps.MapLayer, self).getOffsetY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float.__wrap(super(maps.MapLayer, self).getParallaxY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float.__wrap(super(maps.MapLayer, self).getOpacity())

    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(TiledMapImageLayer, self).getTextureRegion())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(__maps.MapLayer, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(__maps.MapLayer, self).setName(arg0)

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(__maps.MapLayer, self).setParallaxY(__float.valueOf(arg0))

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'maps.MapObjects'.__wrap(super(maps.MapLayer, self).getObjects())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getY()"""
        return float.__wrap(super(TiledMapImageLayer, self).getY())

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float.__wrap(super(maps.MapLayer, self).getRenderOffsetX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float.__wrap(super(maps.MapLayer, self).getParallaxX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setY(float)"""
        super(__TiledMapImageLayer, self).setY(__float.valueOf(arg0))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setX(float)"""
        super(__TiledMapImageLayer, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def getParent(self) -> 'maps.MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'maps.MapLayer'.__wrap(super(maps.MapLayer, self).getParent())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool.__wrap(super(maps.MapLayer, self).isVisible())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'maps.MapProperties'.__wrap(super(maps.MapLayer, self).getProperties())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(__maps.MapLayer, self).setOffsetX(__float.valueOf(arg0))

    @override
    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float.__wrap(super(maps.MapLayer, self).getRenderOffsetY()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TideMapLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
import com.badlogic.gdx.maps.tiled.TideMapLoader as __TideMapLoader
__TideMapLoader = __TideMapLoader
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.maps.tiled.TiledMap as __TiledMap
__TiledMap = __TiledMap
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TideMapLoader(assets.__SynchronousAssetLoader, loaders.SynchronousAssetLoader):
    """com.badlogic.gdx.maps.tiled.TideMapLoader"""
 
    @staticmethod
    def __wrap(java_value: __TideMapLoader) -> 'TideMapLoader':
        return TideMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TideMapLoader):
        """
        Dynamic initializer for TideMapLoader.
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @overload
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TideMapLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters)"""
        return 'TiledMap'.__wrap(super(__TideMapLoader, self).load(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.TideMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters)"""
        return 'utils.Array'.__wrap(super(__TideMapLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TideMapLoader.load(java.lang.String)"""
        return 'TiledMap'.__wrap(super(__TideMapLoader, self).load(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __TideMapLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader()"""
        val = __TideMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader()"""
        val = __TideMapLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as __AtlasTmxMapLoader_AtlasTiledMapLoaderParameters
__AtlasTiledMapLoaderParameters = __AtlasTmxMapLoader_AtlasTiledMapLoaderParameters.AtlasTiledMapLoaderParameters
from builtins import int
 
class AtlasTiledMapLoaderParameters(__Parameters, Parameters):
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasTiledMapLoaderParameters"""
 
    @staticmethod
    def __wrap(java_value: __AtlasTiledMapLoaderParameters) -> 'AtlasTiledMapLoaderParameters':
        return AtlasTiledMapLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtlasTiledMapLoaderParameters):
        """
        Dynamic initializer for AtlasTiledMapLoaderParameters.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters()"""
        val = __AtlasTiledMapLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters()"""
        val = __AtlasTiledMapLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.maps.tiled.TiledMapTile as __TiledMapTile_BlendMode
__BlendMode = __TiledMapTile_BlendMode.BlendMode
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BlendMode(__Enum, Enum):
    """com.badlogic.gdx.maps.tiled.TiledMapTile.BlendMode"""
 
    @staticmethod
    def __wrap(java_value: __BlendMode) -> 'BlendMode':
        return BlendMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlendMode):
        """
        Dynamic initializer for BlendMode.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BlendMode':
        """public static com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode.valueOf(java.lang.String)"""
        return BlendMode.__wrap(__BlendMode.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['BlendMode']:
        """public static com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode[] com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode.values()"""
        return List[BlendMode].__wrap(__BlendMode.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())