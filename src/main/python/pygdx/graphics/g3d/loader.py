from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as _ObjLoader_ObjLoaderParameters
_ObjLoaderParameters = _ObjLoader_ObjLoaderParameters.ObjLoaderParameters
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjLoaderParameters():
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader.ObjLoaderParameters"""
 
    @staticmethod
    def _wrap(java_value: _ObjLoaderParameters) -> 'ObjLoaderParameters':
        return ObjLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjLoaderParameters):
        """
        Dynamic initializer for ObjLoaderParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjLoaderParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjLoaderParameters__wrapper":
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
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = _ObjLoaderParameters()
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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters(boolean)"""
        val = _ObjLoaderParameters(_boolean.valueOf(arg0))
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = _ObjLoaderParameters()
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as _ObjLoader_ObjLoaderParameters
_ObjLoaderParameters = _ObjLoader_ObjLoaderParameters.ObjLoaderParameters
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjLoaderParameters():
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader.ObjLoaderParameters"""
 
    @staticmethod
    def _wrap(java_value: _ObjLoaderParameters) -> 'ObjLoaderParameters':
        return ObjLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjLoaderParameters):
        """
        Dynamic initializer for ObjLoaderParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjLoaderParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjLoaderParameters__wrapper":
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
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = _ObjLoaderParameters()
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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters(boolean)"""
        val = _ObjLoaderParameters(_boolean.valueOf(arg0))
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = _ObjLoaderParameters()
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader
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

import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as _ObjLoader
_ObjLoader = _ObjLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.String as _string
import java.lang.Boolean as _boolean
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
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = _import_once("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjLoader():
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader"""
 
    @staticmethod
    def _wrap(java_value: _ObjLoader) -> 'ObjLoader':
        return ObjLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjLoader):
        """
        Dynamic initializer for ObjLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def loadModelData(self, arg0: 'FileHandle', arg1: 'ObjLoaderParameters') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.ObjLoader.loadModelData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters)"""
        return 'data.ModelData'._wrap(super(_ObjLoader, self).loadModelData(arg0, arg1))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ModelParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ModelLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_loaders.ModelLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters'):
        """public void com.badlogic.gdx.assets.loaders.ModelLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.ModelLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadModelData(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'._wrap(super(_loaders.ModelLoader, self).loadModelData(arg0))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: bool) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.loader.ObjLoader.loadModel(com.badlogic.gdx.files.FileHandle,boolean)"""
        return 'g3d.Model'._wrap(super(_ObjLoader, self).loadModel(arg0, _boolean.valueOf(arg1)))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider', arg2: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadSync(arg0, arg1, arg2, arg3))

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

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1))

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
    def loadModel(self, arg0: 'FileHandle') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader()"""
        val = _ObjLoader()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader()"""
        val = _ObjLoader()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _ObjLoader(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader
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

try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

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
import com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader as _G3dModelLoader
_G3dModelLoader = _G3dModelLoader
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = _import_once("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class G3dModelLoader():
    """com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader"""
 
    @staticmethod
    def _wrap(java_value: _G3dModelLoader) -> 'G3dModelLoader':
        return G3dModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _G3dModelLoader):
        """
        Dynamic initializer for G3dModelLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_G3dModelLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_G3dModelLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'BaseJsonReader', arg1: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader(com.badlogic.gdx.utils.BaseJsonReader,com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _G3dModelLoader(arg0, arg1)
        self.__wrapper = val

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ModelParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ModelLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'._wrap(super(_loaders.ModelLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters'):
        """public void com.badlogic.gdx.assets.loaders.ModelLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.ModelLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadModelData(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'._wrap(super(_loaders.ModelLoader, self).loadModelData(arg0))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider', arg2: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1, arg2))

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadSync(arg0, arg1, arg2, arg3))

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

    @overload
    def loadModelData(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters)"""
        return 'data.ModelData'._wrap(super(_G3dModelLoader, self).loadModelData(arg0, arg1))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0, arg1))

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
    def loadModel(self, arg0: 'FileHandle') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle)"""
        return 'g3d.Model'._wrap(super(_loaders.ModelLoader, self).loadModel(arg0))

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
    def parseModel(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader.parseModel(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'._wrap(super(_G3dModelLoader, self).parseModel(arg0))

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
    def __init__(self, arg0: 'BaseJsonReader'):
        """public com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader(com.badlogic.gdx.utils.BaseJsonReader)"""
        val = _G3dModelLoader(arg0)
        self.__wrapper = val