from __future__ import annotations
from overload import overload


 
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import dev.ultreon.quantum.resources.DynamicResource as _DynamicResource
_DynamicResource = _DynamicResource
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import de.marhali.json5.Json5Element as Json5Element
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import de.marhali.json5.Json5Element as _Json5Element
_Json5Element = _Json5Element
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.resources.Resource as _Resource
_Resource = _Resource
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicResource():
    """dev.ultreon.quantum.resources.DynamicResource"""
 
    @staticmethod
    def _wrap(java_value: _DynamicResource) -> 'DynamicResource':
        return DynamicResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicResource):
        """
        Dynamic initializer for DynamicResource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicResource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicResource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.DynamicResource.getData()"""
        return List[int]._wrap(super(DynamicResource, self).getData())

    @staticmethod
    @overload
    def of(arg0: 'Loader') -> 'DynamicResource':
        """public static dev.ultreon.quantum.resources.DynamicResource dev.ultreon.quantum.resources.DynamicResource.of(dev.ultreon.quantum.resources.DynamicResource$Loader)"""
        return DynamicResource._wrap(_DynamicResource.of(arg0))

    @override
    @overload
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'._wrap(super(Resource, self).openStream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.resources.DynamicResource.load()"""
        super(DynamicResource, self).load()

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
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool._wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int]._wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object._wrap(super(_Resource, self).loadJson(arg0))

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.DynamicResource.isLoaded()"""
        return bool._wrap(super(DynamicResource, self).isLoaded())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'._wrap(super(Resource, self).loadJson5())

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
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'._wrap(super(Resource, self).openReader())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import dev.ultreon.quantum.resources.DynamicResource as _DynamicResource
_DynamicResource = _DynamicResource
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import de.marhali.json5.Json5Element as Json5Element
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import de.marhali.json5.Json5Element as _Json5Element
_Json5Element = _Json5Element
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.resources.Resource as _Resource
_Resource = _Resource
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicResource():
    """dev.ultreon.quantum.resources.DynamicResource"""
 
    @staticmethod
    def _wrap(java_value: _DynamicResource) -> 'DynamicResource':
        return DynamicResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicResource):
        """
        Dynamic initializer for DynamicResource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicResource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicResource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.DynamicResource.getData()"""
        return List[int]._wrap(super(DynamicResource, self).getData())

    @staticmethod
    @overload
    def of(arg0: 'Loader') -> 'DynamicResource':
        """public static dev.ultreon.quantum.resources.DynamicResource dev.ultreon.quantum.resources.DynamicResource.of(dev.ultreon.quantum.resources.DynamicResource$Loader)"""
        return DynamicResource._wrap(_DynamicResource.of(arg0))

    @override
    @overload
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'._wrap(super(Resource, self).openStream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.resources.DynamicResource.load()"""
        super(DynamicResource, self).load()

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
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool._wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int]._wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object._wrap(super(_Resource, self).loadJson(arg0))

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.DynamicResource.isLoaded()"""
        return bool._wrap(super(DynamicResource, self).isLoaded())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'._wrap(super(Resource, self).loadJson5())

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
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'._wrap(super(Resource, self).openReader())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource 
 
 
# CLASS: dev.ultreon.quantum.resources.Resource
import java.io.Reader as _Reader
_Reader = _Reader
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import de.marhali.json5.Json5Element as Json5Element
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import de.marhali.json5.Json5Element as _Json5Element
_Json5Element = _Json5Element
from builtins import bool
import dev.ultreon.quantum.resources.Resource as _Resource
_Resource = _Resource
from builtins import int
 
class Resource():
    """dev.ultreon.quantum.resources.Resource"""
 
    @staticmethod
    def _wrap(java_value: _Resource) -> 'Resource':
        return Resource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Resource):
        """
        Dynamic initializer for Resource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Resource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Resource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def load(self, ):
        """public abstract void dev.ultreon.quantum.resources.Resource.load()"""
        pass

    @abstractmethod
    def getData(self, ):
        """public abstract byte[] dev.ultreon.quantum.resources.Resource.getData()"""
        pass

    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool._wrap(super(Resource, self).isNotLoaded())

    @overload
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'._wrap(super(Resource, self).openStream())

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object._wrap(super(_Resource, self).loadJson(arg0))

    @overload
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'._wrap(super(Resource, self).openReader())

    @abstractmethod
    def isLoaded(self, ):
        """public abstract boolean dev.ultreon.quantum.resources.Resource.isLoaded()"""
        pass

    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int]._wrap(super(Resource, self).loadOrGet())

    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'._wrap(super(Resource, self).loadJson5()) 
 
 
# CLASS: dev.ultreon.quantum.resources.ReloadContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.resources.ReloadContext as _ReloadContext
_ReloadContext = _ReloadContext
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.concurrent.CompletableFuture as CompletableFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReloadContext():
    """dev.ultreon.quantum.resources.ReloadContext"""
 
    @staticmethod
    def _wrap(java_value: _ReloadContext) -> 'ReloadContext':
        return ReloadContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReloadContext):
        """
        Dynamic initializer for ReloadContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReloadContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReloadContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PollingExecutorService', arg1: 'ResourceManager'):
        """public dev.ultreon.quantum.resources.ReloadContext(dev.ultreon.quantum.util.PollingExecutorService,dev.ultreon.quantum.resources.ResourceManager)"""
        val = _ReloadContext(arg0, arg1)
        self.__wrapper = val

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.resources.ReloadContext.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_ReloadContext, self).submit(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getResourceManager(self) -> 'ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.resources.ReloadContext.getResourceManager()"""
        return 'ResourceManager'._wrap(super(ReloadContext, self).getResourceManager())

    @staticmethod
    @overload
    def create(arg0: 'PollingExecutorService', arg1: 'ResourceManager') -> 'ReloadContext':
        """public static dev.ultreon.quantum.resources.ReloadContext dev.ultreon.quantum.resources.ReloadContext.create(dev.ultreon.quantum.util.PollingExecutorService,dev.ultreon.quantum.resources.ResourceManager)"""
        return ReloadContext._wrap(_ReloadContext.create(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isDone(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.ReloadContext.isDone()"""
        return bool._wrap(super(ReloadContext, self).isDone())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def submit(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.resources.ReloadContext.submit(java.lang.Runnable)"""
        super(_ReloadContext, self).submit(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def finish(self):
        """public void dev.ultreon.quantum.resources.ReloadContext.finish()"""
        super(ReloadContext, self).finish()

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
 
 
# CLASS: dev.ultreon.quantum.resources.ResourceCategory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as _StaticResource
_StaticResource = _StaticResource
import java.lang.String as _string
import java.util.Set as Set
import dev.ultreon.quantum.resources.ResourceCategory as _ResourceCategory
_ResourceCategory = _ResourceCategory
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceCategory():
    """dev.ultreon.quantum.resources.ResourceCategory"""
 
    @staticmethod
    def _wrap(java_value: _ResourceCategory) -> 'ResourceCategory':
        return ResourceCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceCategory):
        """
        Dynamic initializer for ResourceCategory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceCategory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceCategory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourceCategory.mapEntries()"""
        return 'Map'._wrap(super(ResourceCategory, self).mapEntries())

    @overload
    def get(self, arg0: 'Identifier') -> 'StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.ResourceCategory.get(dev.ultreon.quantum.util.Identifier)"""
        return 'StaticResource'._wrap(super(_ResourceCategory, self).get(arg0))

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
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourceCategory.has(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_ResourceCategory, self).has(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.resources.ResourceCategory.getName()"""
        return str._wrap(super(ResourceCategory, self).getName())

    @overload
    def resourceCount(self) -> int:
        """public int dev.ultreon.quantum.resources.ResourceCategory.resourceCount()"""
        return int._wrap(super(ResourceCategory, self).resourceCount())

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
    def resources(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourceCategory.resources()"""
        return 'List'._wrap(super(ResourceCategory, self).resources())

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
    def forEach(self, arg0: 'BiConsumer'):
        """public void dev.ultreon.quantum.resources.ResourceCategory.forEach(java.util.function.BiConsumer<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource>)"""
        super(_ResourceCategory, self).forEach(arg0)

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourceCategory.entries()"""
        return 'Set'._wrap(super(ResourceCategory, self).entries())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.resources.ResourceCategory(java.lang.String)"""
        val = _ResourceCategory(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource$Loader
import dev.ultreon.quantum.resources.DynamicResource as _DynamicResource_Loader
_Loader = _DynamicResource_Loader.Loader
from abc import abstractmethod, ABC
 
class Loader():
    """dev.ultreon.quantum.resources.DynamicResource.Loader"""
 
    @staticmethod
    def _wrap(java_value: _Loader) -> 'Loader':
        return Loader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Loader):
        """
        Dynamic initializer for Loader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Loader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Loader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract byte[] dev.ultreon.quantum.resources.DynamicResource$Loader.get()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.resources.ResourceManager
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.io.File as File
import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import dev.ultreon.quantum.resources.Resource as _Resource
_Resource = _Resource
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceManager():
    """dev.ultreon.quantum.resources.ResourceManager"""
 
    @staticmethod
    def _wrap(java_value: _ResourceManager) -> 'ResourceManager':
        return ResourceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceManager):
        """
        Dynamic initializer for ResourceManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reload(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.reload()"""
        super(ResourceManager, self).reload()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.resources.ResourceManager(java.lang.String)"""
        val = _ResourceManager(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def importPackage(self, arg0: 'URI'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.net.URI) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def getAllDataByPath(self, arg0: str) -> 'List':
        """public java.util.List<byte[]> dev.ultreon.quantum.resources.ResourceManager.getAllDataByPath(java.lang.String)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataByPath(arg0))

    @overload
    def openResourceStream(self, arg0: 'Identifier') -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.resources.ResourceManager.openResourceStream(dev.ultreon.quantum.util.Identifier) throws java.io.IOException"""
        return 'InputStream'._wrap(super(_ResourceManager, self).openResourceStream(arg0))

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
    def getResourcePackages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourcePackage> dev.ultreon.quantum.resources.ResourceManager.getResourcePackages()"""
        return 'List'._wrap(super(ResourceManager, self).getResourcePackages())

    @overload
    def getResourceCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourceManager.getResourceCategories()"""
        return 'List'._wrap(super(ResourceManager, self).getResourceCategories())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getResource(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.quantum.resources.Resource dev.ultreon.quantum.resources.ResourceManager.getResource(dev.ultreon.quantum.util.Identifier)"""
        return 'Resource'._wrap(super(_ResourceManager, self).getResource(arg0))

    @overload
    def canScanFiles(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourceManager.canScanFiles()"""
        return bool._wrap(super(ResourceManager, self).canScanFiles())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAllDataById(self, arg0: 'Identifier') -> 'List':
        """public java.util.List<byte[]> dev.ultreon.quantum.resources.ResourceManager.getAllDataById(dev.ultreon.quantum.util.Identifier)"""
        return 'List'._wrap(super(_ResourceManager, self).getAllDataById(arg0))

    @overload
    def importDeferredPackage(self, arg0: 'Class'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importDeferredPackage(java.lang.Class<?>)"""
        super(_ResourceManager, self).importDeferredPackage(arg0)

    @overload
    def getResourceCategory(self, arg0: str) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourceManager.getResourceCategory(java.lang.String)"""
        return 'List'._wrap(super(_ResourceManager, self).getResourceCategory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getRoot(self) -> str:
        """public java.lang.String dev.ultreon.quantum.resources.ResourceManager.getRoot()"""
        return str._wrap(super(ResourceManager, self).getRoot())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.close()"""
        super(ResourceManager, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def importPackage(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.nio.file.Path) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @overload
    def importPackage(self, arg0: 'File'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.io.File) throws java.io.IOException"""
        super(_ResourceManager, self).importPackage(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def importModResources(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.importModResources()"""
        super(ResourceManager, self).importModResources()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.resources.ResourcePackage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as _StaticResource
_StaticResource = _StaticResource
import java.lang.String as _string
import java.util.Set as Set
import dev.ultreon.quantum.resources.ResourceCategory as _ResourceCategory
_ResourceCategory = _ResourceCategory
import java.lang.Integer as _int
import dev.ultreon.quantum.resources.ResourcePackage as _ResourcePackage
_ResourcePackage = _ResourcePackage
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourcePackage():
    """dev.ultreon.quantum.resources.ResourcePackage"""
 
    @staticmethod
    def _wrap(java_value: _ResourcePackage) -> 'ResourcePackage':
        return ResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourcePackage):
        """
        Dynamic initializer for ResourcePackage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourcePackage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourcePackage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'._wrap(super(ResourcePackage, self).entries())

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool._wrap(super(_ResourcePackage, self).has(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCategory(self, arg0: str) -> 'ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'ResourceCategory'._wrap(super(_ResourcePackage, self).getCategory(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'Map'):
        """public dev.ultreon.quantum.resources.ResourcePackage(java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource>,java.util.Map<java.lang.String, dev.ultreon.quantum.resources.ResourceCategory>)"""
        val = _ResourcePackage(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'._wrap(super(ResourcePackage, self).mapEntries())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: 'Identifier') -> 'StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.ResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'StaticResource'._wrap(super(_ResourcePackage, self).get(arg0))

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
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool._wrap(super(_ResourcePackage, self).hasCategory(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.resources.ResourcePackage()"""
        val = _ResourcePackage()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.resources.ResourcePackage()"""
        val = _ResourcePackage()
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(ResourcePackage, self).close()

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'._wrap(super(ResourcePackage, self).getCategories())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.resources.StaticResource
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = _import_once("pycorelibs.functions.v0.misc")

import dev.ultreon.quantum.resources.StaticResource as _StaticResource
_StaticResource = _StaticResource
import java.io.ByteArrayInputStream as ByteArrayInputStream
from builtins import bool
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.ByteArrayInputStream as _ByteArrayInputStream
_ByteArrayInputStream = _ByteArrayInputStream
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.io.InputStream as _InputStream
_InputStream = _InputStream
import de.marhali.json5.Json5Element as Json5Element
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import de.marhali.json5.Json5Element as _Json5Element
_Json5Element = _Json5Element
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import java.lang.Long as _long
import dev.ultreon.quantum.resources.Resource as _Resource
_Resource = _Resource
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StaticResource():
    """dev.ultreon.quantum.resources.StaticResource"""
 
    @staticmethod
    def _wrap(java_value: _StaticResource) -> 'StaticResource':
        return StaticResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StaticResource):
        """
        Dynamic initializer for StaticResource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StaticResource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StaticResource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.StaticResource.close()"""
        super(StaticResource, self).close()

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
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.StaticResource.getData()"""
        return List[int]._wrap(super(StaticResource, self).getData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool._wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.StaticResource.isLoaded()"""
        return bool._wrap(super(StaticResource, self).isLoaded())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int]._wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def load(self):
        """public void dev.ultreon.quantum.resources.StaticResource.load()"""
        super(StaticResource, self).load()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.resources.StaticResource.id()"""
        return 'util.Identifier'._wrap(super(StaticResource, self).id())

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object._wrap(super(_Resource, self).loadJson(arg0))

    @overload
    def loadOrOpenStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.resources.StaticResource.loadOrOpenStream()"""
        return 'InputStream'._wrap(super(StaticResource, self).loadOrOpenStream())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'._wrap(super(Resource, self).loadJson5())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ThrowingSupplier'):
        """public dev.ultreon.quantum.resources.StaticResource(dev.ultreon.quantum.util.Identifier,dev.ultreon.libs.functions.v0.misc.ThrowingSupplier<java.io.InputStream, java.io.IOException>)"""
        val = _StaticResource(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'._wrap(super(Resource, self).openReader())

    @override
    @overload
    def openStream(self) -> 'ByteArrayInputStream':
        """public java.io.ByteArrayInputStream dev.ultreon.quantum.resources.StaticResource.openStream()"""
        return 'ByteArrayInputStream'._wrap(super(StaticResource, self).openStream())

    @overload
    def readJson5(self) -> 'Json5Element':
        """public de.marhali.json5.Json5Element dev.ultreon.quantum.resources.StaticResource.readJson5()"""
        return 'Json5Element'._wrap(super(StaticResource, self).readJson5())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())