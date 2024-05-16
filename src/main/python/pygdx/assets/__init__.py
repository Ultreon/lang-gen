from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.assets.AssetLoaderParameters as __AssetLoaderParameters
__AssetLoaderParameters = __AssetLoaderParameters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetLoaderParameters():
    """com.badlogic.gdx.assets.AssetLoaderParameters"""
 
    @staticmethod
    def __wrap(java_value: __AssetLoaderParameters) -> 'AssetLoaderParameters':
        return AssetLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetLoaderParameters):
        """
        Dynamic initializer for AssetLoaderParameters.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = __AssetLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = __AssetLoaderParameters()
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

 
 
 
# CLASS: com.badlogic.gdx.assets.AssetLoaderParameters
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
import com.badlogic.gdx.assets.AssetLoaderParameters as __AssetLoaderParameters
__AssetLoaderParameters = __AssetLoaderParameters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetLoaderParameters():
    """com.badlogic.gdx.assets.AssetLoaderParameters"""
 
    @staticmethod
    def __wrap(java_value: __AssetLoaderParameters) -> 'AssetLoaderParameters':
        return AssetLoaderParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetLoaderParameters):
        """
        Dynamic initializer for AssetLoaderParameters.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = __AssetLoaderParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.assets.AssetLoaderParameters()"""
        val = __AssetLoaderParameters()
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

 
 
 
# CLASS: com.badlogic.gdx.assets.AssetLoaderParameters 
 
 
# CLASS: com.badlogic.gdx.assets.AssetDescriptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.assets.AssetDescriptor as __AssetDescriptor
__AssetDescriptor = __AssetDescriptor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class AssetDescriptor():
    """com.badlogic.gdx.assets.AssetDescriptor"""
 
    @staticmethod
    def __wrap(java_value: __AssetDescriptor) -> 'AssetDescriptor':
        return AssetDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetDescriptor):
        """
        Dynamic initializer for AssetDescriptor.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public com.badlogic.gdx.assets.AssetDescriptor(com.badlogic.gdx.files.FileHandle,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        val = __AssetDescriptor(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.assets.AssetDescriptor(java.lang.String,java.lang.Class<T>)"""
        val = __AssetDescriptor(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public com.badlogic.gdx.assets.AssetDescriptor(java.lang.String,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        val = __AssetDescriptor(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
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
        return str.__wrap(super(AssetDescriptor, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Class'):
        """public com.badlogic.gdx.assets.AssetDescriptor(com.badlogic.gdx.files.FileHandle,java.lang.Class<T>)"""
        val = __AssetDescriptor(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.assets.AssetLoaderParameters$LoadedCallback
from builtins import type
import com.badlogic.gdx.assets.AssetLoaderParameters as __AssetLoaderParameters_LoadedCallback
__LoadedCallback = __AssetLoaderParameters_LoadedCallback.LoadedCallback
from abc import abstractmethod, ABC
 
class LoadedCallback(ABC):
    """com.badlogic.gdx.assets.AssetLoaderParameters.LoadedCallback"""
 
    @staticmethod
    def __wrap(java_value: __LoadedCallback) -> 'LoadedCallback':
        return LoadedCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadedCallback):
        """
        Dynamic initializer for LoadedCallback.
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
    def finishedLoading(self, arg0: 'AssetManager', arg1: str, arg2: 'Class'):
        """public abstract void com.badlogic.gdx.assets.AssetLoaderParameters$LoadedCallback.finishedLoading(com.badlogic.gdx.assets.AssetManager,java.lang.String,java.lang.Class)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.assets.AssetErrorListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.badlogic.gdx.assets.AssetErrorListener as __AssetErrorListener
__AssetErrorListener = __AssetErrorListener
 
class AssetErrorListener(ABC):
    """com.badlogic.gdx.assets.AssetErrorListener"""
 
    @staticmethod
    def __wrap(java_value: __AssetErrorListener) -> 'AssetErrorListener':
        return AssetErrorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetErrorListener):
        """
        Dynamic initializer for AssetErrorListener.
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
    def error(self, arg0: 'AssetDescriptor', arg1: 'Throwable'):
        """public abstract void com.badlogic.gdx.assets.AssetErrorListener.error(com.badlogic.gdx.assets.AssetDescriptor,java.lang.Throwable)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.assets.AssetManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.Logger as __Logger
__Logger = __Logger
from builtins import float
import com.badlogic.gdx.assets.AssetManager as __AssetManager
__AssetManager = __AssetManager
from builtins import object
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
import com.badlogic.gdx.assets.loaders.FileHandleResolver as __FileHandleResolver
__FileHandleResolver = __FileHandleResolver
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetManager(pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.assets.AssetManager"""
 
    @staticmethod
    def __wrap(java_value: __AssetManager) -> 'AssetManager':
        return AssetManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetManager):
        """
        Dynamic initializer for AssetManager.
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
    def get(self, arg0: str, arg1: 'Class') -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,java.lang.Class<T>)"""
        return object.__wrap(super(__AssetManager, self).get(arg0, arg1))

    @overload
    def setLoader(self, arg0: 'Class', arg1: 'AssetLoader'):
        """public synchronized <T,P extends com.badlogic.gdx.assets.AssetLoaderParameters<T>> void com.badlogic.gdx.assets.AssetManager.setLoader(java.lang.Class<T>,com.badlogic.gdx.assets.loaders.AssetLoader<T, P>)"""
        super(__AssetManager, self).setLoader(arg0, arg1)

    @overload
    def __init__(self, arg0: 'FileHandleResolver', arg1: bool):
        """public com.badlogic.gdx.assets.AssetManager(com.badlogic.gdx.assets.loaders.FileHandleResolver,boolean)"""
        val = __AssetManager(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getQueuedAssets(self) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getQueuedAssets()"""
        return int.__wrap(super(AssetManager, self).getQueuedAssets())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def finishLoadingAsset(self, arg0: 'AssetDescriptor') -> object:
        """public <T> T com.badlogic.gdx.assets.AssetManager.finishLoadingAsset(com.badlogic.gdx.assets.AssetDescriptor)"""
        return object.__wrap(super(__AssetManager, self).finishLoadingAsset(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.assets.AssetManager.dispose()"""
        super(AssetManager, self).dispose()

    @overload
    def unload(self, arg0: str):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.unload(java.lang.String)"""
        super(__AssetManager, self).unload(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getAssetFileName(self, arg0: object) -> str:
        """public synchronized <T> java.lang.String com.badlogic.gdx.assets.AssetManager.getAssetFileName(T)"""
        return str.__wrap(super(__AssetManager, self).getAssetFileName(arg0))

    @overload
    def load(self, arg0: 'AssetDescriptor'):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.load(com.badlogic.gdx.assets.AssetDescriptor)"""
        super(__AssetManager, self).load(arg0)

    @overload
    def load(self, arg0: str, arg1: 'Class'):
        """public synchronized <T> void com.badlogic.gdx.assets.AssetManager.load(java.lang.String,java.lang.Class<T>)"""
        super(__AssetManager, self).load(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAll(self, arg0: 'Class', arg1: 'Array') -> 'utils.Array':
        """public synchronized <T> com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.assets.AssetManager.getAll(java.lang.Class<T>,com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'.__wrap(super(__AssetManager, self).getAll(arg0, arg1))

    @overload
    def setLogger(self, arg0: 'Logger'):
        """public void com.badlogic.gdx.assets.AssetManager.setLogger(com.badlogic.gdx.utils.Logger)"""
        super(__AssetManager, self).setLogger(arg0)

    @overload
    def getAssetType(self, arg0: str) -> 'type.Class':
        """public synchronized java.lang.Class com.badlogic.gdx.assets.AssetManager.getAssetType(java.lang.String)"""
        return 'type.Class'.__wrap(super(__AssetManager, self).getAssetType(arg0))

    @overload
    def load(self, arg0: str, arg1: 'Class', arg2: 'AssetLoaderParameters'):
        """public synchronized <T> void com.badlogic.gdx.assets.AssetManager.load(java.lang.String,java.lang.Class<T>,com.badlogic.gdx.assets.AssetLoaderParameters<T>)"""
        super(__AssetManager, self).load(arg0, arg1, arg2)

    @overload
    def getLogger(self) -> 'utils.Logger':
        """public com.badlogic.gdx.utils.Logger com.badlogic.gdx.assets.AssetManager.getLogger()"""
        return 'utils.Logger'.__wrap(super(AssetManager, self).getLogger())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLoader(self, arg0: 'Class', arg1: str, arg2: 'AssetLoader'):
        """public synchronized <T,P extends com.badlogic.gdx.assets.AssetLoaderParameters<T>> void com.badlogic.gdx.assets.AssetManager.setLoader(java.lang.Class<T>,java.lang.String,com.badlogic.gdx.assets.loaders.AssetLoader<T, P>)"""
        super(__AssetManager, self).setLoader(arg0, arg1, arg2)

    @overload
    def setErrorListener(self, arg0: 'AssetErrorListener'):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.setErrorListener(com.badlogic.gdx.assets.AssetErrorListener)"""
        super(__AssetManager, self).setErrorListener(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def finishLoadingAsset(self, arg0: str) -> object:
        """public <T> T com.badlogic.gdx.assets.AssetManager.finishLoadingAsset(java.lang.String)"""
        return object.__wrap(super(__AssetManager, self).finishLoadingAsset(arg0))

    @overload
    def containsAsset(self, arg0: object) -> bool:
        """public synchronized <T> boolean com.badlogic.gdx.assets.AssetManager.containsAsset(T)"""
        return bool.__wrap(super(__AssetManager, self).containsAsset(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.assets.AssetManager()"""
        val = __AssetManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.assets.AssetManager(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __AssetManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isLoaded(self, arg0: str, arg1: 'Class') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(java.lang.String,java.lang.Class)"""
        return bool.__wrap(super(__AssetManager, self).isLoaded(arg0, arg1))

    @overload
    def get(self, arg0: str) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String)"""
        return object.__wrap(super(__AssetManager, self).get(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.contains(java.lang.String)"""
        return bool.__wrap(super(__AssetManager, self).contains(arg0))

    @overload
    def getReferenceCount(self, arg0: str) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getReferenceCount(java.lang.String)"""
        return int.__wrap(super(__AssetManager, self).getReferenceCount(arg0))

    @overload
    def get(self, arg0: str, arg1: bool) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,boolean)"""
        return object.__wrap(super(__AssetManager, self).get(arg0, __boolean.valueOf(arg1)))

    @overload
    def finishLoading(self):
        """public void com.badlogic.gdx.assets.AssetManager.finishLoading()"""
        super(AssetManager, self).finishLoading()

    @overload
    def getFileHandleResolver(self) -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.assets.AssetManager.getFileHandleResolver()"""
        return 'loaders.FileHandleResolver'.__wrap(super(AssetManager, self).getFileHandleResolver())

    @overload
    def getAssetNames(self) -> 'utils.Array':
        """public synchronized com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.assets.AssetManager.getAssetNames()"""
        return 'utils.Array'.__wrap(super(AssetManager, self).getAssetNames())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isLoaded(self, arg0: 'AssetDescriptor') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(com.badlogic.gdx.assets.AssetDescriptor)"""
        return bool.__wrap(super(__AssetManager, self).isLoaded(arg0))

    @overload
    def getProgress(self) -> float:
        """public synchronized float com.badlogic.gdx.assets.AssetManager.getProgress()"""
        return float.__wrap(super(AssetManager, self).getProgress())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.assets.AssetManager.clear()"""
        super(AssetManager, self).clear()

    @overload
    def getDiagnostics(self) -> str:
        """public synchronized java.lang.String com.badlogic.gdx.assets.AssetManager.getDiagnostics()"""
        return str.__wrap(super(AssetManager, self).getDiagnostics())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getLoadedAssets(self) -> int:
        """public synchronized int com.badlogic.gdx.assets.AssetManager.getLoadedAssets()"""
        return int.__wrap(super(AssetManager, self).getLoadedAssets())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def get(self, arg0: 'AssetDescriptor') -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(com.badlogic.gdx.assets.AssetDescriptor<T>)"""
        return object.__wrap(super(__AssetManager, self).get(arg0))

    @overload
    def getLoader(self, arg0: 'Class') -> 'loaders.AssetLoader':
        """public <T> com.badlogic.gdx.assets.loaders.AssetLoader com.badlogic.gdx.assets.AssetManager.getLoader(java.lang.Class<T>)"""
        return 'loaders.AssetLoader'.__wrap(super(__AssetManager, self).getLoader(arg0))

    @overload
    def getLoader(self, arg0: 'Class', arg1: str) -> 'loaders.AssetLoader':
        """public <T> com.badlogic.gdx.assets.loaders.AssetLoader com.badlogic.gdx.assets.AssetManager.getLoader(java.lang.Class<T>,java.lang.String)"""
        return 'loaders.AssetLoader'.__wrap(super(__AssetManager, self).getLoader(arg0, arg1))

    @overload
    def isFinished(self) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isFinished()"""
        return bool.__wrap(super(AssetManager, self).isFinished())

    @overload
    def get(self, arg0: str, arg1: 'Class', arg2: bool) -> object:
        """public synchronized <T> T com.badlogic.gdx.assets.AssetManager.get(java.lang.String,java.lang.Class<T>,boolean)"""
        return object.__wrap(super(__AssetManager, self).get(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def isLoaded(self, arg0: str) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.isLoaded(java.lang.String)"""
        return bool.__wrap(super(__AssetManager, self).isLoaded(arg0))

    @overload
    def update(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.assets.AssetManager.update(int)"""
        return bool.__wrap(super(__AssetManager, self).update(__int.valueOf(arg0)))

    @overload
    def setReferenceCount(self, arg0: str, arg1: int):
        """public synchronized void com.badlogic.gdx.assets.AssetManager.setReferenceCount(java.lang.String,int)"""
        super(__AssetManager, self).setReferenceCount(arg0, __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.assets.AssetManager()"""
        val = __AssetManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self) -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.update()"""
        return bool.__wrap(super(AssetManager, self).update())

    @overload
    def contains(self, arg0: str, arg1: 'Class') -> bool:
        """public synchronized boolean com.badlogic.gdx.assets.AssetManager.contains(java.lang.String,java.lang.Class)"""
        return bool.__wrap(super(__AssetManager, self).contains(arg0, arg1))

    @overload
    def getDependencies(self, arg0: str) -> 'utils.Array':
        """public synchronized com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.assets.AssetManager.getDependencies(java.lang.String)"""
        return 'utils.Array'.__wrap(super(__AssetManager, self).getDependencies(arg0))