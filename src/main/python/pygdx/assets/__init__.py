from __future__ import annotations
from overload import overload


 
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.badlogic.gdx.assets.AssetErrorListener as _AssetErrorListener
_AssetErrorListener = _AssetErrorListener
 
class AssetErrorListener():
    """com.badlogic.gdx.assets.AssetErrorListener"""
 
    @staticmethod
    def _wrap(java_value: _AssetErrorListener) -> 'AssetErrorListener':
        return AssetErrorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetErrorListener):
        """
        Dynamic initializer for AssetErrorListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetErrorListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetErrorListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, arg0: 'AssetDescriptor', arg1: 'Throwable'):
        """public abstract void com.badlogic.gdx.assets.AssetErrorListener.error(com.badlogic.gdx.assets.AssetDescriptor,java.lang.Throwable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.assets.AssetErrorListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.badlogic.gdx.assets.AssetErrorListener as _AssetErrorListener
_AssetErrorListener = _AssetErrorListener
 
class AssetErrorListener():
    """com.badlogic.gdx.assets.AssetErrorListener"""
 
    @staticmethod
    def _wrap(java_value: _AssetErrorListener) -> 'AssetErrorListener':
        return AssetErrorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetErrorListener):
        """
        Dynamic initializer for AssetErrorListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetErrorListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetErrorListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, arg0: 'AssetDescriptor', arg1: 'Throwable'):
        """public abstract void com.badlogic.gdx.assets.AssetErrorListener.error(com.badlogic.gdx.assets.AssetDescriptor,java.lang.Throwable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.assets.AssetErrorListener 
 
 
# CLASS: com.badlogic.gdx.assets.AssetManager
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.assets.loaders.FileHandleResolver as _FileHandleResolver
_FileHandleResolver = _FileHandleResolver
import java.lang.Integer as _int
import com.badlogic.gdx.utils.Logger as _Logger
_Logger = _Logger
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.assets.AssetManager as _AssetManager
_AssetManager = _AssetManager
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetManager():
    """com.badlogic.gdx.assets.AssetManager"""
 
    @staticmethod
    def _wrap(java_value: _AssetManager) -> 'AssetManager':
        return AssetManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetManager):
        """
        Dynamic initializer for AssetManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def contains(self, arg0: str) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.contains(java.lang.String)"""
        return bool._wrap(super(_AssetManager, self).contains(arg0))

    @overload
    def isLoaded(self, arg0: str) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(java.lang.String)"""
        return bool._wrap(super(_AssetManager, self).isLoaded(arg0))

    @overload
    def getLoader(self, arg0: 'Class') -> 'loaders.AssetLoader':
        """public <T> com.badlogic.gdx.assets.loaders.AssetLoader com.badlogic.gdx.assets.AssetManager.getLoader(java.lang.Class<T>)"""
        return 'loaders.AssetLoader'._wrap(super(_AssetManager, self).getLoader(arg0))

    @overload
    def get(self, arg0: str, arg1: 'Class', arg2: bool) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,java.lang.Class<T>,boolean)"""
        return object._wrap(super(_AssetManager, self).get(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def load(self, arg0: 'AssetDescriptor'):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.load(com.badlogic.gdx.assets.AssetDescriptor)"""
        super(_AssetManager, self).load(arg0)

    @overload
    def getFileHandleResolver(self) -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.assets.AssetManager.getFileHandleResolver()"""
        return 'loaders.FileHandleResolver'._wrap(super(AssetManager, self).getFileHandleResolver())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'AssetDescriptor') -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(com.badlogic.gdx.assets.AssetDescriptor<T>)"""
        return object._wrap(super(_AssetManager, self).get(arg0))

    @overload
    def getAssetType(self, arg0: str) -> 'type.Class':
        """public synchronized java.lang.Class com.badlogic.gdx.assets.AssetManager.getAssetType(java.lang.String)"""
        return 'type.Class'._wrap(super(_AssetManager, self).getAssetType(arg0))

    @overload
    def getProgress(self) -> float:
        """public synchronized float com.badlogic.gdx.assets.AssetManager.getProgress()"""
        return float._wrap(super(AssetManager, self).getProgress())

    @overload
    def isFinished(self) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isFinished()"""
        return bool._wrap(super(AssetManager, self).isFinished())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setErrorListener(self, arg0: 'AssetErrorListener'):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.setErrorListener(com.badlogic.gdx.assets.AssetErrorListener)"""
        super(_AssetManager, self).setErrorListener(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.assets.AssetManager.dispose()"""
        super(AssetManager, self).dispose()

    @overload
    def setReferenceCount(self, arg0: str, arg1: int):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.setReferenceCount(java.lang.String,int)"""
        super(_AssetManager, self).setReferenceCount(arg0, _int.valueOf(arg1))

    @overload
    def isLoaded(self, arg0: str, arg1: 'Class') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(java.lang.String,java.lang.Class)"""
        return bool._wrap(super(_AssetManager, self).isLoaded(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def update(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.assets.AssetManager.update(int)"""
        return bool._wrap(super(_AssetManager, self).update(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: str, arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public synchronized <T> void com.badlogic.gdx.assets.AssetManager.load(java.lang.String,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        super(_AssetManager, self).load(arg0, arg1, arg2)

    @overload
    def getDependencies(self, arg0: str) -> 'utils.Array':
        """public synchronized com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.assets.AssetManager.getDependencies(java.lang.String)"""
        return 'utils.Array'._wrap(super(_AssetManager, self).getDependencies(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDiagnostics(self) -> str:
        """public synchronized java.lang.String com.badlogic.gdx.assets.AssetManager.getDiagnostics()"""
        return str._wrap(super(AssetManager, self).getDiagnostics())

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void com.badlogic.gdx.assets.AssetManager.setLogger(com.badlogic.gdx.utils.Logger)"""
        super(_AssetManager, self).setLogger(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def update(self) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.update()"""
        return bool._wrap(super(AssetManager, self).update())

    @overload
    def get(self, arg0: str, arg1: 'Class') -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,java.lang.Class<T>)"""
        return object._wrap(super(_AssetManager, self).get(arg0, arg1))

    @overload
    def load(self, arg0: str, arg1: 'Class'):
        """public synchronized <T> void com.badlogic.gdx.assets.AssetManager.load(java.lang.String,java.lang.Class<T>)"""
        super(_AssetManager, self).load(arg0, arg1)

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.AssetManager(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _AssetManager(arg0)
        self.__wrapper = val

    @overload
    def get(self, arg0: str, arg1: bool) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,boolean)"""
        return object._wrap(super(_AssetManager, self).get(arg0, _boolean.valueOf(arg1)))

    @overload
    def getLoader(self, arg0: 'Class', arg1: str) -> 'loaders.AssetLoader':
        """public <T> com.badlogic.gdx.assets.loaders.AssetLoader com.badlogic.gdx.assets.AssetManager.getLoader(java.lang.Class<T>,java.lang.String)"""
        return 'loaders.AssetLoader'._wrap(super(_AssetManager, self).getLoader(arg0, arg1))

    @overload
    def finishLoading(self):
        """public void com.badlogic.gdx.assets.AssetManager.finishLoading()"""
        super(AssetManager, self).finishLoading()

    @overload
    def getLoadedAssets(self) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getLoadedAssets()"""
        return int._wrap(super(AssetManager, self).getLoadedAssets())

    @overload
    def setLoader(self, arg0: 'Class', arg1: str, arg2: 'AssetLoader'):
        """public synchronized <T,P extends com.badlogic.gdx.assets.AssetLoaderParameters<T>> void com.badlogic.gdx.assets.AssetManager.setLoader(java.lang.Class<T>,java.lang.String,com.badlogic.gdx.assets.loaders.AssetLoader<T, P>)"""
        super(_AssetManager, self).setLoader(arg0, arg1, arg2)

    @overload
    def getReferenceCount(self, arg0: str) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getReferenceCount(java.lang.String)"""
        return int._wrap(super(_AssetManager, self).getReferenceCount(arg0))

    @overload
    def get(self, arg0: str) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String)"""
        return object._wrap(super(_AssetManager, self).get(arg0))

    @overload
    def getAssetNames(self) -> 'utils.Array':
        """public synchronized com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.assets.AssetManager.getAssetNames()"""
        return 'utils.Array'._wrap(super(AssetManager, self).getAssetNames())

    @overload
    def getLogger(self) -> 'utils.Logger':
        """public com.badlogic.gdx.utils.Logger com.badlogic.gdx.assets.AssetManager.getLogger()"""
        return 'utils.Logger'._wrap(super(AssetManager, self).getLogger())

    @overload
    def getAssetFileName(self, arg0: object) -> str:
        """public synchronized <T> java.lang.String com.badlogic.gdx.assets.AssetManager.getAssetFileName(T)"""
        return str._wrap(super(_AssetManager, self).getAssetFileName(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.assets.AssetManager.clear()"""
        super(AssetManager, self).clear()

    @overload
    def setLoader(self, arg0: 'Class', arg1: 'AssetLoader'):
        """public synchronized <T,P extends com.badlogic.gdx.assets.AssetLoaderParameters<T>> void com.badlogic.gdx.assets.AssetManager.setLoader(java.lang.Class<T>,com.badlogic.gdx.assets.loaders.AssetLoader<T, P>)"""
        super(_AssetManager, self).setLoader(arg0, arg1)

    @overload
    def containsAsset(self, arg0: object) -> bool:
        """public synchronized <T> boolean com.badlogic.gdx.assets.AssetManager.containsAsset(T)"""
        return bool._wrap(super(_AssetManager, self).containsAsset(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getQueuedAssets(self) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getQueuedAssets()"""
        return int._wrap(super(AssetManager, self).getQueuedAssets())

    @overload
    def contains(self, arg0: str, arg1: 'Class') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.contains(java.lang.String,java.lang.Class)"""
        return bool._wrap(super(_AssetManager, self).contains(arg0, arg1))

    @overload
    def getAll(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public synchronized <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.assets.AssetManager.getAll(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'._wrap(super(_AssetManager, self).getAll(arg0, arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.AssetManager()"""
        val = _AssetManager()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'FileHandleResolver', arg1: bool):
        """public com.badlogic.gdx.assets.AssetManager(com.badlogic.gdx.assets.loaders.FileHandleResolver,boolean)"""
        val = _AssetManager(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isLoaded(self, arg0: 'AssetDescriptor') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(com.badlogic.gdx.assets.AssetDescriptor)"""
        return bool._wrap(super(_AssetManager, self).isLoaded(arg0))

    @overload
    def finishLoadingAsset(self, arg0: str) -> object:
        """public <T> T com.badlogic.gdx.assets.AssetManager.finishLoadingAsset(java.lang.String)"""
        return object._wrap(super(_AssetManager, self).finishLoadingAsset(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.AssetManager()"""
        val = _AssetManager()
        self.__wrapper = val

    @overload
    def unload(self, arg0: str):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.unload(java.lang.String)"""
        super(_AssetManager, self).unload(arg0)

    @overload
    def finishLoadingAsset(self, arg0: 'AssetDescriptor') -> object:
        """public <T> T com.badlogic.gdx.assets.AssetManager.finishLoadingAsset(com.badlogic.gdx.assets.AssetDescriptor)"""
        return object._wrap(super(_AssetManager, self).finishLoadingAsset(arg0)) 
 
 
# CLASS: com.badlogic.gdx.assets.AssetLoaderParameters$LoadedCallback
import com.badlogic.gdx.assets.AssetLoaderParameters as _AssetLoaderParameters_LoadedCallback
_LoadedCallback = _AssetLoaderParameters_LoadedCallback.LoadedCallback
from builtins import type
from abc import abstractmethod, ABC
 
class LoadedCallback():
    """com.badlogic.gdx.assets.AssetLoaderParameters.LoadedCallback"""
 
    @staticmethod
    def _wrap(java_value: _LoadedCallback) -> 'LoadedCallback':
        return LoadedCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadedCallback):
        """
        Dynamic initializer for LoadedCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadedCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadedCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def finishedLoading(self, arg0: 'AssetManager', arg1: str, arg2: 'Class'):
        """public abstract void com.badlogic.gdx.assets.AssetLoaderParameters$LoadedCallback.finishedLoading(com.badlogic.gdx.assets.AssetManager,java.lang.String,java.lang.Class)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.assets.AssetLoaderParameters
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.assets.AssetLoaderParameters as _AssetLoaderParameters
_AssetLoaderParameters = _AssetLoaderParameters
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetLoaderParameters():
    """com.badlogic.gdx.assets.AssetLoaderParameters"""
 
    @staticmethod
    def _wrap(java_value: _AssetLoaderParameters) -> 'AssetLoaderParameters':
        return AssetLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetLoaderParameters):
        """
        Dynamic initializer for AssetLoaderParameters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetLoaderParameters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetLoaderParameters__wrapper":
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
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = _AssetLoaderParameters()
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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = _AssetLoaderParameters()
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
 
 
# CLASS: com.badlogic.gdx.assets.AssetDescriptor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.assets.AssetDescriptor as _AssetDescriptor
_AssetDescriptor = _AssetDescriptor
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetDescriptor():
    """com.badlogic.gdx.assets.AssetDescriptor"""
 
    @staticmethod
    def _wrap(java_value: _AssetDescriptor) -> 'AssetDescriptor':
        return AssetDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetDescriptor):
        """
        Dynamic initializer for AssetDescriptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetDescriptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetDescriptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Class'):
        """public com.badlogic.gdx.assets.AssetDescriptor(com.badlogic.gdx.files.FileHandle,java.lang.Class<T>)"""
        val = _AssetDescriptor(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public com.badlogic.gdx.assets.AssetDescriptor(java.lang.String,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        val = _AssetDescriptor(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.assets.AssetDescriptor.toString()"""
        return str._wrap(super(AssetDescriptor, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public com.badlogic.gdx.assets.AssetDescriptor(com.badlogic.gdx.files.FileHandle,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        val = _AssetDescriptor(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.assets.AssetDescriptor(java.lang.String,java.lang.Class<T>)"""
        val = _AssetDescriptor(arg0, arg1)
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