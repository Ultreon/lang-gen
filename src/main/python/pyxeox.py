from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.registry.Registry as __Registry_Builder
__Builder = __Registry_Builder.Builder
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import dev.ultreon.xeox.loader.JSRegistries as __JSRegistries
__JSRegistries = __JSRegistries
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JSRegistries():
    """dev.ultreon.xeox.loader.JSRegistries"""
 
    @staticmethod
    def __wrap(java_value: __JSRegistries) -> 'JSRegistries':
        return JSRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JSRegistries):
        """
        Dynamic initializer for JSRegistries.
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
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = __JSRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def registry(self, arg0: 'Identifier') -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry'.__wrap(super(__JSRegistries, self).registry(arg0))

    @overload
    def createBuilder(self, arg0: 'Identifier') -> 'registry.Registry$Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<?> dev.ultreon.xeox.loader.JSRegistries.createBuilder(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry$Builder'.__wrap(super(__JSRegistries, self).createBuilder(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def id(self, arg0: str, arg1: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String,java.lang.String)"""
        return 'util.Identifier'.__wrap(super(__JSRegistries, self).id(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def registry(self, arg0: str) -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(java.lang.String)"""
        return 'registry.Registry'.__wrap(super(__JSRegistries, self).registry(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = __JSRegistries()
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
    def id(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String)"""
        return 'util.Identifier'.__wrap(super(__JSRegistries, self).id(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.xeox.loader.JSRegistries
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.registry.Registry as __Registry_Builder
__Builder = __Registry_Builder.Builder
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

import dev.ultreon.xeox.loader.JSRegistries as __JSRegistries
__JSRegistries = __JSRegistries
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.registry.Registry as __Registry
__Registry = __Registry
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JSRegistries():
    """dev.ultreon.xeox.loader.JSRegistries"""
 
    @staticmethod
    def __wrap(java_value: __JSRegistries) -> 'JSRegistries':
        return JSRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JSRegistries):
        """
        Dynamic initializer for JSRegistries.
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
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = __JSRegistries()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def registry(self, arg0: 'Identifier') -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry'.__wrap(super(__JSRegistries, self).registry(arg0))

    @overload
    def createBuilder(self, arg0: 'Identifier') -> 'registry.Registry$Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<?> dev.ultreon.xeox.loader.JSRegistries.createBuilder(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry$Builder'.__wrap(super(__JSRegistries, self).createBuilder(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def id(self, arg0: str, arg1: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String,java.lang.String)"""
        return 'util.Identifier'.__wrap(super(__JSRegistries, self).id(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def registry(self, arg0: str) -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(java.lang.String)"""
        return 'registry.Registry'.__wrap(super(__JSRegistries, self).registry(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = __JSRegistries()
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
    def id(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String)"""
        return 'util.Identifier'.__wrap(super(__JSRegistries, self).id(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.xeox.loader.JSRegistries 
 
 
# CLASS: dev.ultreon.xeox.loader.JSEvents
from builtins import str
import org.mozilla.javascript.Context as Context
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.xeox.loader.JSEvents as __JSEvents
__JSEvents = __JSEvents
from builtins import object
import org.mozilla.javascript.Scriptable as Scriptable
import org.mozilla.javascript.Function as Function
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
 
class JSEvents():
    """dev.ultreon.xeox.loader.JSEvents"""
 
    @staticmethod
    def __wrap(java_value: __JSEvents) -> 'JSEvents':
        return JSEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JSEvents):
        """
        Dynamic initializer for JSEvents.
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
    def emitAll(arg0: str, *arg1: object):
        """public static void dev.ultreon.xeox.loader.JSEvents.emitAll(java.lang.String,java.lang.Object...)"""
        __JSEvents.emitAll(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'Scriptable', arg1: 'Context'):
        """public dev.ultreon.xeox.loader.JSEvents(org.mozilla.javascript.Scriptable,org.mozilla.javascript.Context)"""
        val = __JSEvents(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def register(arg0: str):
        """public static void dev.ultreon.xeox.loader.JSEvents.register(java.lang.String)"""
        __JSEvents.register(arg0)

    @overload
    def on(self, arg0: str, arg1: 'Function'):
        """public void dev.ultreon.xeox.loader.JSEvents.on(java.lang.String,org.mozilla.javascript.Function)"""
        super(__JSEvents, self).on(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def emit(self, arg0: str, *arg1: object):
        """public void dev.ultreon.xeox.loader.JSEvents.emit(java.lang.String,java.lang.Object...)"""
        super(__JSEvents, self).emit(arg0, arg1)

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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$InitBindings
import dev.ultreon.xeox.loader.XeoxEvents as __XeoxEvents_InitBindings
__InitBindings = __XeoxEvents_InitBindings.InitBindings
import org.mozilla.javascript.ScriptableObject as ScriptableObject
from abc import abstractmethod, ABC
 
class InitBindings(ABC):
    """dev.ultreon.xeox.loader.XeoxEvents.InitBindings"""
 
    @staticmethod
    def __wrap(java_value: __InitBindings) -> 'InitBindings':
        return InitBindings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InitBindings):
        """
        Dynamic initializer for InitBindings.
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
    def onInitBindings(self, arg0: 'ScriptableObject'):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$InitBindings.onInitBindings(org.mozilla.javascript.ScriptableObject)"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$EventRegistration
import dev.ultreon.xeox.loader.XeoxEvents as __XeoxEvents_EventRegistration
__EventRegistration = __XeoxEvents_EventRegistration.EventRegistration
from abc import abstractmethod, ABC
 
class EventRegistration(ABC):
    """dev.ultreon.xeox.loader.XeoxEvents.EventRegistration"""
 
    @staticmethod
    def __wrap(java_value: __EventRegistration) -> 'EventRegistration':
        return EventRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventRegistration):
        """
        Dynamic initializer for EventRegistration.
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
    def onRegister(self, ):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$EventRegistration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxLoader
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.xeox.loader.XeoxLoader as __XeoxLoader
__XeoxLoader = __XeoxLoader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
from builtins import type
import java.io.File as File
import java.util.Optional as __Optional
__Optional = __Optional
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class XeoxLoader():
    """dev.ultreon.xeox.loader.XeoxLoader"""
 
    @staticmethod
    def __wrap(java_value: __XeoxLoader) -> 'XeoxLoader':
        return XeoxLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XeoxLoader):
        """
        Dynamic initializer for XeoxLoader.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.xeox.loader.XeoxLoader.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


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
    def constructMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.constructMods()"""
        super(XeoxLoader, self).constructMods()

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.xeox.loader.XeoxLoader.isModLoaded(java.lang.String)"""
        return bool.__wrap(super(__XeoxLoader, self).isModLoaded(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get() -> 'XeoxLoader':
        """public static dev.ultreon.xeox.loader.XeoxLoader dev.ultreon.xeox.loader.XeoxLoader.get()"""
        return XeoxLoader.__wrap(__XeoxLoader.get())

    @overload
    def initMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.initMods()"""
        super(XeoxLoader, self).initMods()

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
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.xeox.loader.XeoxLoader.getMod(java.lang.String)"""
        return 'Optional'.__wrap(super(__XeoxLoader, self).getMod(arg0))

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
    def getRhinoExceptions(self) -> 'List':
        """public java.util.List<org.mozilla.javascript.RhinoException> dev.ultreon.xeox.loader.XeoxLoader.getRhinoExceptions()"""
        return 'List'.__wrap(super(XeoxLoader, self).getRhinoExceptions())

    @overload
    def getMods(self) -> 'List':
        """public java.util.List<dev.ultreon.xeox.loader.XeoxMod> dev.ultreon.xeox.loader.XeoxLoader.getMods()"""
        return 'List'.__wrap(super(XeoxLoader, self).getMods())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getErrors(self) -> 'List':
        """public java.util.List<dev.ultreon.xeox.loader.ModImportException> dev.ultreon.xeox.loader.XeoxLoader.getErrors()"""
        return 'List'.__wrap(super(XeoxLoader, self).getErrors())

    @overload
    def importMod(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.xeox.loader.XeoxLoader.importMod(java.io.File)"""
        return 'util.Result'.__wrap(super(__XeoxLoader, self).importMod(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def loadMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.loadMods()"""
        super(XeoxLoader, self).loadMods() 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxModFile
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import dev.ultreon.xeox.loader.XeoxMod as __XeoxMod
__XeoxMod = __XeoxMod
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.xeox.loader.XeoxMetadata as __XeoxMetadata
__XeoxMetadata = __XeoxMetadata
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.xeox.loader.XeoxModFile as __XeoxModFile
__XeoxModFile = __XeoxModFile
from builtins import int
 
class XeoxModFile():
    """dev.ultreon.xeox.loader.XeoxModFile"""
 
    @staticmethod
    def __wrap(java_value: __XeoxModFile) -> 'XeoxModFile':
        return XeoxModFile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XeoxModFile):
        """
        Dynamic initializer for XeoxModFile.
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

    @staticmethod
    @overload
    def importFile(arg0: 'File') -> 'XeoxModFile':
        """public static dev.ultreon.xeox.loader.XeoxModFile dev.ultreon.xeox.loader.XeoxModFile.importFile(java.io.File) throws java.io.IOException"""
        return XeoxModFile.__wrap(__XeoxModFile.importFile(arg0))

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
    def getFile(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.xeox.loader.XeoxModFile.getFile()"""
        return 'files.FileHandle'.__wrap(super(XeoxModFile, self).getFile())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public dev.ultreon.xeox.loader.XeoxModFile(com.badlogic.gdx.files.FileHandle)"""
        val = __XeoxModFile(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getMetadata(self) -> 'XeoxMetadata':
        """public dev.ultreon.xeox.loader.XeoxMetadata dev.ultreon.xeox.loader.XeoxModFile.getMetadata()"""
        return 'XeoxMetadata'.__wrap(super(XeoxModFile, self).getMetadata())

    @overload
    def constructMod(self) -> 'XeoxMod':
        """public dev.ultreon.xeox.loader.XeoxMod dev.ultreon.xeox.loader.XeoxModFile.constructMod()"""
        return 'XeoxMod'.__wrap(super(XeoxModFile, self).constructMod())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.xeox.loader.XeoxEvents as __XeoxEvents
__XeoxEvents = __XeoxEvents
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class XeoxEvents():
    """dev.ultreon.xeox.loader.XeoxEvents"""
 
    @staticmethod
    def __wrap(java_value: __XeoxEvents) -> 'XeoxEvents':
        return XeoxEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XeoxEvents):
        """
        Dynamic initializer for XeoxEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$EventError> dev.ultreon.xeox.loader.XeoxEvents.EVENT_ERROR
    EVENT_ERROR: 'api.Event' = __wrap(__api.Event.EVENT_ERROR)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$InitBindings> dev.ultreon.xeox.loader.XeoxEvents.INIT_BINDINGS
    INIT_BINDINGS: 'api.Event' = __wrap(__api.Event.INIT_BINDINGS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$EventRegistration> dev.ultreon.xeox.loader.XeoxEvents.EVENT_REGISTRATION
    EVENT_REGISTRATION: 'api.Event' = __wrap(__api.Event.EVENT_REGISTRATION)


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
    def __init__(self):
        """public dev.ultreon.xeox.loader.XeoxEvents()"""
        val = __XeoxEvents()
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
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.XeoxEvents()"""
        val = __XeoxEvents()
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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxMetadata
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.xeox.loader.XeoxMetadata as __XeoxMetadata
__XeoxMetadata = __XeoxMetadata
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.ModOrigin as __ModOrigin
__ModOrigin = __ModOrigin
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class XeoxMetadata():
    """dev.ultreon.xeox.loader.XeoxMetadata"""
 
    @staticmethod
    def __wrap(java_value: __XeoxMetadata) -> 'XeoxMetadata':
        return XeoxMetadata(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XeoxMetadata):
        """
        Dynamic initializer for XeoxMetadata.
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
    def authors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.xeox.loader.XeoxMetadata.authors()"""
        return 'Collection'.__wrap(super(XeoxMetadata, self).authors())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def description(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.description()"""
        return str.__wrap(super(XeoxMetadata, self).description())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.xeox.loader.XeoxMetadata.hashCode()"""
        return int.__wrap(super(XeoxMetadata, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: 'Collection'):
        """public dev.ultreon.xeox.loader.XeoxMetadata(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        val = __XeoxMetadata(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.toString()"""
        return str.__wrap(super(XeoxMetadata, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.id()"""
        return str.__wrap(super(XeoxMetadata, self).id())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.xeox.loader.XeoxMetadata.equals(java.lang.Object)"""
        return bool.__wrap(super(__XeoxMetadata, self).equals(arg0))

    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.xeox.loader.XeoxMetadata.getOrigin()"""
        return 'pyquantum.ModOrigin'.__wrap(super(XeoxMetadata, self).getOrigin())

    @overload
    def version(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.version()"""
        return str.__wrap(super(XeoxMetadata, self).version())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.name()"""
        return str.__wrap(super(XeoxMetadata, self).name()) 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$EventError
import dev.ultreon.xeox.loader.XeoxEvents as __XeoxEvents_EventError
__EventError = __XeoxEvents_EventError.EventError
import org.mozilla.javascript.RhinoException as RhinoException
from abc import abstractmethod, ABC
 
class EventError(ABC):
    """dev.ultreon.xeox.loader.XeoxEvents.EventError"""
 
    @staticmethod
    def __wrap(java_value: __EventError) -> 'EventError':
        return EventError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventError):
        """
        Dynamic initializer for EventError.
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
    def onError(self, arg0: 'RhinoException'):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$EventError.onError(org.mozilla.javascript.RhinoException)"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.JSLibGDX
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.xeox.loader.JSLibGDX as __JSLibGDX
__JSLibGDX = __JSLibGDX
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JSLibGDX():
    """dev.ultreon.xeox.loader.JSLibGDX"""
 
    @staticmethod
    def __wrap(java_value: __JSLibGDX) -> 'JSLibGDX':
        return JSLibGDX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JSLibGDX):
        """
        Dynamic initializer for JSLibGDX.
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
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSLibGDX()"""
        val = __JSLibGDX()
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
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.JSLibGDX()"""
        val = __JSLibGDX()
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
 
 
# CLASS: dev.ultreon.xeox.loader.ModImportException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.xeox.loader.ModImportException as __ModImportException
__ModImportException = __ModImportException
from builtins import int
 
class ModImportException():
    """dev.ultreon.xeox.loader.ModImportException"""
 
    @staticmethod
    def __wrap(java_value: __ModImportException) -> 'ModImportException':
        return ModImportException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModImportException):
        """
        Dynamic initializer for ModImportException.
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.String,java.lang.Throwable)"""
        val = __ModImportException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.ModImportException()"""
        val = __ModImportException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.String)"""
        val = __ModImportException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.Throwable)"""
        val = __ModImportException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.ModImportException()"""
        val = __ModImportException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.xeox.loader.JSModInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.xeox.loader.JSModInfo as __JSModInfo
__JSModInfo = __JSModInfo
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JSModInfo():
    """dev.ultreon.xeox.loader.JSModInfo"""
 
    @staticmethod
    def __wrap(java_value: __JSModInfo) -> 'JSModInfo':
        return JSModInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JSModInfo):
        """
        Dynamic initializer for JSModInfo.
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
    def makeId(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSModInfo.makeId(java.lang.String)"""
        return 'util.Identifier'.__wrap(super(__JSModInfo, self).makeId(arg0))

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
    def __init__(self, arg0: 'XeoxMod'):
        """public dev.ultreon.xeox.loader.JSModInfo(dev.ultreon.xeox.loader.XeoxMod)"""
        val = __JSModInfo(arg0)
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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxMod
from pyquantum_helper import import_once as __import_once__
import org.mozilla.javascript.Context as Context
import org.mozilla.javascript.ScriptableObject as ScriptableObject
from builtins import type
import java.util.Collection as Collection
import dev.ultreon.xeox.loader.XeoxMod as __XeoxMod
__XeoxMod = __XeoxMod
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.xeox.loader.XeoxMetadata as __XeoxMetadata
__XeoxMetadata = __XeoxMetadata
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Optional as __Optional
__Optional = __Optional
import org.mozilla.javascript.ScriptableObject as __ScriptableObject
__ScriptableObject = __ScriptableObject
import java.lang.Iterable as Iterable
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from builtins import object
import org.mozilla.javascript.Scriptable as Scriptable
import org.mozilla.javascript.Function as Function
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.ModOrigin as __ModOrigin
__ModOrigin = __ModOrigin
import java.lang.Integer as __int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class XeoxMod():
    """dev.ultreon.xeox.loader.XeoxMod"""
 
    @staticmethod
    def __wrap(java_value: __XeoxMod) -> 'XeoxMod':
        return XeoxMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __XeoxMod):
        """
        Dynamic initializer for XeoxMod.
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
    def __init__(self, arg0: 'XeoxMetadata', arg1: str):
        """public dev.ultreon.xeox.loader.XeoxMod(dev.ultreon.xeox.loader.XeoxMetadata,java.lang.String)"""
        val = __XeoxMod(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getId()"""
        return str.__wrap(super(XeoxMod, self).getId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getPath()"""
        return str.__wrap(super(XeoxMod, self).getPath())

    @overload
    def getMetadata(self) -> 'XeoxMetadata':
        """public dev.ultreon.xeox.loader.XeoxMetadata dev.ultreon.xeox.loader.XeoxMod.getMetadata()"""
        return 'XeoxMetadata'.__wrap(super(XeoxMod, self).getMetadata())

    @override
    @overload
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getVersion()"""
        return str.__wrap(super(XeoxMod, self).getVersion())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def importScript(arg0: 'Context', arg1: 'Scriptable', arg2: 'Object', arg3: 'Function') -> 'ScriptableObject':
        """public static org.mozilla.javascript.ScriptableObject dev.ultreon.xeox.loader.XeoxMod.importScript(org.mozilla.javascript.Context,org.mozilla.javascript.Scriptable,java.lang.Object[],org.mozilla.javascript.Function) throws java.io.IOException"""
        return ScriptableObject.__wrap(__XeoxMod.importScript(arg0, arg1, arg2, arg3))

    @overload
    def init(self):
        """public void dev.ultreon.xeox.loader.XeoxMod.init() throws java.io.IOException"""
        super(XeoxMod, self).init()

    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.xeox.loader.XeoxMod.getIconPath(int)"""
        return 'Optional'.__wrap(super(__XeoxMod, self).getIconPath(__int.valueOf(arg0)))

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.xeox.loader.XeoxMod.getOrigin()"""
        return 'pyquantum.ModOrigin'.__wrap(super(XeoxMod, self).getOrigin())

    @overload
    def disable(self):
        """public void dev.ultreon.xeox.loader.XeoxMod.disable()"""
        super(XeoxMod, self).disable()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getDescription()"""
        return str.__wrap(super(XeoxMod, self).getDescription())

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getName()"""
        return str.__wrap(super(XeoxMod, self).getName())

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.xeox.loader.XeoxMod.getRootPaths()"""
        return 'Iterable'.__wrap(super(XeoxMod, self).getRootPaths())

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

        @staticmethod
        @overload
        def dispose():
            """public static void dev.ultreon.xeox.loader.XeoxMod.dispose()"""
            __XeoxMod.dispose()

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.xeox.loader.XeoxMod.getAuthors()"""
        return 'Collection'.__wrap(super(XeoxMod, self).getAuthors())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))