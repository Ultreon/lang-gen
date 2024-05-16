from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import dev.ultreon.quantum.resources.DynamicResource as __DynamicResource
__DynamicResource = __DynamicResource
import java.lang.Long as __long
import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import java.lang.Class as __Class
__Class = __Class
import de.marhali.json5.Json5Element as Json5Element
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import java.lang.Integer as __int
from builtins import bool
import de.marhali.json5.Json5Element as __Json5Element
__Json5Element = __Json5Element
from builtins import int
 
class DynamicResource(ABC, __Resource, Resource):
    """dev.ultreon.quantum.resources.DynamicResource"""
 
    @staticmethod
    def __wrap(java_value: __DynamicResource) -> 'DynamicResource':
        return DynamicResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicResource):
        """
        Dynamic initializer for DynamicResource.
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
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'.__wrap(super(Resource, self).openStream())

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object.__wrap(super(__Resource, self).loadJson(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Loader') -> 'DynamicResource':
        """public static dev.ultreon.quantum.resources.DynamicResource dev.ultreon.quantum.resources.DynamicResource.of(dev.ultreon.quantum.resources.DynamicResource$Loader)"""
        return DynamicResource.__wrap(__DynamicResource.of(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool.__wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'.__wrap(super(Resource, self).loadJson5())

    @override
    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.DynamicResource.getData()"""
        return List[int].__wrap(super(DynamicResource, self).getData())

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

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.DynamicResource.isLoaded()"""
        return bool.__wrap(super(DynamicResource, self).isLoaded())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'.__wrap(super(Resource, self).openReader())

 
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import dev.ultreon.quantum.resources.DynamicResource as __DynamicResource
__DynamicResource = __DynamicResource
import java.lang.Long as __long
import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import java.lang.Class as __Class
__Class = __Class
import de.marhali.json5.Json5Element as Json5Element
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import java.lang.Integer as __int
from builtins import bool
import de.marhali.json5.Json5Element as __Json5Element
__Json5Element = __Json5Element
from builtins import int
 
class DynamicResource(ABC, __Resource, Resource):
    """dev.ultreon.quantum.resources.DynamicResource"""
 
    @staticmethod
    def __wrap(java_value: __DynamicResource) -> 'DynamicResource':
        return DynamicResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicResource):
        """
        Dynamic initializer for DynamicResource.
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
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'.__wrap(super(Resource, self).openStream())

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object.__wrap(super(__Resource, self).loadJson(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Loader') -> 'DynamicResource':
        """public static dev.ultreon.quantum.resources.DynamicResource dev.ultreon.quantum.resources.DynamicResource.of(dev.ultreon.quantum.resources.DynamicResource$Loader)"""
        return DynamicResource.__wrap(__DynamicResource.of(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool.__wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'.__wrap(super(Resource, self).loadJson5())

    @override
    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.DynamicResource.getData()"""
        return List[int].__wrap(super(DynamicResource, self).getData())

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

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.DynamicResource.isLoaded()"""
        return bool.__wrap(super(DynamicResource, self).isLoaded())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'.__wrap(super(Resource, self).openReader())

 
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource 
 
 
# CLASS: dev.ultreon.quantum.resources.Resource
from builtins import type
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import de.marhali.json5.Json5Element as Json5Element
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
from builtins import bool
import de.marhali.json5.Json5Element as __Json5Element
__Json5Element = __Json5Element
from builtins import int
 
class Resource(ABC):
    """dev.ultreon.quantum.resources.Resource"""
 
    @staticmethod
    def __wrap(java_value: __Resource) -> 'Resource':
        return Resource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Resource):
        """
        Dynamic initializer for Resource.
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
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'.__wrap(super(Resource, self).openReader())

    @abstractmethod
    def load(self, ):
        """public abstract void dev.ultreon.quantum.resources.Resource.load()"""
        pass

    @abstractmethod
    def getData(self, ):
        """public abstract byte[] dev.ultreon.quantum.resources.Resource.getData()"""
        pass

    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'.__wrap(super(Resource, self).loadJson5())

    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object.__wrap(super(__Resource, self).loadJson(arg0))

    @abstractmethod
    def isLoaded(self, ):
        """public abstract boolean dev.ultreon.quantum.resources.Resource.isLoaded()"""
        pass

    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool.__wrap(super(Resource, self).isNotLoaded())

    @overload
    def openStream(self) -> 'InputStream':
        """public default java.io.InputStream dev.ultreon.quantum.resources.Resource.openStream() throws java.io.IOException"""
        return 'InputStream'.__wrap(super(Resource, self).openStream()) 
 
 
# CLASS: dev.ultreon.quantum.resources.ReloadContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
from pyquantum_helper import override
import dev.ultreon.quantum.resources.ReloadContext as __ReloadContext
__ReloadContext = __ReloadContext
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import java.lang.Runnable as Runnable
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
 
class ReloadContext():
    """dev.ultreon.quantum.resources.ReloadContext"""
 
    @staticmethod
    def __wrap(java_value: __ReloadContext) -> 'ReloadContext':
        return ReloadContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReloadContext):
        """
        Dynamic initializer for ReloadContext.
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
    def submit(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.resources.ReloadContext.submit(java.lang.Runnable)"""
        super(__ReloadContext, self).submit(arg0)

    @overload
    def isDone(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.ReloadContext.isDone()"""
        return bool.__wrap(super(ReloadContext, self).isDone())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def create(arg0: 'PollingExecutorService', arg1: 'ResourceManager') -> 'ReloadContext':
        """public static dev.ultreon.quantum.resources.ReloadContext dev.ultreon.quantum.resources.ReloadContext.create(dev.ultreon.quantum.util.PollingExecutorService,dev.ultreon.quantum.resources.ResourceManager)"""
        return ReloadContext.__wrap(__ReloadContext.create(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.resources.ReloadContext.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__ReloadContext, self).submit(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'PollingExecutorService', arg1: 'ResourceManager'):
        """public dev.ultreon.quantum.resources.ReloadContext(dev.ultreon.quantum.util.PollingExecutorService,dev.ultreon.quantum.resources.ResourceManager)"""
        val = __ReloadContext(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getResourceManager(self) -> 'ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.resources.ReloadContext.getResourceManager()"""
        return 'ResourceManager'.__wrap(super(ReloadContext, self).getResourceManager()) 
 
 
# CLASS: dev.ultreon.quantum.resources.ResourceCategory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.resources.ResourceCategory as __ResourceCategory
__ResourceCategory = __ResourceCategory
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as __StaticResource
__StaticResource = __StaticResource
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ResourceCategory():
    """dev.ultreon.quantum.resources.ResourceCategory"""
 
    @staticmethod
    def __wrap(java_value: __ResourceCategory) -> 'ResourceCategory':
        return ResourceCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceCategory):
        """
        Dynamic initializer for ResourceCategory.
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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.resources.ResourceCategory.getName()"""
        return str.__wrap(super(ResourceCategory, self).getName())

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
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourceCategory.mapEntries()"""
        return 'Map'.__wrap(super(ResourceCategory, self).mapEntries())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def resources(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourceCategory.resources()"""
        return 'List'.__wrap(super(ResourceCategory, self).resources())

    @overload
    def resourceCount(self) -> int:
        """public int dev.ultreon.quantum.resources.ResourceCategory.resourceCount()"""
        return int.__wrap(super(ResourceCategory, self).resourceCount())

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
    def get(self, arg0: 'Identifier') -> 'StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.ResourceCategory.get(dev.ultreon.quantum.util.Identifier)"""
        return 'StaticResource'.__wrap(super(__ResourceCategory, self).get(arg0))

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourceCategory.has(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__ResourceCategory, self).has(arg0))

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
    def forEach(self, arg0: 'BiConsumer'):
        """public void dev.ultreon.quantum.resources.ResourceCategory.forEach(java.util.function.BiConsumer<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource>)"""
        super(__ResourceCategory, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.resources.ResourceCategory(java.lang.String)"""
        val = __ResourceCategory(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourceCategory.entries()"""
        return 'Set'.__wrap(super(ResourceCategory, self).entries()) 
 
 
# CLASS: dev.ultreon.quantum.resources.DynamicResource$Loader
from abc import abstractmethod, ABC
import dev.ultreon.quantum.resources.DynamicResource as __DynamicResource_Loader
__Loader = __DynamicResource_Loader.Loader
 
class Loader(ABC):
    """dev.ultreon.quantum.resources.DynamicResource.Loader"""
 
    @staticmethod
    def __wrap(java_value: __Loader) -> 'Loader':
        return Loader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Loader):
        """
        Dynamic initializer for Loader.
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
    def get(self, ):
        """public abstract byte[] dev.ultreon.quantum.resources.DynamicResource$Loader.get()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.resources.ResourceManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.io.InputStream as __InputStream
__InputStream = __InputStream
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ResourceManager(__Closeable, Closeable):
    """dev.ultreon.quantum.resources.ResourceManager"""
 
    @staticmethod
    def __wrap(java_value: __ResourceManager) -> 'ResourceManager':
        return ResourceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceManager):
        """
        Dynamic initializer for ResourceManager.
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
    def reload(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.reload()"""
        super(ResourceManager, self).reload()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.resources.ResourceManager(java.lang.String)"""
        val = __ResourceManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAllDataByPath(self, arg0: str) -> 'List':
        """public java.util.List<byte[]> dev.ultreon.quantum.resources.ResourceManager.getAllDataByPath(java.lang.String)"""
        return 'List'.__wrap(super(__ResourceManager, self).getAllDataByPath(arg0))

    @overload
    def getResourceCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourceManager.getResourceCategories()"""
        return 'List'.__wrap(super(ResourceManager, self).getResourceCategories())

    @overload
    def importDeferredPackage(self, arg0: 'Class'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importDeferredPackage(java.lang.Class<?>)"""
        super(__ResourceManager, self).importDeferredPackage(arg0)

    @overload
    def importPackage(self, arg0: 'File'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.io.File) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def importPackage(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.nio.file.Path) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

    @overload
    def getAllDataById(self, arg0: 'Identifier') -> 'List':
        """public java.util.List<byte[]> dev.ultreon.quantum.resources.ResourceManager.getAllDataById(dev.ultreon.quantum.util.Identifier)"""
        return 'List'.__wrap(super(__ResourceManager, self).getAllDataById(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getResourceCategory(self, arg0: str) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourceManager.getResourceCategory(java.lang.String)"""
        return 'List'.__wrap(super(__ResourceManager, self).getResourceCategory(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getRoot(self) -> str:
        """public java.lang.String dev.ultreon.quantum.resources.ResourceManager.getRoot()"""
        return str.__wrap(super(ResourceManager, self).getRoot())

    @overload
    def openResourceStream(self, arg0: 'Identifier') -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.resources.ResourceManager.openResourceStream(dev.ultreon.quantum.util.Identifier) throws java.io.IOException"""
        return 'InputStream'.__wrap(super(__ResourceManager, self).openResourceStream(arg0))

    @overload
    def importPackage(self, arg0: 'URI'):
        """public void dev.ultreon.quantum.resources.ResourceManager.importPackage(java.net.URI) throws java.io.IOException"""
        super(__ResourceManager, self).importPackage(arg0)

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
    def getResourcePackages(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourcePackage> dev.ultreon.quantum.resources.ResourceManager.getResourcePackages()"""
        return 'List'.__wrap(super(ResourceManager, self).getResourcePackages())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.close()"""
        super(ResourceManager, self).close()

    @overload
    def getResource(self, arg0: 'Identifier') -> 'Resource':
        """public dev.ultreon.quantum.resources.Resource dev.ultreon.quantum.resources.ResourceManager.getResource(dev.ultreon.quantum.util.Identifier)"""
        return 'Resource'.__wrap(super(__ResourceManager, self).getResource(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def importModResources(self):
        """public void dev.ultreon.quantum.resources.ResourceManager.importModResources()"""
        super(ResourceManager, self).importModResources()

    @overload
    def canScanFiles(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourceManager.canScanFiles()"""
        return bool.__wrap(super(ResourceManager, self).canScanFiles()) 
 
 
# CLASS: dev.ultreon.quantum.resources.ResourcePackage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.resources.ResourceCategory as __ResourceCategory
__ResourceCategory = __ResourceCategory
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.resources.StaticResource as __StaticResource
__StaticResource = __StaticResource
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.resources.ResourcePackage as __ResourcePackage
__ResourcePackage = __ResourcePackage
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ResourcePackage(__Closeable, Closeable):
    """dev.ultreon.quantum.resources.ResourcePackage"""
 
    @staticmethod
    def __wrap(java_value: __ResourcePackage) -> 'ResourcePackage':
        return ResourcePackage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourcePackage):
        """
        Dynamic initializer for ResourcePackage.
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
    def entries(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.resources.ResourcePackage.entries()"""
        return 'Set'.__wrap(super(ResourcePackage, self).entries())

    @overload
    def get(self, arg0: 'Identifier') -> 'StaticResource':
        """public dev.ultreon.quantum.resources.StaticResource dev.ultreon.quantum.resources.ResourcePackage.get(dev.ultreon.quantum.util.Identifier)"""
        return 'StaticResource'.__wrap(super(__ResourcePackage, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def has(self, arg0: 'Identifier') -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.has(dev.ultreon.quantum.util.Identifier)"""
        return bool.__wrap(super(__ResourcePackage, self).has(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'Map'):
        """public dev.ultreon.quantum.resources.ResourcePackage(java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource>,java.util.Map<java.lang.String, dev.ultreon.quantum.resources.ResourceCategory>)"""
        val = __ResourcePackage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def hasCategory(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.resources.ResourcePackage.hasCategory(java.lang.String)"""
        return bool.__wrap(super(__ResourcePackage, self).hasCategory(arg0))

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
    def __init__(self):
        """public dev.ultreon.quantum.resources.ResourcePackage()"""
        val = __ResourcePackage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.resources.ResourcePackage()"""
        val = __ResourcePackage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getCategory(self, arg0: str) -> 'ResourceCategory':
        """public dev.ultreon.quantum.resources.ResourceCategory dev.ultreon.quantum.resources.ResourcePackage.getCategory(java.lang.String)"""
        return 'ResourceCategory'.__wrap(super(__ResourcePackage, self).getCategory(arg0))

    @overload
    def mapEntries(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.resources.StaticResource> dev.ultreon.quantum.resources.ResourcePackage.mapEntries()"""
        return 'Map'.__wrap(super(ResourcePackage, self).mapEntries())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.resources.ResourcePackage.close()"""
        super(ResourcePackage, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.resources.ResourceCategory> dev.ultreon.quantum.resources.ResourcePackage.getCategories()"""
        return 'List'.__wrap(super(ResourcePackage, self).getCategories()) 
 
 
# CLASS: dev.ultreon.quantum.resources.StaticResource
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pycorelibs.functions.v0 import misc
except ImportError:
    misc = __import_once__("pycorelibs.functions.v0.misc")

import dev.ultreon.quantum.resources.StaticResource as __StaticResource
__StaticResource = __StaticResource
import java.io.ByteArrayInputStream as __ByteArrayInputStream
__ByteArrayInputStream = __ByteArrayInputStream
import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import java.lang.Class as __Class
__Class = __Class
import java.io.ByteArrayInputStream as ByteArrayInputStream
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import de.marhali.json5.Json5Element as Json5Element
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import de.marhali.json5.Json5Element as __Json5Element
__Json5Element = __Json5Element
from builtins import int
 
class StaticResource(__Resource, Resource, __Closeable, Closeable):
    """dev.ultreon.quantum.resources.StaticResource"""
 
    @staticmethod
    def __wrap(java_value: __StaticResource) -> 'StaticResource':
        return StaticResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StaticResource):
        """
        Dynamic initializer for StaticResource.
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
    def close(self):
        """public void dev.ultreon.quantum.resources.StaticResource.close()"""
        super(StaticResource, self).close()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.resources.StaticResource.id()"""
        return 'util.Identifier'.__wrap(super(StaticResource, self).id())

    @override
    @overload
    def isLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.resources.StaticResource.isLoaded()"""
        return bool.__wrap(super(StaticResource, self).isLoaded())

    @override
    @overload
    def getData(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.resources.StaticResource.getData()"""
        return List[int].__wrap(super(StaticResource, self).getData())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadJson(self, arg0: 'Class') -> object:
        """public default <T> T dev.ultreon.quantum.resources.Resource.loadJson(java.lang.Class<T>)"""
        return object.__wrap(super(__Resource, self).loadJson(arg0))

    @overload
    def __init__(self, arg0: 'Identifier', arg1: 'ThrowingSupplier'):
        """public dev.ultreon.quantum.resources.StaticResource(dev.ultreon.quantum.util.Identifier,dev.ultreon.libs.functions.v0.misc.ThrowingSupplier<java.io.InputStream, java.io.IOException>)"""
        val = __StaticResource(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadOrOpenStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.resources.StaticResource.loadOrOpenStream()"""
        return 'InputStream'.__wrap(super(StaticResource, self).loadOrOpenStream())

    @override
    @overload
    def openStream(self) -> 'ByteArrayInputStream':
        """public java.io.ByteArrayInputStream dev.ultreon.quantum.resources.StaticResource.openStream()"""
        return 'ByteArrayInputStream'.__wrap(super(StaticResource, self).openStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isNotLoaded(self) -> bool:
        """public default boolean dev.ultreon.quantum.resources.Resource.isNotLoaded()"""
        return bool.__wrap(super(Resource, self).isNotLoaded())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def loadJson5(self) -> 'Json5Element':
        """public default de.marhali.json5.Json5Element dev.ultreon.quantum.resources.Resource.loadJson5()"""
        return 'Json5Element'.__wrap(super(Resource, self).loadJson5())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def loadOrGet(self) -> List[int]:
        """public default byte[] dev.ultreon.quantum.resources.Resource.loadOrGet()"""
        return List[int].__wrap(super(Resource, self).loadOrGet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readJson5(self) -> 'Json5Element':
        """public de.marhali.json5.Json5Element dev.ultreon.quantum.resources.StaticResource.readJson5()"""
        return 'Json5Element'.__wrap(super(StaticResource, self).readJson5())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def openReader(self) -> 'Reader':
        """public default java.io.Reader dev.ultreon.quantum.resources.Resource.openReader() throws java.io.IOException"""
        return 'Reader'.__wrap(super(Resource, self).openReader())