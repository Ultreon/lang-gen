from __future__ import annotations
from overload import overload


 
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.audio.Sound as _Sound
_Sound = _Sound
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.assets.loaders.SoundLoader as _SoundLoader
_SoundLoader = _SoundLoader
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundLoader():
    """com.badlogic.gdx.assets.loaders.SoundLoader"""
 
    @staticmethod
    def _wrap(java_value: _SoundLoader) -> 'SoundLoader':
        return SoundLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundLoader):
        """
        Dynamic initializer for SoundLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'SoundParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.SoundLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        return 'utils.Array'._wrap(super(_SoundLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SoundParameter') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.assets.loaders.SoundLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        return 'audio.Sound'._wrap(super(_SoundLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.SoundLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _SoundLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SoundParameter'):
        """public void com.badlogic.gdx.assets.loaders.SoundLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        super(_SoundLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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

 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SoundLoader
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.audio.Sound as _Sound
_Sound = _Sound
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.assets.loaders.SoundLoader as _SoundLoader
_SoundLoader = _SoundLoader
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundLoader():
    """com.badlogic.gdx.assets.loaders.SoundLoader"""
 
    @staticmethod
    def _wrap(java_value: _SoundLoader) -> 'SoundLoader':
        return SoundLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundLoader):
        """
        Dynamic initializer for SoundLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'SoundParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.SoundLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        return 'utils.Array'._wrap(super(_SoundLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SoundParameter') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.assets.loaders.SoundLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        return 'audio.Sound'._wrap(super(_SoundLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.SoundLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _SoundLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SoundParameter'):
        """public void com.badlogic.gdx.assets.loaders.SoundLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter)"""
        super(_SoundLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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

 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SoundLoader 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ModelLoader
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.assets.loaders.ModelLoader as _ModelLoader
_ModelLoader = _ModelLoader
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
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
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
import com.badlogic.gdx.graphics.g3d.model.data.ModelData as _ModelData
_ModelData = _ModelData
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = _import_once("pygdx.graphics.g3d.model.data")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelLoader():
    """com.badlogic.gdx.assets.loaders.ModelLoader"""
 
    @staticmethod
    def _wrap(java_value: _ModelLoader) -> 'ModelLoader':
        return ModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelLoader):
        """
        Dynamic initializer for ModelLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider', arg2: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider,P)"""
        return 'g3d.Model'._wrap(super(_ModelLoader, self).loadModel(arg0, arg1, arg2))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ModelParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ModelLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_ModelLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_ModelLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return 'g3d.Model'._wrap(super(_ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def loadModelData(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'._wrap(super(_ModelLoader, self).loadModelData(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.ModelLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _ModelLoader(arg0)
        self.__wrapper = val

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters'):
        """public void com.badlogic.gdx.assets.loaders.ModelLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_ModelLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadModel(self, arg0: 'FileHandle') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle)"""
        return 'g3d.Model'._wrap(super(_ModelLoader, self).loadModel(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_ModelLoader, self).loadModel(arg0, arg1))

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

    @abstractmethod
    def loadModelData(self, arg0: 'FileHandle', arg1: 'ModelParameters'):
        """public abstract com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle,P)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter
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
import com.badlogic.gdx.assets.loaders.TextureLoader as _TextureLoader_TextureParameter
_TextureParameter = _TextureLoader_TextureParameter.TextureParameter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureParameter():
    """com.badlogic.gdx.assets.loaders.TextureLoader.TextureParameter"""
 
    @staticmethod
    def _wrap(java_value: _TextureParameter) -> 'TextureParameter':
        return TextureParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureParameter):
        """
        Dynamic initializer for TextureParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureParameter__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter()"""
        val = _TextureParameter()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter()"""
        val = _TextureParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SkinLoader
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.ui.Skin as _Skin
_Skin = _Skin
try:
    from pygdx.scenes.scene2d import ui
except ImportError:
    ui = _import_once("pygdx.scenes.scene2d.ui")

import com.badlogic.gdx.assets.loaders.SkinLoader as _SkinLoader
_SkinLoader = _SkinLoader
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkinLoader():
    """com.badlogic.gdx.assets.loaders.SkinLoader"""
 
    @staticmethod
    def _wrap(java_value: _SkinLoader) -> 'SkinLoader':
        return SkinLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkinLoader):
        """
        Dynamic initializer for SkinLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkinLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkinLoader__wrapper":
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SkinParameter'):
        """public void com.badlogic.gdx.assets.loaders.SkinLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter)"""
        super(_SkinLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.SkinLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _SkinLoader(arg0)
        self.__wrapper = val

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'SkinParameter') -> 'ui.Skin':
        """public com.badlogic.gdx.scenes.scene2d.ui.Skin com.badlogic.gdx.assets.loaders.SkinLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter)"""
        return 'ui.Skin'._wrap(super(_SkinLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'SkinParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.SkinLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter)"""
        return 'utils.Array'._wrap(super(_SkinLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.TextureAtlasLoader as _TextureAtlasLoader_TextureAtlasParameter
_TextureAtlasParameter = _TextureAtlasLoader_TextureAtlasParameter.TextureAtlasParameter
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAtlasParameter():
    """com.badlogic.gdx.assets.loaders.TextureAtlasLoader.TextureAtlasParameter"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasParameter) -> 'TextureAtlasParameter':
        return TextureAtlasParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasParameter):
        """
        Dynamic initializer for TextureAtlasParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasParameter__wrapper":
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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter(boolean)"""
        val = _TextureAtlasParameter(_boolean.valueOf(arg0))
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
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter()"""
        val = _TextureAtlasParameter()
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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter()"""
        val = _TextureAtlasParameter()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter
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
import com.badlogic.gdx.assets.loaders.CubemapLoader as _CubemapLoader_CubemapParameter
_CubemapParameter = _CubemapLoader_CubemapParameter.CubemapParameter
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubemapParameter():
    """com.badlogic.gdx.assets.loaders.CubemapLoader.CubemapParameter"""
 
    @staticmethod
    def _wrap(java_value: _CubemapParameter) -> 'CubemapParameter':
        return CubemapParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapParameter):
        """
        Dynamic initializer for CubemapParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapParameter__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter()"""
        val = _CubemapParameter()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter()"""
        val = _CubemapParameter()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
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

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
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
 
class AsynchronousAssetLoader():
    """com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader"""
 
    @staticmethod
    def _wrap(java_value: _AsynchronousAssetLoader) -> 'AsynchronousAssetLoader':
        return AsynchronousAssetLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsynchronousAssetLoader):
        """
        Dynamic initializer for AsynchronousAssetLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsynchronousAssetLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsynchronousAssetLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @abstractmethod
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'AssetLoaderParameters'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.AssetLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _AsynchronousAssetLoader(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.BitmapFontLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.assets.loaders.BitmapFontLoader as _BitmapFontLoader
_BitmapFontLoader = _BitmapFontLoader
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import com.badlogic.gdx.graphics.g2d.BitmapFont as _BitmapFont
_BitmapFont = _BitmapFont
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
 
class BitmapFontLoader():
    """com.badlogic.gdx.assets.loaders.BitmapFontLoader"""
 
    @staticmethod
    def _wrap(java_value: _BitmapFontLoader) -> 'BitmapFontLoader':
        return BitmapFontLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitmapFontLoader):
        """
        Dynamic initializer for BitmapFontLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitmapFontLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitmapFontLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.BitmapFontLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _BitmapFontLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BitmapFontParameter'):
        """public void com.badlogic.gdx.assets.loaders.BitmapFontLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter)"""
        super(_BitmapFontLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BitmapFontParameter') -> 'g2d.BitmapFont':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont com.badlogic.gdx.assets.loaders.BitmapFontLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter)"""
        return 'g2d.BitmapFont'._wrap(super(_BitmapFontLoader, self).loadSync(arg0, arg1, arg2, arg3))

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'BitmapFontParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.BitmapFontLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter)"""
        return 'utils.Array'._wrap(super(_BitmapFontLoader, self).getDependencies(arg0, arg1, arg2))

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapLoaderInfo
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
import com.badlogic.gdx.assets.loaders.CubemapLoader as _CubemapLoader_CubemapLoaderInfo
_CubemapLoaderInfo = _CubemapLoader_CubemapLoaderInfo.CubemapLoaderInfo
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubemapLoaderInfo():
    """com.badlogic.gdx.assets.loaders.CubemapLoader.CubemapLoaderInfo"""
 
    @staticmethod
    def _wrap(java_value: _CubemapLoaderInfo) -> 'CubemapLoaderInfo':
        return CubemapLoaderInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapLoaderInfo):
        """
        Dynamic initializer for CubemapLoaderInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapLoaderInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapLoaderInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapLoaderInfo()"""
        val = _CubemapLoaderInfo()
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
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapLoaderInfo()"""
        val = _CubemapLoaderInfo()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.assets.loaders.BitmapFontLoader as _BitmapFontLoader_BitmapFontParameter
_BitmapFontParameter = _BitmapFontLoader_BitmapFontParameter.BitmapFontParameter
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitmapFontParameter():
    """com.badlogic.gdx.assets.loaders.BitmapFontLoader.BitmapFontParameter"""
 
    @staticmethod
    def _wrap(java_value: _BitmapFontParameter) -> 'BitmapFontParameter':
        return BitmapFontParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitmapFontParameter):
        """
        Dynamic initializer for BitmapFontParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitmapFontParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitmapFontParameter__wrapper":
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter()"""
        val = _BitmapFontParameter()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.BitmapFontLoader$BitmapFontParameter()"""
        val = _BitmapFontParameter()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.MusicLoader
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.audio.Music as _Music
_Music = _Music
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import com.badlogic.gdx.assets.loaders.MusicLoader as _MusicLoader
_MusicLoader = _MusicLoader
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MusicLoader():
    """com.badlogic.gdx.assets.loaders.MusicLoader"""
 
    @staticmethod
    def _wrap(java_value: _MusicLoader) -> 'MusicLoader':
        return MusicLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MusicLoader):
        """
        Dynamic initializer for MusicLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MusicLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MusicLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'MusicParameter') -> 'audio.Music':
        """public com.badlogic.gdx.audio.Music com.badlogic.gdx.assets.loaders.MusicLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter)"""
        return 'audio.Music'._wrap(super(_MusicLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.MusicLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _MusicLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'MusicParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.MusicLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter)"""
        return 'utils.Array'._wrap(super(_MusicLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'MusicParameter'):
        """public void com.badlogic.gdx.assets.loaders.MusicLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter)"""
        super(_MusicLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.AssetLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
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
 
class AssetLoader():
    """com.badlogic.gdx.assets.loaders.AssetLoader"""
 
    @staticmethod
    def _wrap(java_value: _AssetLoader) -> 'AssetLoader':
        return AssetLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetLoader):
        """
        Dynamic initializer for AssetLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetLoader__wrapper":
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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.AssetLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _AssetLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'AssetLoaderParameters'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.AssetLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter
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
import com.badlogic.gdx.assets.loaders.MusicLoader as _MusicLoader_MusicParameter
_MusicParameter = _MusicLoader_MusicParameter.MusicParameter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MusicParameter():
    """com.badlogic.gdx.assets.loaders.MusicLoader.MusicParameter"""
 
    @staticmethod
    def _wrap(java_value: _MusicParameter) -> 'MusicParameter':
        return MusicParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MusicParameter):
        """
        Dynamic initializer for MusicParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MusicParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MusicParameter__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter()"""
        val = _MusicParameter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.MusicLoader$MusicParameter()"""
        val = _MusicParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ParticleEffectLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

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

import com.badlogic.gdx.graphics.g2d.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import com.badlogic.gdx.assets.loaders.ParticleEffectLoader as _ParticleEffectLoader
_ParticleEffectLoader = _ParticleEffectLoader
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
 
class ParticleEffectLoader():
    """com.badlogic.gdx.assets.loaders.ParticleEffectLoader"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectLoader) -> 'ParticleEffectLoader':
        return ParticleEffectLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectLoader):
        """
        Dynamic initializer for ParticleEffectLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ParticleEffectParameter') -> 'g2d.ParticleEffect':
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect com.badlogic.gdx.assets.loaders.ParticleEffectLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ParticleEffectLoader$ParticleEffectParameter)"""
        return 'g2d.ParticleEffect'._wrap(super(_ParticleEffectLoader, self).load(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.ParticleEffectLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _ParticleEffectLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

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

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ParticleEffectParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ParticleEffectLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ParticleEffectLoader$ParticleEffectParameter)"""
        return 'utils.Array'._wrap(super(_ParticleEffectLoader, self).getDependencies(arg0, arg1, arg2))

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter
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
import com.badlogic.gdx.assets.loaders.SkinLoader as _SkinLoader_SkinParameter
_SkinParameter = _SkinLoader_SkinParameter.SkinParameter
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SkinParameter():
    """com.badlogic.gdx.assets.loaders.SkinLoader.SkinParameter"""
 
    @staticmethod
    def _wrap(java_value: _SkinParameter) -> 'SkinParameter':
        return SkinParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkinParameter):
        """
        Dynamic initializer for SkinParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkinParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkinParameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter(java.lang.String)"""
        val = _SkinParameter(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter()"""
        val = _SkinParameter()
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
    def __init__(self, arg0: str, arg1: 'ObjectMap'):
        """public com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter(java.lang.String,com.badlogic.gdx.utils.ObjectMap<java.lang.String, java.lang.Object>)"""
        val = _SkinParameter(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter()"""
        val = _SkinParameter()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ObjectMap'):
        """public com.badlogic.gdx.assets.loaders.SkinLoader$SkinParameter(com.badlogic.gdx.utils.ObjectMap<java.lang.String, java.lang.Object>)"""
        val = _SkinParameter(arg0)
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.TextureAtlasLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

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

import com.badlogic.gdx.assets.loaders.TextureAtlasLoader as _TextureAtlasLoader
_TextureAtlasLoader = _TextureAtlasLoader
import com.badlogic.gdx.graphics.g2d.TextureAtlas as _TextureAtlas
_TextureAtlas = _TextureAtlas
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
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
 
class TextureAtlasLoader():
    """com.badlogic.gdx.assets.loaders.TextureAtlasLoader"""
 
    @staticmethod
    def _wrap(java_value: _TextureAtlasLoader) -> 'TextureAtlasLoader':
        return TextureAtlasLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAtlasLoader):
        """
        Dynamic initializer for TextureAtlasLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAtlasLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAtlasLoader__wrapper":
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
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'TextureAtlasParameter') -> 'g2d.TextureAtlas':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.assets.loaders.TextureAtlasLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter)"""
        return 'g2d.TextureAtlas'._wrap(super(_TextureAtlasLoader, self).load(arg0, arg1, arg2, arg3))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.TextureAtlasLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _TextureAtlasLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'TextureAtlasParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.TextureAtlasLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.TextureAtlasLoader$TextureAtlasParameter)"""
        return 'utils.Array'._wrap(super(_TextureAtlasLoader, self).getDependencies(arg0, arg1, arg2))

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SynchronousAssetLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import com.badlogic.gdx.assets.loaders.SynchronousAssetLoader as _SynchronousAssetLoader
_SynchronousAssetLoader = _SynchronousAssetLoader
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
 
class SynchronousAssetLoader():
    """com.badlogic.gdx.assets.loaders.SynchronousAssetLoader"""
 
    @staticmethod
    def _wrap(java_value: _SynchronousAssetLoader) -> 'SynchronousAssetLoader':
        return SynchronousAssetLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SynchronousAssetLoader):
        """
        Dynamic initializer for SynchronousAssetLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SynchronousAssetLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SynchronousAssetLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'AssetLoaderParameters'):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.AssetLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

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

    @abstractmethod
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public abstract T com.badlogic.gdx.assets.loaders.SynchronousAssetLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.SynchronousAssetLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _SynchronousAssetLoader(arg0)
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.SoundLoader as _SoundLoader_SoundParameter
_SoundParameter = _SoundLoader_SoundParameter.SoundParameter
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoundParameter():
    """com.badlogic.gdx.assets.loaders.SoundLoader.SoundParameter"""
 
    @staticmethod
    def _wrap(java_value: _SoundParameter) -> 'SoundParameter':
        return SoundParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoundParameter):
        """
        Dynamic initializer for SoundParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoundParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoundParameter__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter()"""
        val = _SoundParameter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.SoundLoader$SoundParameter()"""
        val = _SoundParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.I18NBundleLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.assets.loaders.I18NBundleLoader as _I18NBundleLoader
_I18NBundleLoader = _I18NBundleLoader
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.I18NBundle as _I18NBundle
_I18NBundle = _I18NBundle
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
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
 
class I18NBundleLoader():
    """com.badlogic.gdx.assets.loaders.I18NBundleLoader"""
 
    @staticmethod
    def _wrap(java_value: _I18NBundleLoader) -> 'I18NBundleLoader':
        return I18NBundleLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _I18NBundleLoader):
        """
        Dynamic initializer for I18NBundleLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_I18NBundleLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_I18NBundleLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.I18NBundleLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _I18NBundleLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'I18NBundleParameter'):
        """public void com.badlogic.gdx.assets.loaders.I18NBundleLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter)"""
        super(_I18NBundleLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'I18NBundleParameter') -> 'utils.I18NBundle':
        """public com.badlogic.gdx.utils.I18NBundle com.badlogic.gdx.assets.loaders.I18NBundleLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter)"""
        return 'utils.I18NBundle'._wrap(super(_I18NBundleLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'I18NBundleParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.I18NBundleLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter)"""
        return 'utils.Array'._wrap(super(_I18NBundleLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter
from builtins import str
import com.badlogic.gdx.assets.loaders.ShaderProgramLoader as _ShaderProgramLoader_ShaderProgramParameter
_ShaderProgramParameter = _ShaderProgramLoader_ShaderProgramParameter.ShaderProgramParameter
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
 
class ShaderProgramParameter():
    """com.badlogic.gdx.assets.loaders.ShaderProgramLoader.ShaderProgramParameter"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProgramParameter) -> 'ShaderProgramParameter':
        return ShaderProgramParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProgramParameter):
        """
        Dynamic initializer for ShaderProgramParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProgramParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProgramParameter__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter()"""
        val = _ShaderProgramParameter()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter()"""
        val = _ShaderProgramParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.assets.loaders.PixmapLoader as _PixmapLoader_PixmapParameter
_PixmapParameter = _PixmapLoader_PixmapParameter.PixmapParameter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapParameter():
    """com.badlogic.gdx.assets.loaders.PixmapLoader.PixmapParameter"""
 
    @staticmethod
    def _wrap(java_value: _PixmapParameter) -> 'PixmapParameter':
        return PixmapParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapParameter):
        """
        Dynamic initializer for PixmapParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapParameter__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter()"""
        val = _PixmapParameter()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter()"""
        val = _PixmapParameter()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.PixmapLoader
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
import com.badlogic.gdx.assets.loaders.PixmapLoader as _PixmapLoader
_PixmapLoader = _PixmapLoader
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import com.badlogic.gdx.graphics.Pixmap as _Pixmap
_Pixmap = _Pixmap
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PixmapLoader():
    """com.badlogic.gdx.assets.loaders.PixmapLoader"""
 
    @staticmethod
    def _wrap(java_value: _PixmapLoader) -> 'PixmapLoader':
        return PixmapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PixmapLoader):
        """
        Dynamic initializer for PixmapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PixmapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PixmapLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'PixmapParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.PixmapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter)"""
        return 'utils.Array'._wrap(super(_PixmapLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'PixmapParameter') -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.assets.loaders.PixmapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter)"""
        return 'graphics.Pixmap'._wrap(super(_PixmapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.PixmapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _PixmapLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'PixmapParameter'):
        """public void com.badlogic.gdx.assets.loaders.PixmapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.PixmapLoader$PixmapParameter)"""
        super(_PixmapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ShaderProgramLoader
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.assets.loaders.ShaderProgramLoader as _ShaderProgramLoader
_ShaderProgramLoader = _ShaderProgramLoader
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
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShaderProgramLoader():
    """com.badlogic.gdx.assets.loaders.ShaderProgramLoader"""
 
    @staticmethod
    def _wrap(java_value: _ShaderProgramLoader) -> 'ShaderProgramLoader':
        return ShaderProgramLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShaderProgramLoader):
        """
        Dynamic initializer for ShaderProgramLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShaderProgramLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShaderProgramLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ShaderProgramParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ShaderProgramLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter)"""
        return 'utils.Array'._wrap(super(_ShaderProgramLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ShaderProgramParameter') -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.assets.loaders.ShaderProgramLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter)"""
        return 'glutils.ShaderProgram'._wrap(super(_ShaderProgramLoader, self).loadSync(arg0, arg1, arg2, arg3))

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ShaderProgramParameter'):
        """public void com.badlogic.gdx.assets.loaders.ShaderProgramLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ShaderProgramLoader$ShaderProgramParameter)"""
        super(_ShaderProgramLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.ShaderProgramLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _ShaderProgramLoader(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver', arg1: str, arg2: str):
        """public com.badlogic.gdx.assets.loaders.ShaderProgramLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver,java.lang.String,java.lang.String)"""
        val = _ShaderProgramLoader(arg0, arg1, arg2)
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.FileHandleResolver
import com.badlogic.gdx.assets.loaders.FileHandleResolver as _FileHandleResolver
_FileHandleResolver = _FileHandleResolver
from abc import abstractmethod, ABC
 
class FileHandleResolver():
    """com.badlogic.gdx.assets.loaders.FileHandleResolver"""
 
    @staticmethod
    def _wrap(java_value: _FileHandleResolver) -> 'FileHandleResolver':
        return FileHandleResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileHandleResolver):
        """
        Dynamic initializer for FileHandleResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileHandleResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileHandleResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def resolve(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.FileHandleResolver.resolve(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.CubemapLoader
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.assets.loaders.CubemapLoader as _CubemapLoader
_CubemapLoader = _CubemapLoader
import com.badlogic.gdx.graphics.Cubemap as _Cubemap
_Cubemap = _Cubemap
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubemapLoader():
    """com.badlogic.gdx.assets.loaders.CubemapLoader"""
 
    @staticmethod
    def _wrap(java_value: _CubemapLoader) -> 'CubemapLoader':
        return CubemapLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapLoader):
        """
        Dynamic initializer for CubemapLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapLoader__wrapper":
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'CubemapParameter'):
        """public void com.badlogic.gdx.assets.loaders.CubemapLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter)"""
        super(_CubemapLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'CubemapParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.CubemapLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter)"""
        return 'utils.Array'._wrap(super(_CubemapLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'CubemapParameter') -> 'graphics.Cubemap':
        """public com.badlogic.gdx.graphics.Cubemap com.badlogic.gdx.assets.loaders.CubemapLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.CubemapLoader$CubemapParameter)"""
        return 'graphics.Cubemap'._wrap(super(_CubemapLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.CubemapLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _CubemapLoader(arg0)
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters
import com.badlogic.gdx.assets.loaders.ModelLoader as _ModelLoader_ModelParameters
_ModelParameters = _ModelLoader_ModelParameters.ModelParameters
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelParameters():
    """com.badlogic.gdx.assets.loaders.ModelLoader.ModelParameters"""
 
    @staticmethod
    def _wrap(java_value: _ModelParameters) -> 'ModelParameters':
        return ModelParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelParameters):
        """
        Dynamic initializer for ModelParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelParameters__wrapper":
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters()"""
        val = _ModelParameters()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters()"""
        val = _ModelParameters()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.assets.loaders.TextureLoader$TextureLoaderInfo
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.TextureLoader as _TextureLoader_TextureLoaderInfo
_TextureLoaderInfo = _TextureLoader_TextureLoaderInfo.TextureLoaderInfo
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureLoaderInfo():
    """com.badlogic.gdx.assets.loaders.TextureLoader.TextureLoaderInfo"""
 
    @staticmethod
    def _wrap(java_value: _TextureLoaderInfo) -> 'TextureLoaderInfo':
        return TextureLoaderInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureLoaderInfo):
        """
        Dynamic initializer for TextureLoaderInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureLoaderInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureLoaderInfo__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.TextureLoader$TextureLoaderInfo()"""
        val = _TextureLoaderInfo()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.TextureLoader$TextureLoaderInfo()"""
        val = _TextureLoaderInfo()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.ParticleEffectLoader$ParticleEffectParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.ParticleEffectLoader as _ParticleEffectLoader_ParticleEffectParameter
_ParticleEffectParameter = _ParticleEffectLoader_ParticleEffectParameter.ParticleEffectParameter
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffectParameter():
    """com.badlogic.gdx.assets.loaders.ParticleEffectLoader.ParticleEffectParameter"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectParameter) -> 'ParticleEffectParameter':
        return ParticleEffectParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectParameter):
        """
        Dynamic initializer for ParticleEffectParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectParameter__wrapper":
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
        """public com.badlogic.gdx.assets.loaders.ParticleEffectLoader$ParticleEffectParameter()"""
        val = _ParticleEffectParameter()
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
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.ParticleEffectLoader$ParticleEffectParameter()"""
        val = _ParticleEffectParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.I18NBundleLoader as _I18NBundleLoader_I18NBundleParameter
_I18NBundleParameter = _I18NBundleLoader_I18NBundleParameter.I18NBundleParameter
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class I18NBundleParameter():
    """com.badlogic.gdx.assets.loaders.I18NBundleLoader.I18NBundleParameter"""
 
    @staticmethod
    def _wrap(java_value: _I18NBundleParameter) -> 'I18NBundleParameter':
        return I18NBundleParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _I18NBundleParameter):
        """
        Dynamic initializer for I18NBundleParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_I18NBundleParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_I18NBundleParameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Locale'):
        """public com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter(java.util.Locale)"""
        val = _I18NBundleParameter(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Locale', arg1: str):
        """public com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter(java.util.Locale,java.lang.String)"""
        val = _I18NBundleParameter(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter()"""
        val = _I18NBundleParameter()
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.loaders.I18NBundleLoader$I18NBundleParameter()"""
        val = _I18NBundleParameter()
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
 
 
# CLASS: com.badlogic.gdx.assets.loaders.TextureLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.loaders.TextureLoader as _TextureLoader
_TextureLoader = _TextureLoader
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureLoader():
    """com.badlogic.gdx.assets.loaders.TextureLoader"""
 
    @staticmethod
    def _wrap(java_value: _TextureLoader) -> 'TextureLoader':
        return TextureLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureLoader):
        """
        Dynamic initializer for TextureLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureLoader__wrapper":
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_AssetLoader, self).resolve(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'TextureParameter'):
        """public void com.badlogic.gdx.assets.loaders.TextureLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter)"""
        super(_TextureLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.loaders.TextureLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _TextureLoader(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'TextureParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.TextureLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter)"""
        return 'utils.Array'._wrap(super(_TextureLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'TextureParameter') -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.assets.loaders.TextureLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.TextureLoader$TextureParameter)"""
        return 'graphics.Texture'._wrap(super(_TextureLoader, self).loadSync(arg0, arg1, arg2, arg3))

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