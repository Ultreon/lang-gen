from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as _BaseTmxMapLoader
_BaseTmxMapLoader = _BaseTmxMapLoader
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader
_AtlasTmxMapLoader = _AtlasTmxMapLoader
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
import com.badlogic.gdx.utils.IntMap as _IntMap
_IntMap = _IntMap
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
from typing import List
import java.lang.Integer as _int
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtlasTmxMapLoader():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader"""
 
    @staticmethod
    def _wrap(java_value: _AtlasTmxMapLoader) -> 'AtlasTmxMapLoader':
        return AtlasTmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasTmxMapLoader):
        """
        Dynamic initializer for AtlasTmxMapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasTmxMapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasTmxMapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int]._wrap(_BaseTmxMapLoader.getTileIds(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).load(arg0))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'._wrap(super(BaseTmxMapLoader, self).getIdToObject())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = _AtlasTmxMapLoader()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = _AtlasTmxMapLoader()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _AtlasTmxMapLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def load(self, arg0: str, arg1: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).load(arg0, arg1))

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters'):
        """public void com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        super(_AtlasTmxMapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as _BaseTmxMapLoader
_BaseTmxMapLoader = _BaseTmxMapLoader
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader
_AtlasTmxMapLoader = _AtlasTmxMapLoader
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
import com.badlogic.gdx.utils.IntMap as _IntMap
_IntMap = _IntMap
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
from typing import List
import java.lang.Integer as _int
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtlasTmxMapLoader():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader"""
 
    @staticmethod
    def _wrap(java_value: _AtlasTmxMapLoader) -> 'AtlasTmxMapLoader':
        return AtlasTmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasTmxMapLoader):
        """
        Dynamic initializer for AtlasTmxMapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasTmxMapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasTmxMapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int]._wrap(_BaseTmxMapLoader.getTileIds(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).load(arg0))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'._wrap(super(BaseTmxMapLoader, self).getIdToObject())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = _AtlasTmxMapLoader()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader()"""
        val = _AtlasTmxMapLoader()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _AtlasTmxMapLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def load(self, arg0: str, arg1: 'AtlasTiledMapLoaderParameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.load(java.lang.String,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        return 'TiledMap'._wrap(super(_AtlasTmxMapLoader, self).load(arg0, arg1))

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AtlasTiledMapLoaderParameters'):
        """public void com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters)"""
        super(_AtlasTmxMapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile_BlendMode
_BlendMode = _TiledMapTile_BlendMode.BlendMode
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlendMode():
    """com.badlogic.gdx.maps.tiled.TiledMapTile.BlendMode"""
 
    @staticmethod
    def _wrap(java_value: _BlendMode) -> 'BlendMode':
        return BlendMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlendMode):
        """
        Dynamic initializer for BlendMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlendMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlendMode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BlendMode':
        """public static com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode.valueOf(java.lang.String)"""
        return BlendMode._wrap(_BlendMode.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['BlendMode']:
        """public static com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode[] com.badlogic.gdx.maps.tiled.TiledMapTile$BlendMode.values()"""
        return List[BlendMode]._wrap(_BlendMode.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.BaseTmxMapLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.utils.IntMap as _IntMap
_IntMap = _IntMap
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as _BaseTmxMapLoader
_BaseTmxMapLoader = _BaseTmxMapLoader
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseTmxMapLoader():
    """com.badlogic.gdx.maps.tiled.BaseTmxMapLoader"""
 
    @staticmethod
    def _wrap(java_value: _BaseTmxMapLoader) -> 'BaseTmxMapLoader':
        return BaseTmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseTmxMapLoader):
        """
        Dynamic initializer for BaseTmxMapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseTmxMapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseTmxMapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int]._wrap(_BaseTmxMapLoader.getTileIds(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'._wrap(super(BaseTmxMapLoader, self).getIdToObject())

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _BaseTmxMapLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters
from builtins import str
import com.badlogic.gdx.maps.tiled.TmxMapLoader as _TmxMapLoader_Parameters
_Parameters = _TmxMapLoader_Parameters.Parameters
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Parameters():
    """com.badlogic.gdx.maps.tiled.TmxMapLoader.Parameters"""
 
    @staticmethod
    def _wrap(java_value: _Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parameters):
        """
        Dynamic initializer for Parameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parameters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters()"""
        val = _Parameters()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters()"""
        val = _Parameters()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TideMapLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.maps.tiled.TideMapLoader as _TideMapLoader
_TideMapLoader = _TideMapLoader
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TideMapLoader():
    """com.badlogic.gdx.maps.tiled.TideMapLoader"""
 
    @staticmethod
    def _wrap(java_value: _TideMapLoader) -> 'TideMapLoader':
        return TideMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TideMapLoader):
        """
        Dynamic initializer for TideMapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TideMapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TideMapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader()"""
        val = _TideMapLoader()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.TideMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters)"""
        return 'utils.Array'._wrap(super(_TideMapLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _TideMapLoader(arg0)
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @overload
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TideMapLoader.load(java.lang.String)"""
        return 'TiledMap'._wrap(super(_TideMapLoader, self).load(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader()"""
        val = _TideMapLoader()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TideMapLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters)"""
        return 'TiledMap'._wrap(super(_TideMapLoader, self).load(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader_AtlasResolver
_AtlasResolver = _AtlasTmxMapLoader_AtlasResolver.AtlasResolver
import com.badlogic.gdx.maps.ImageResolver as _ImageResolver
_ImageResolver = _ImageResolver
from abc import abstractmethod, ABC
 
class AtlasResolver():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver"""
 
    @staticmethod
    def _wrap(java_value: _AtlasResolver) -> 'AtlasResolver':
        return AtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasResolver):
        """
        Dynamic initializer for AtlasResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileSet
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.tiled.TiledMapTileSet as _TiledMapTileSet
_TiledMapTileSet = _TiledMapTileSet
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapTileSet():
    """com.badlogic.gdx.maps.tiled.TiledMapTileSet"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTileSet) -> 'TiledMapTileSet':
        return TiledMapTileSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTileSet):
        """
        Dynamic initializer for TiledMapTileSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTileSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTileSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileSet.size()"""
        return int._wrap(super(TiledMapTileSet, self).size())

    @overload
    def getTile(self, arg0: int) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileSet.getTile(int)"""
        return 'TiledMapTile'._wrap(super(_TiledMapTileSet, self).getTile(_int.valueOf(arg0)))

    @overload
    def removeTile(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.removeTile(int)"""
        super(_TiledMapTileSet, self).removeTile(_int.valueOf(arg0))

    @overload
    def putTile(self, arg0: int, arg1: 'TiledMapTile'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.putTile(int,com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        super(_TiledMapTileSet, self).putTile(_int.valueOf(arg0), arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = _TiledMapTileSet()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet()"""
        val = _TiledMapTileSet()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.tiled.TiledMapTileSet.getName()"""
        return str._wrap(super(TiledMapTileSet, self).getName())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.tiled.TiledMapTile> com.badlogic.gdx.maps.tiled.TiledMapTileSet.iterator()"""
        return 'Iterator'._wrap(super(TiledMapTileSet, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.tiled.TiledMapTileSet.getProperties()"""
        return 'maps.MapProperties'._wrap(super(TiledMapTileSet, self).getProperties())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSet.setName(java.lang.String)"""
        super(_TiledMapTileSet, self).setName(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader_AtlasResolver_DirectAtlasResolver
_DirectAtlasResolver = _AtlasTmxMapLoader_AtlasResolver_DirectAtlasResolver.AtlasResolver.DirectAtlasResolver
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectAtlasResolver():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver.DirectAtlasResolver"""
 
    @staticmethod
    def _wrap(java_value: _DirectAtlasResolver) -> 'DirectAtlasResolver':
        return DirectAtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectAtlasResolver):
        """
        Dynamic initializer for DirectAtlasResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectAtlasResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectAtlasResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getAtlas(self) -> 'g2d.TextureAtlas':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver.getAtlas()"""
        return 'g2d.TextureAtlas'._wrap(super(DirectAtlasResolver, self).getAtlas())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getImage(self, arg0: str) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_DirectAtlasResolver, self).getImage(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureAtlas'):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$DirectAtlasResolver(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        val = _DirectAtlasResolver(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTile
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

from abc import abstractmethod, ABC
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
 
class TiledMapTile():
    """com.badlogic.gdx.maps.tiled.TiledMapTile"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTile) -> 'TiledMapTile':
        return TiledMapTile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTile):
        """
        Dynamic initializer for TiledMapTile.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTile__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTile__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.maps.tiled.TideMapLoader as _TideMapLoader_Parameters
_Parameters = _TideMapLoader_Parameters.Parameters
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Parameters():
    """com.badlogic.gdx.maps.tiled.TideMapLoader.Parameters"""
 
    @staticmethod
    def _wrap(java_value: _Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parameters):
        """
        Dynamic initializer for Parameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parameters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters()"""
        val = _Parameters()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TideMapLoader$Parameters()"""
        val = _Parameters()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader_AtlasTiledMapLoaderParameters
_AtlasTiledMapLoaderParameters = _AtlasTmxMapLoader_AtlasTiledMapLoaderParameters.AtlasTiledMapLoaderParameters
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtlasTiledMapLoaderParameters():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasTiledMapLoaderParameters"""
 
    @staticmethod
    def _wrap(java_value: _AtlasTiledMapLoaderParameters) -> 'AtlasTiledMapLoaderParameters':
        return AtlasTiledMapLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtlasTiledMapLoaderParameters):
        """
        Dynamic initializer for AtlasTiledMapLoaderParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtlasTiledMapLoaderParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtlasTiledMapLoaderParameters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters()"""
        val = _AtlasTiledMapLoaderParameters()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasTiledMapLoaderParameters()"""
        val = _AtlasTiledMapLoaderParameters()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileLayer
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
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.String as _string
import com.badlogic.gdx.maps.MapLayer as _MapLayer
_MapLayer = _MapLayer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as _TiledMapTileLayer_Cell
_Cell = _TiledMapTileLayer_Cell.Cell
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as _TiledMapTileLayer
_TiledMapTileLayer = _TiledMapTileLayer
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapTileLayer():
    """com.badlogic.gdx.maps.tiled.TiledMapTileLayer"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTileLayer) -> 'TiledMapTileLayer':
        return TiledMapTileLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTileLayer):
        """
        Dynamic initializer for TiledMapTileLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTileLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTileLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float._wrap(super(maps.MapLayer, self).getParallaxY())

    @override
    @overload
    def getParent(self) -> 'maps.MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'maps.MapLayer'._wrap(super(maps.MapLayer, self).getParent())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float._wrap(super(maps.MapLayer, self).getOpacity())

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float._wrap(super(maps.MapLayer, self).getRenderOffsetX())

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(_maps.MapLayer, self).setParallaxX(_float.valueOf(arg0))

    @overload
    def setCell(self, arg0: int, arg1: int, arg2: 'Cell'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileLayer.setCell(int,int,com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell)"""
        super(_TiledMapTileLayer, self).setCell(_int.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool._wrap(super(maps.MapLayer, self).isVisible())

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

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getHeight()"""
        return int._wrap(super(TiledMapTileLayer, self).getHeight())

    @override
    @overload
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float._wrap(super(maps.MapLayer, self).getParallaxX())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(_maps.MapLayer, self).setOffsetX(_float.valueOf(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getCell(self, arg0: int, arg1: int) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getCell(int,int)"""
        return 'Cell'._wrap(super(_TiledMapTileLayer, self).getCell(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getTileHeight(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getTileHeight()"""
        return int._wrap(super(TiledMapTileLayer, self).getTileHeight())

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getWidth()"""
        return int._wrap(super(TiledMapTileLayer, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer(int,int,int,int)"""
        val = _TiledMapTileLayer(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float._wrap(super(maps.MapLayer, self).getRenderOffsetY())

    @overload
    def getTileWidth(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer.getTileWidth()"""
        return int._wrap(super(TiledMapTileLayer, self).getTileWidth())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(_maps.MapLayer, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'maps.MapObjects'._wrap(super(maps.MapLayer, self).getObjects())

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float._wrap(super(maps.MapLayer, self).getOffsetY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(_maps.MapLayer, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str._wrap(super(maps.MapLayer, self).getName())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(_maps.MapLayer, self).setName(arg0)

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(_maps.MapLayer, self).setParent(arg0)

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapLayer, self).getProperties())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float._wrap(super(maps.MapLayer, self).getOffsetX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(_maps.MapLayer, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(_maps.MapLayer, self).setParallaxY(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapImageLayer
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

import java.lang.Float as _float
import com.badlogic.gdx.maps.MapObjects as _MapObjects
_MapObjects = _MapObjects
import java.lang.String as _string
import com.badlogic.gdx.maps.MapLayer as _MapLayer
_MapLayer = _MapLayer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.TiledMapImageLayer as _TiledMapImageLayer
_TiledMapImageLayer = _TiledMapImageLayer
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapImageLayer():
    """com.badlogic.gdx.maps.tiled.TiledMapImageLayer"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapImageLayer) -> 'TiledMapImageLayer':
        return TiledMapImageLayer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapImageLayer):
        """
        Dynamic initializer for TiledMapImageLayer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapImageLayer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapImageLayer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setX(float)"""
        super(_TiledMapImageLayer, self).setX(_float.valueOf(arg0))

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TiledMapImageLayer, self).setTextureRegion(arg0)

    @override
    @overload
    def getParallaxY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxY()"""
        return float._wrap(super(maps.MapLayer, self).getParallaxY())

    @override
    @overload
    def getParent(self) -> 'maps.MapLayer':
        """public com.badlogic.gdx.maps.MapLayer com.badlogic.gdx.maps.MapLayer.getParent()"""
        return 'maps.MapLayer'._wrap(super(maps.MapLayer, self).getParent())

    @override
    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOpacity()"""
        return float._wrap(super(maps.MapLayer, self).getOpacity())

    @override
    @overload
    def getRenderOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetX()"""
        return float._wrap(super(maps.MapLayer, self).getRenderOffsetX())

    @override
    @overload
    def setParallaxX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxX(float)"""
        super(_maps.MapLayer, self).setParallaxX(_float.valueOf(arg0))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.maps.MapLayer.isVisible()"""
        return bool._wrap(super(maps.MapLayer, self).isVisible())

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
    def getParallaxX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getParallaxX()"""
        return float._wrap(super(maps.MapLayer, self).getParallaxX())

    @override
    @overload
    def setOffsetX(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetX(float)"""
        super(_maps.MapLayer, self).setOffsetX(_float.valueOf(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.maps.tiled.TiledMapImageLayer.setY(float)"""
        super(_TiledMapImageLayer, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getY()"""
        return float._wrap(super(TiledMapImageLayer, self).getY())

    @override
    @overload
    def getRenderOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getRenderOffsetY()"""
        return float._wrap(super(maps.MapLayer, self).getRenderOffsetY())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getX()"""
        return float._wrap(super(TiledMapImageLayer, self).getX())

    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.TiledMapImageLayer.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(TiledMapImageLayer, self).getTextureRegion())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOpacity(float)"""
        super(_maps.MapLayer, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getObjects(self) -> 'maps.MapObjects':
        """public com.badlogic.gdx.maps.MapObjects com.badlogic.gdx.maps.MapLayer.getObjects()"""
        return 'maps.MapObjects'._wrap(super(maps.MapLayer, self).getObjects())

    @override
    @overload
    def getOffsetY(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetY()"""
        return float._wrap(super(maps.MapLayer, self).getOffsetY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.maps.MapLayer.setVisible(boolean)"""
        super(_maps.MapLayer, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.maps.MapLayer.getName()"""
        return str._wrap(super(maps.MapLayer, self).getName())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.maps.MapLayer.setName(java.lang.String)"""
        super(_maps.MapLayer, self).setName(arg0)

    @override
    @overload
    def setParent(self, arg0: 'MapLayer'):
        """public void com.badlogic.gdx.maps.MapLayer.setParent(com.badlogic.gdx.maps.MapLayer)"""
        super(_maps.MapLayer, self).setParent(arg0)

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.MapLayer.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.MapLayer, self).getProperties())

    @override
    @overload
    def getOffsetX(self) -> float:
        """public float com.badlogic.gdx.maps.MapLayer.getOffsetX()"""
        return float._wrap(super(maps.MapLayer, self).getOffsetX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOffsetY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setOffsetY(float)"""
        super(_maps.MapLayer, self).setOffsetY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public com.badlogic.gdx.maps.tiled.TiledMapImageLayer(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        val = _TiledMapImageLayer(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def setParallaxY(self, arg0: float):
        """public void com.badlogic.gdx.maps.MapLayer.setParallaxY(float)"""
        super(_maps.MapLayer, self).setParallaxY(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileSets
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import com.badlogic.gdx.maps.tiled.TiledMapTileSets as _TiledMapTileSets
_TiledMapTileSets = _TiledMapTileSets
import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.TiledMapTileSet as _TiledMapTileSet
_TiledMapTileSet = _TiledMapTileSet
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMapTileSets():
    """com.badlogic.gdx.maps.tiled.TiledMapTileSets"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapTileSets) -> 'TiledMapTileSets':
        return TiledMapTileSets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapTileSets):
        """
        Dynamic initializer for TiledMapTileSets.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapTileSets__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapTileSets__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets()"""
        val = _TiledMapTileSets()
        self.__wrapper = val

    @overload
    def removeTileSet(self, arg0: 'TiledMapTileSet'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.removeTileSet(com.badlogic.gdx.maps.tiled.TiledMapTileSet)"""
        super(_TiledMapTileSets, self).removeTileSet(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addTileSet(self, arg0: 'TiledMapTileSet'):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.addTileSet(com.badlogic.gdx.maps.tiled.TiledMapTileSet)"""
        super(_TiledMapTileSets, self).addTileSet(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def getTileSet(self, arg0: str) -> 'TiledMapTileSet':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTileSet(java.lang.String)"""
        return 'TiledMapTileSet'._wrap(super(_TiledMapTileSets, self).getTileSet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTileSet(self, arg0: int) -> 'TiledMapTileSet':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSet com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTileSet(int)"""
        return 'TiledMapTileSet'._wrap(super(_TiledMapTileSets, self).getTileSet(_int.valueOf(arg0)))

    @overload
    def getTile(self, arg0: int) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileSets.getTile(int)"""
        return 'TiledMapTile'._wrap(super(_TiledMapTileSets, self).getTile(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets()"""
        val = _TiledMapTileSets()
        self.__wrapper = val

    @overload
    def removeTileSet(self, arg0: int):
        """public void com.badlogic.gdx.maps.tiled.TiledMapTileSets.removeTileSet(int)"""
        super(_TiledMapTileSets, self).removeTileSet(_int.valueOf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.maps.tiled.TiledMapTileSet> com.badlogic.gdx.maps.tiled.TiledMapTileSets.iterator()"""
        return 'Iterator'._wrap(super(TiledMapTileSets, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver
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
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader as _AtlasTmxMapLoader_AtlasResolver_AssetManagerAtlasResolver
_AssetManagerAtlasResolver = _AtlasTmxMapLoader_AtlasResolver_AssetManagerAtlasResolver.AtlasResolver.AssetManagerAtlasResolver
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetManagerAtlasResolver():
    """com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader.AtlasResolver.AssetManagerAtlasResolver"""
 
    @staticmethod
    def _wrap(java_value: _AssetManagerAtlasResolver) -> 'AssetManagerAtlasResolver':
        return AssetManagerAtlasResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetManagerAtlasResolver):
        """
        Dynamic initializer for AssetManagerAtlasResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetManagerAtlasResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetManagerAtlasResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getAtlas(self) -> 'g2d.TextureAtlas':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver.getAtlas()"""
        return 'g2d.TextureAtlas'._wrap(super(AssetManagerAtlasResolver, self).getAtlas())

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
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver.getImage(java.lang.String)"""
        return 'g2d.TextureRegion'._wrap(super(_AssetManagerAtlasResolver, self).getImage(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'AssetManager', arg1: str):
        """public com.badlogic.gdx.maps.tiled.AtlasTmxMapLoader$AtlasResolver$AssetManagerAtlasResolver(com.badlogic.gdx.assets.AssetManager,java.lang.String)"""
        val = _AssetManagerAtlasResolver(arg0, arg1)
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer as _TiledMapTileLayer_Cell
_Cell = _TiledMapTileLayer_Cell.Cell
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.maps.tiled.TiledMapTile as _TiledMapTile
_TiledMapTile = _TiledMapTile
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Cell():
    """com.badlogic.gdx.maps.tiled.TiledMapTileLayer.Cell"""
 
    @staticmethod
    def _wrap(java_value: _Cell) -> 'Cell':
        return Cell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cell):
        """
        Dynamic initializer for Cell.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cell__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cell__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFlipHorizontally(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getFlipHorizontally()"""
        return bool._wrap(super(Cell, self).getFlipHorizontally())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setFlipVertically(self, arg0: bool) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setFlipVertically(boolean)"""
        return 'Cell'._wrap(super(_Cell, self).setFlipVertically(_boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFlipHorizontally(self, arg0: bool) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setFlipHorizontally(boolean)"""
        return 'Cell'._wrap(super(_Cell, self).setFlipHorizontally(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRotation(self, arg0: int) -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setRotation(int)"""
        return 'Cell'._wrap(super(_Cell, self).setRotation(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTile(self, arg0: 'TiledMapTile') -> 'Cell':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.setTile(com.badlogic.gdx.maps.tiled.TiledMapTile)"""
        return 'Cell'._wrap(super(_Cell, self).setTile(arg0))

    @overload
    def getTile(self) -> 'TiledMapTile':
        """public com.badlogic.gdx.maps.tiled.TiledMapTile com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getTile()"""
        return 'TiledMapTile'._wrap(super(Cell, self).getTile())

    @overload
    def getFlipVertically(self) -> bool:
        """public boolean com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getFlipVertically()"""
        return bool._wrap(super(Cell, self).getFlipVertically())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell()"""
        val = _Cell()
        self.__wrapper = val

    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell.getRotation()"""
        return int._wrap(super(Cell, self).getRotation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMapTileLayer$Cell()"""
        val = _Cell()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMap
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.maps.MapLayers as _MapLayers
_MapLayers = _MapLayers
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

import com.badlogic.gdx.maps.tiled.TiledMapTileSets as _TiledMapTileSets
_TiledMapTileSets = _TiledMapTileSets
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
import java.lang.Integer as _int
import com.badlogic.gdx.maps.Map as _Map
_Map = _Map
import com.badlogic.gdx.maps.MapProperties as _MapProperties
_MapProperties = _MapProperties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TiledMap():
    """com.badlogic.gdx.maps.tiled.TiledMap"""
 
    @staticmethod
    def _wrap(java_value: _TiledMap) -> 'TiledMap':
        return TiledMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMap):
        """
        Dynamic initializer for TiledMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLayers(self) -> 'maps.MapLayers':
        """public com.badlogic.gdx.maps.MapLayers com.badlogic.gdx.maps.Map.getLayers()"""
        return 'maps.MapLayers'._wrap(super(maps.Map, self).getLayers())

    @overload
    def setOwnedResources(self, arg0: 'Array'):
        """public void com.badlogic.gdx.maps.tiled.TiledMap.setOwnedResources(com.badlogic.gdx.utils.Array<? extends com.badlogic.gdx.utils.Disposable>)"""
        super(_TiledMap, self).setOwnedResources(arg0)

    @override
    @overload
    def getProperties(self) -> 'maps.MapProperties':
        """public com.badlogic.gdx.maps.MapProperties com.badlogic.gdx.maps.Map.getProperties()"""
        return 'maps.MapProperties'._wrap(super(maps.Map, self).getProperties())

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
    def dispose(self):
        """public void com.badlogic.gdx.maps.tiled.TiledMap.dispose()"""
        super(TiledMap, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TiledMap()"""
        val = _TiledMap()
        self.__wrapper = val

    @overload
    def getTileSets(self) -> 'TiledMapTileSets':
        """public com.badlogic.gdx.maps.tiled.TiledMapTileSets com.badlogic.gdx.maps.tiled.TiledMap.getTileSets()"""
        return 'TiledMapTileSets'._wrap(super(TiledMap, self).getTileSets())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TiledMap()"""
        val = _TiledMap()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TmxMapLoader
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.maps.tiled.TmxMapLoader as _TmxMapLoader
_TmxMapLoader = _TmxMapLoader
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as _BaseTmxMapLoader
_BaseTmxMapLoader = _BaseTmxMapLoader
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import java.lang.String as _string
import com.badlogic.gdx.maps.tiled.TiledMap as _TiledMap
_TiledMap = _TiledMap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
import com.badlogic.gdx.utils.IntMap as _IntMap
_IntMap = _IntMap
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
from typing import List
import java.lang.Integer as _int
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TmxMapLoader():
    """com.badlogic.gdx.maps.tiled.TmxMapLoader"""
 
    @staticmethod
    def _wrap(java_value: _TmxMapLoader) -> 'TmxMapLoader':
        return TmxMapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TmxMapLoader):
        """
        Dynamic initializer for TmxMapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TmxMapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TmxMapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getTileIds(arg0: 'Element', arg1: int, arg2: int) -> List[int]:
        """public static int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(com.badlogic.gdx.utils.XmlReader$Element,int,int)"""
        return List[int]._wrap(_BaseTmxMapLoader.getTileIds(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def load(self, arg0: str, arg1: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.load(java.lang.String,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        return 'TiledMap'._wrap(super(_TmxMapLoader, self).load(arg0, arg1))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _TmxMapLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters') -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        return 'TiledMap'._wrap(super(_TmxMapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'Parameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_BaseTmxMapLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getIdToObject(self) -> 'utils.IntMap':
        """public com.badlogic.gdx.utils.IntMap<com.badlogic.gdx.maps.MapObject> com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getIdToObject()"""
        return 'utils.IntMap'._wrap(super(BaseTmxMapLoader, self).getIdToObject())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader()"""
        val = _TmxMapLoader()
        self.__wrapper = val

    @overload
    def load(self, arg0: str) -> 'TiledMap':
        """public com.badlogic.gdx.maps.tiled.TiledMap com.badlogic.gdx.maps.tiled.TmxMapLoader.load(java.lang.String)"""
        return 'TiledMap'._wrap(super(_TmxMapLoader, self).load(arg0))

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'Parameters'):
        """public void com.badlogic.gdx.maps.tiled.TmxMapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.maps.tiled.TmxMapLoader$Parameters)"""
        super(_TmxMapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.TmxMapLoader()"""
        val = _TmxMapLoader()
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
 
 
# CLASS: com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.maps.tiled.BaseTmxMapLoader as _BaseTmxMapLoader_Parameters
_Parameters = _BaseTmxMapLoader_Parameters.Parameters
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Parameters():
    """com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.Parameters"""
 
    @staticmethod
    def _wrap(java_value: _Parameters) -> 'Parameters':
        return Parameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parameters):
        """
        Dynamic initializer for Parameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parameters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters()"""
        val = _Parameters()
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.maps.tiled.BaseTmxMapLoader$Parameters()"""
        val = _Parameters()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.maps.tiled.TiledMapRenderer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.maps.tiled.TiledMapRenderer as _TiledMapRenderer
_TiledMapRenderer = _TiledMapRenderer
import com.badlogic.gdx.maps.MapRenderer as _MapRenderer
_MapRenderer = _MapRenderer
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import maps
except ImportError:
    maps = _import_once("pygdx.maps")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import int
 
class TiledMapRenderer():
    """com.badlogic.gdx.maps.tiled.TiledMapRenderer"""
 
    @staticmethod
    def _wrap(java_value: _TiledMapRenderer) -> 'TiledMapRenderer':
        return TiledMapRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledMapRenderer):
        """
        Dynamic initializer for TiledMapRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledMapRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledMapRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def setView(self, arg0: 'OrthographicCamera'):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.setView(com.badlogic.gdx.graphics.OrthographicCamera)"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.maps.MapRenderer.render()"""
        pass