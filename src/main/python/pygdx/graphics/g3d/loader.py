from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as __ObjLoader_ObjLoaderParameters
__ObjLoaderParameters = __ObjLoader_ObjLoaderParameters.ObjLoaderParameters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjLoaderParameters(assets.__ModelLoader_ModelParameters, loaders.ModelLoader$ModelParameters):
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader.ObjLoaderParameters"""
 
    @staticmethod
    def __wrap(java_value: __ObjLoaderParameters) -> 'ObjLoaderParameters':
        return ObjLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjLoaderParameters):
        """
        Dynamic initializer for ObjLoaderParameters.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = __ObjLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = __ObjLoaderParameters()
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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters(boolean)"""
        val = __ObjLoaderParameters(__boolean.valueOf(arg0))
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as __ObjLoader_ObjLoaderParameters
__ObjLoaderParameters = __ObjLoader_ObjLoaderParameters.ObjLoaderParameters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjLoaderParameters(assets.__ModelLoader_ModelParameters, loaders.ModelLoader$ModelParameters):
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader.ObjLoaderParameters"""
 
    @staticmethod
    def __wrap(java_value: __ObjLoaderParameters) -> 'ObjLoaderParameters':
        return ObjLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjLoaderParameters):
        """
        Dynamic initializer for ObjLoaderParameters.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = __ObjLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters()"""
        val = __ObjLoaderParameters()
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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters(boolean)"""
        val = __ObjLoaderParameters(__boolean.valueOf(arg0))
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

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.ObjLoader
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
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

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
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
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.model.data.ModelData as __ModelData
__ModelData = __ModelData
import java.lang.Long as __long
import com.badlogic.gdx.assets.loaders.ModelLoader as __ModelLoader
__ModelLoader = __ModelLoader
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
import java.lang.Integer as __int
try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = __import_once__("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.graphics.g3d.loader.ObjLoader as __ObjLoader
__ObjLoader = __ObjLoader
from builtins import int
 
class ObjLoader(assets.__ModelLoader, loaders.ModelLoader):
    """com.badlogic.gdx.graphics.g3d.loader.ObjLoader"""
 
    @staticmethod
    def __wrap(java_value: __ObjLoader) -> 'ObjLoader':
        return ObjLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjLoader):
        """
        Dynamic initializer for ObjLoader.
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
    def loadModel(self, arg0: 'FileHandle') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider', arg2: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadSync(arg0, arg1, arg2, arg3))

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ModelParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ModelLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'.__wrap(super(__loaders.ModelLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: bool) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.graphics.g3d.loader.ObjLoader.loadModel(com.badlogic.gdx.files.FileHandle,boolean)"""
        return 'g3d.Model'.__wrap(super(__ObjLoader, self).loadModel(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadModelData(self, arg0: 'FileHandle', arg1: 'ObjLoaderParameters') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.ObjLoader.loadModelData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.loader.ObjLoader$ObjLoaderParameters)"""
        return 'data.ModelData'.__wrap(super(__ObjLoader, self).loadModelData(arg0, arg1))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader()"""
        val = __ObjLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def loadModelData(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'.__wrap(super(__loaders.ModelLoader, self).loadModelData(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader()"""
        val = __ObjLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.loader.ObjLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __ObjLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters'):
        """public void com.badlogic.gdx.assets.loaders.ModelLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.ModelLoader, self).loadAsync(arg0, arg1, arg2, arg3) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader
from pyquantum_helper import import_once as __import_once__
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

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
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
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader as __G3dModelLoader
__G3dModelLoader = __G3dModelLoader
import com.badlogic.gdx.graphics.g3d.model.data.ModelData as __ModelData
__ModelData = __ModelData
import java.lang.Long as __long
import com.badlogic.gdx.assets.loaders.ModelLoader as __ModelLoader
__ModelLoader = __ModelLoader
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
import java.lang.Integer as __int
try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = __import_once__("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class G3dModelLoader(assets.__ModelLoader, loaders.ModelLoader):
    """com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader"""
 
    @staticmethod
    def __wrap(java_value: __G3dModelLoader) -> 'G3dModelLoader':
        return G3dModelLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __G3dModelLoader):
        """
        Dynamic initializer for G3dModelLoader.
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
    def parseModel(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader.parseModel(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'.__wrap(super(__G3dModelLoader, self).parseModel(arg0))

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
    def __init__(self, arg0: 'BaseJsonReader', arg1: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader(com.badlogic.gdx.utils.BaseJsonReader,com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __G3dModelLoader(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadModel(self, arg0: 'FileHandle') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider', arg2: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadSync(arg0, arg1, arg2, arg3))

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ModelParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.assets.loaders.ModelLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        return 'utils.Array'.__wrap(super(__loaders.ModelLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadModelData(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.loaders.ModelLoader$ModelParameters)"""
        return 'data.ModelData'.__wrap(super(__G3dModelLoader, self).loadModelData(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, arg0: 'BaseJsonReader'):
        """public com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader(com.badlogic.gdx.utils.BaseJsonReader)"""
        val = __G3dModelLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadModel(self, arg0: 'FileHandle', arg1: 'ModelParameters') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,P)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def loadModelData(self, arg0: 'FileHandle') -> 'data.ModelData':
        """public com.badlogic.gdx.graphics.g3d.model.data.ModelData com.badlogic.gdx.assets.loaders.ModelLoader.loadModelData(com.badlogic.gdx.files.FileHandle)"""
        return 'data.ModelData'.__wrap(super(__loaders.ModelLoader, self).loadModelData(arg0))

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
    def loadModel(self, arg0: 'FileHandle', arg1: 'TextureProvider') -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model com.badlogic.gdx.assets.loaders.ModelLoader.loadModel(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return 'g3d.Model'.__wrap(super(__loaders.ModelLoader, self).loadModel(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ModelParameters'):
        """public void com.badlogic.gdx.assets.loaders.ModelLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.ModelLoader, self).loadAsync(arg0, arg1, arg2, arg3)