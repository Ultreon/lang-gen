from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
import dev.ultreon.quantum.registry.Registry as _Registry_Builder
_Builder = _Registry_Builder.Builder
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.xeox.loader.JSRegistries as _JSRegistries
_JSRegistries = _JSRegistries
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JSRegistries():
    """dev.ultreon.xeox.loader.JSRegistries"""
 
    @staticmethod
    def _wrap(java_value: _JSRegistries) -> 'JSRegistries':
        return JSRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JSRegistries):
        """
        Dynamic initializer for JSRegistries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JSRegistries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JSRegistries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = _JSRegistries()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = _JSRegistries()
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
    def createBuilder(self, arg0: 'Identifier') -> 'registry.Registry$Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<?> dev.ultreon.xeox.loader.JSRegistries.createBuilder(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry$Builder'._wrap(super(_JSRegistries, self).createBuilder(arg0))

    @overload
    def registry(self, arg0: 'Identifier') -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry'._wrap(super(_JSRegistries, self).registry(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def id(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String)"""
        return 'util.Identifier'._wrap(super(_JSRegistries, self).id(arg0))

    @overload
    def registry(self, arg0: str) -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(java.lang.String)"""
        return 'registry.Registry'._wrap(super(_JSRegistries, self).registry(arg0))

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
    def id(self, arg0: str, arg1: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String,java.lang.String)"""
        return 'util.Identifier'._wrap(super(_JSRegistries, self).id(arg0, arg1))

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

 
 
 
# CLASS: dev.ultreon.xeox.loader.JSRegistries
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.registry.Registry as _Registry
_Registry = _Registry
import dev.ultreon.quantum.registry.Registry as _Registry_Builder
_Builder = _Registry_Builder.Builder
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.xeox.loader.JSRegistries as _JSRegistries
_JSRegistries = _JSRegistries
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JSRegistries():
    """dev.ultreon.xeox.loader.JSRegistries"""
 
    @staticmethod
    def _wrap(java_value: _JSRegistries) -> 'JSRegistries':
        return JSRegistries(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JSRegistries):
        """
        Dynamic initializer for JSRegistries.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JSRegistries__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JSRegistries__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = _JSRegistries()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.JSRegistries()"""
        val = _JSRegistries()
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
    def createBuilder(self, arg0: 'Identifier') -> 'registry.Registry$Builder':
        """public dev.ultreon.quantum.registry.Registry$Builder<?> dev.ultreon.xeox.loader.JSRegistries.createBuilder(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry$Builder'._wrap(super(_JSRegistries, self).createBuilder(arg0))

    @overload
    def registry(self, arg0: 'Identifier') -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(dev.ultreon.quantum.util.Identifier)"""
        return 'registry.Registry'._wrap(super(_JSRegistries, self).registry(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def id(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String)"""
        return 'util.Identifier'._wrap(super(_JSRegistries, self).id(arg0))

    @overload
    def registry(self, arg0: str) -> 'registry.Registry':
        """public dev.ultreon.quantum.registry.Registry<?> dev.ultreon.xeox.loader.JSRegistries.registry(java.lang.String)"""
        return 'registry.Registry'._wrap(super(_JSRegistries, self).registry(arg0))

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
    def id(self, arg0: str, arg1: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSRegistries.id(java.lang.String,java.lang.String)"""
        return 'util.Identifier'._wrap(super(_JSRegistries, self).id(arg0, arg1))

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

 
 
 
# CLASS: dev.ultreon.xeox.loader.JSRegistries 
 
 
# CLASS: dev.ultreon.xeox.loader.JSEvents
from builtins import str
import org.mozilla.javascript.Context as Context
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.mozilla.javascript.Scriptable as Scriptable
import java.lang.String as _string
import org.mozilla.javascript.Function as Function
import java.lang.Integer as _int
import dev.ultreon.xeox.loader.JSEvents as _JSEvents
_JSEvents = _JSEvents
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JSEvents():
    """dev.ultreon.xeox.loader.JSEvents"""
 
    @staticmethod
    def _wrap(java_value: _JSEvents) -> 'JSEvents':
        return JSEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JSEvents):
        """
        Dynamic initializer for JSEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JSEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JSEvents__wrapper":
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

    @staticmethod
    @overload
    def emitAll(arg0: str, *arg1: object):
        """public static void dev.ultreon.xeox.loader.JSEvents.emitAll(java.lang.String,java.lang.Object...)"""
        _JSEvents.emitAll(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def on(self, arg0: str, arg1: 'Function'):
        """public void dev.ultreon.xeox.loader.JSEvents.on(java.lang.String,org.mozilla.javascript.Function)"""
        super(_JSEvents, self).on(arg0, arg1)

    @staticmethod
    @overload
    def register(arg0: str):
        """public static void dev.ultreon.xeox.loader.JSEvents.register(java.lang.String)"""
        _JSEvents.register(arg0)

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
    def emit(self, arg0: str, *arg1: object):
        """public void dev.ultreon.xeox.loader.JSEvents.emit(java.lang.String,java.lang.Object...)"""
        super(_JSEvents, self).emit(arg0, arg1)

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
    def __init__(self, arg0: 'Scriptable', arg1: 'Context'):
        """public dev.ultreon.xeox.loader.JSEvents(org.mozilla.javascript.Scriptable,org.mozilla.javascript.Context)"""
        val = _JSEvents(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$InitBindings
import org.mozilla.javascript.ScriptableObject as ScriptableObject
import dev.ultreon.xeox.loader.XeoxEvents as _XeoxEvents_InitBindings
_InitBindings = _XeoxEvents_InitBindings.InitBindings
from abc import abstractmethod, ABC
 
class InitBindings():
    """dev.ultreon.xeox.loader.XeoxEvents.InitBindings"""
 
    @staticmethod
    def _wrap(java_value: _InitBindings) -> 'InitBindings':
        return InitBindings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InitBindings):
        """
        Dynamic initializer for InitBindings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InitBindings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InitBindings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onInitBindings(self, arg0: 'ScriptableObject'):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$InitBindings.onInitBindings(org.mozilla.javascript.ScriptableObject)"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$EventRegistration
import dev.ultreon.xeox.loader.XeoxEvents as _XeoxEvents_EventRegistration
_EventRegistration = _XeoxEvents_EventRegistration.EventRegistration
from abc import abstractmethod, ABC
 
class EventRegistration():
    """dev.ultreon.xeox.loader.XeoxEvents.EventRegistration"""
 
    @staticmethod
    def _wrap(java_value: _EventRegistration) -> 'EventRegistration':
        return EventRegistration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventRegistration):
        """
        Dynamic initializer for EventRegistration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventRegistration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventRegistration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegister(self, ):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$EventRegistration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.xeox.loader.XeoxLoader as _XeoxLoader
_XeoxLoader = _XeoxLoader
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class XeoxLoader():
    """dev.ultreon.xeox.loader.XeoxLoader"""
 
    @staticmethod
    def _wrap(java_value: _XeoxLoader) -> 'XeoxLoader':
        return XeoxLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _XeoxLoader):
        """
        Dynamic initializer for XeoxLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_XeoxLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_XeoxLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.xeox.loader.XeoxLoader.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @staticmethod
    @overload
    def get() -> 'XeoxLoader':
        """public static dev.ultreon.xeox.loader.XeoxLoader dev.ultreon.xeox.loader.XeoxLoader.get()"""
        return XeoxLoader._wrap(_XeoxLoader.get())

    @overload
    def getErrors(self) -> 'List':
        """public java.util.List<dev.ultreon.xeox.loader.ModImportException> dev.ultreon.xeox.loader.XeoxLoader.getErrors()"""
        return 'List'._wrap(super(XeoxLoader, self).getErrors())

    @overload
    def constructMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.constructMods()"""
        super(XeoxLoader, self).constructMods()

    @overload
    def isModLoaded(self, arg0: str) -> bool:
        """public boolean dev.ultreon.xeox.loader.XeoxLoader.isModLoaded(java.lang.String)"""
        return bool._wrap(super(_XeoxLoader, self).isModLoaded(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def importMod(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.xeox.loader.XeoxLoader.importMod(java.io.File)"""
        return 'util.Result'._wrap(super(_XeoxLoader, self).importMod(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def initMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.initMods()"""
        super(XeoxLoader, self).initMods()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getRhinoExceptions(self) -> 'List':
        """public java.util.List<org.mozilla.javascript.RhinoException> dev.ultreon.xeox.loader.XeoxLoader.getRhinoExceptions()"""
        return 'List'._wrap(super(XeoxLoader, self).getRhinoExceptions())

    @overload
    def getMods(self) -> 'List':
        """public java.util.List<dev.ultreon.xeox.loader.XeoxMod> dev.ultreon.xeox.loader.XeoxLoader.getMods()"""
        return 'List'._wrap(super(XeoxLoader, self).getMods())

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
    def getMod(self, arg0: str) -> 'Optional':
        """public java.util.Optional<dev.ultreon.quantum.Mod> dev.ultreon.xeox.loader.XeoxLoader.getMod(java.lang.String)"""
        return 'Optional'._wrap(super(_XeoxLoader, self).getMod(arg0))

    @overload
    def loadMods(self):
        """public void dev.ultreon.xeox.loader.XeoxLoader.loadMods()"""
        super(XeoxLoader, self).loadMods()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxModFile
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.xeox.loader.XeoxModFile as _XeoxModFile
_XeoxModFile = _XeoxModFile
import java.io.File as File
import dev.ultreon.xeox.loader.XeoxMod as _XeoxMod
_XeoxMod = _XeoxMod
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.Integer as _int
import dev.ultreon.xeox.loader.XeoxMetadata as _XeoxMetadata
_XeoxMetadata = _XeoxMetadata
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class XeoxModFile():
    """dev.ultreon.xeox.loader.XeoxModFile"""
 
    @staticmethod
    def _wrap(java_value: _XeoxModFile) -> 'XeoxModFile':
        return XeoxModFile(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _XeoxModFile):
        """
        Dynamic initializer for XeoxModFile.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_XeoxModFile__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_XeoxModFile__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMetadata(self) -> 'XeoxMetadata':
        """public dev.ultreon.xeox.loader.XeoxMetadata dev.ultreon.xeox.loader.XeoxModFile.getMetadata()"""
        return 'XeoxMetadata'._wrap(super(XeoxModFile, self).getMetadata())

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
    def constructMod(self) -> 'XeoxMod':
        """public dev.ultreon.xeox.loader.XeoxMod dev.ultreon.xeox.loader.XeoxModFile.constructMod()"""
        return 'XeoxMod'._wrap(super(XeoxModFile, self).constructMod())

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
    def __init__(self, arg0: 'FileHandle'):
        """public dev.ultreon.xeox.loader.XeoxModFile(com.badlogic.gdx.files.FileHandle)"""
        val = _XeoxModFile(arg0)
        self.__wrapper = val

    @overload
    def getFile(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle dev.ultreon.xeox.loader.XeoxModFile.getFile()"""
        return 'files.FileHandle'._wrap(super(XeoxModFile, self).getFile())

    @staticmethod
    @overload
    def importFile(arg0: 'File') -> 'XeoxModFile':
        """public static dev.ultreon.xeox.loader.XeoxModFile dev.ultreon.xeox.loader.XeoxModFile.importFile(java.io.File) throws java.io.IOException"""
        return XeoxModFile._wrap(_XeoxModFile.importFile(arg0))

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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.xeox.loader.XeoxEvents as _XeoxEvents
_XeoxEvents = _XeoxEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class XeoxEvents():
    """dev.ultreon.xeox.loader.XeoxEvents"""
 
    @staticmethod
    def _wrap(java_value: _XeoxEvents) -> 'XeoxEvents':
        return XeoxEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _XeoxEvents):
        """
        Dynamic initializer for XeoxEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_XeoxEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_XeoxEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$EventRegistration> dev.ultreon.xeox.loader.XeoxEvents.EVENT_REGISTRATION
    EVENT_REGISTRATION: 'api.Event' = _wrap(_api.Event.EVENT_REGISTRATION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$InitBindings> dev.ultreon.xeox.loader.XeoxEvents.INIT_BINDINGS
    INIT_BINDINGS: 'api.Event' = _wrap(_api.Event.INIT_BINDINGS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.xeox.loader.XeoxEvents$EventError> dev.ultreon.xeox.loader.XeoxEvents.EVENT_ERROR
    EVENT_ERROR: 'api.Event' = _wrap(_api.Event.EVENT_ERROR)


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
        """public dev.ultreon.xeox.loader.XeoxEvents()"""
        val = _XeoxEvents()
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
        """public dev.ultreon.xeox.loader.XeoxEvents()"""
        val = _XeoxEvents()
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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxMetadata
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.ModOrigin as _ModOrigin
_ModOrigin = _ModOrigin
import java.util.Collection as Collection
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.xeox.loader.XeoxMetadata as _XeoxMetadata
_XeoxMetadata = _XeoxMetadata
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class XeoxMetadata():
    """dev.ultreon.xeox.loader.XeoxMetadata"""
 
    @staticmethod
    def _wrap(java_value: _XeoxMetadata) -> 'XeoxMetadata':
        return XeoxMetadata(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _XeoxMetadata):
        """
        Dynamic initializer for XeoxMetadata.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_XeoxMetadata__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_XeoxMetadata__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.xeox.loader.XeoxMetadata.hashCode()"""
        return int._wrap(super(XeoxMetadata, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.toString()"""
        return str._wrap(super(XeoxMetadata, self).toString())

    @overload
    def authors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.xeox.loader.XeoxMetadata.authors()"""
        return 'Collection'._wrap(super(XeoxMetadata, self).authors())

    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.xeox.loader.XeoxMetadata.getOrigin()"""
        return 'pyquantum.ModOrigin'._wrap(super(XeoxMetadata, self).getOrigin())

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.name()"""
        return str._wrap(super(XeoxMetadata, self).name())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.id()"""
        return str._wrap(super(XeoxMetadata, self).id())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def version(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.version()"""
        return str._wrap(super(XeoxMetadata, self).version())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: 'Collection'):
        """public dev.ultreon.xeox.loader.XeoxMetadata(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        val = _XeoxMetadata(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.xeox.loader.XeoxMetadata.equals(java.lang.Object)"""
        return bool._wrap(super(_XeoxMetadata, self).equals(arg0))

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
    def description(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMetadata.description()"""
        return str._wrap(super(XeoxMetadata, self).description())

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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxEvents$EventError
import org.mozilla.javascript.RhinoException as RhinoException
from abc import abstractmethod, ABC
import dev.ultreon.xeox.loader.XeoxEvents as _XeoxEvents_EventError
_EventError = _XeoxEvents_EventError.EventError
 
class EventError():
    """dev.ultreon.xeox.loader.XeoxEvents.EventError"""
 
    @staticmethod
    def _wrap(java_value: _EventError) -> 'EventError':
        return EventError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventError):
        """
        Dynamic initializer for EventError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onError(self, arg0: 'RhinoException'):
        """public abstract void dev.ultreon.xeox.loader.XeoxEvents$EventError.onError(org.mozilla.javascript.RhinoException)"""
        pass 
 
 
# CLASS: dev.ultreon.xeox.loader.JSLibGDX
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
import dev.ultreon.xeox.loader.JSLibGDX as _JSLibGDX
_JSLibGDX = _JSLibGDX
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JSLibGDX():
    """dev.ultreon.xeox.loader.JSLibGDX"""
 
    @staticmethod
    def _wrap(java_value: _JSLibGDX) -> 'JSLibGDX':
        return JSLibGDX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JSLibGDX):
        """
        Dynamic initializer for JSLibGDX.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JSLibGDX__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JSLibGDX__wrapper":
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
    def __init__(self):
        """public dev.ultreon.xeox.loader.JSLibGDX()"""
        val = _JSLibGDX()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.JSLibGDX()"""
        val = _JSLibGDX()
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
 
 
# CLASS: dev.ultreon.xeox.loader.ModImportException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.xeox.loader.ModImportException as _ModImportException
_ModImportException = _ModImportException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModImportException():
    """dev.ultreon.xeox.loader.ModImportException"""
 
    @staticmethod
    def _wrap(java_value: _ModImportException) -> 'ModImportException':
        return ModImportException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModImportException):
        """
        Dynamic initializer for ModImportException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModImportException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModImportException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.Throwable)"""
        val = _ModImportException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.xeox.loader.ModImportException()"""
        val = _ModImportException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.String)"""
        val = _ModImportException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.xeox.loader.ModImportException(java.lang.String,java.lang.Throwable)"""
        val = _ModImportException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.xeox.loader.ModImportException()"""
        val = _ModImportException()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.xeox.loader.JSModInfo
from pyquantum_helper import import_once as _import_once
import dev.ultreon.xeox.loader.JSModInfo as _JSModInfo
_JSModInfo = _JSModInfo
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JSModInfo():
    """dev.ultreon.xeox.loader.JSModInfo"""
 
    @staticmethod
    def _wrap(java_value: _JSModInfo) -> 'JSModInfo':
        return JSModInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JSModInfo):
        """
        Dynamic initializer for JSModInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JSModInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JSModInfo__wrapper":
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

    @overload
    def makeId(self, arg0: str) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.xeox.loader.JSModInfo.makeId(java.lang.String)"""
        return 'util.Identifier'._wrap(super(_JSModInfo, self).makeId(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'XeoxMod'):
        """public dev.ultreon.xeox.loader.JSModInfo(dev.ultreon.xeox.loader.XeoxMod)"""
        val = _JSModInfo(arg0)
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
 
 
# CLASS: dev.ultreon.xeox.loader.XeoxMod
from pyquantum_helper import import_once as _import_once
import org.mozilla.javascript.Context as Context
import org.mozilla.javascript.ScriptableObject as ScriptableObject
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.xeox.loader.XeoxMod as _XeoxMod
_XeoxMod = _XeoxMod
import java.util.Collection as Collection
import java.lang.String as _string
import java.util.Optional as _Optional
_Optional = _Optional
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.mozilla.javascript.ScriptableObject as _ScriptableObject
_ScriptableObject = _ScriptableObject
import dev.ultreon.quantum.ModOrigin as _ModOrigin
_ModOrigin = _ModOrigin
import java.lang.Iterable as Iterable
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

import java.lang.String as _String
_String = _String
from builtins import object
import org.mozilla.javascript.Scriptable as Scriptable
import org.mozilla.javascript.Function as Function
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.xeox.loader.XeoxMetadata as _XeoxMetadata
_XeoxMetadata = _XeoxMetadata
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Optional as Optional
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class XeoxMod():
    """dev.ultreon.xeox.loader.XeoxMod"""
 
    @staticmethod
    def _wrap(java_value: _XeoxMod) -> 'XeoxMod':
        return XeoxMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _XeoxMod):
        """
        Dynamic initializer for XeoxMod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_XeoxMod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_XeoxMod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getIconPath(self, arg0: int) -> 'Optional':
        """public java.util.Optional<java.lang.String> dev.ultreon.xeox.loader.XeoxMod.getIconPath(int)"""
        return 'Optional'._wrap(super(_XeoxMod, self).getIconPath(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getName()"""
        return str._wrap(super(XeoxMod, self).getName())

    @override
    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getDescription()"""
        return str._wrap(super(XeoxMod, self).getDescription())

    @override
    @overload
    def getOrigin(self) -> 'pyquantum.ModOrigin':
        """public dev.ultreon.quantum.ModOrigin dev.ultreon.xeox.loader.XeoxMod.getOrigin()"""
        return 'pyquantum.ModOrigin'._wrap(super(XeoxMod, self).getOrigin())

    @overload
    def getMetadata(self) -> 'XeoxMetadata':
        """public dev.ultreon.xeox.loader.XeoxMetadata dev.ultreon.xeox.loader.XeoxMod.getMetadata()"""
        return 'XeoxMetadata'._wrap(super(XeoxMod, self).getMetadata())

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
    def init(self):
        """public void dev.ultreon.xeox.loader.XeoxMod.init() throws java.io.IOException"""
        super(XeoxMod, self).init()

    @overload
    def __init__(self, arg0: 'XeoxMetadata', arg1: str):
        """public dev.ultreon.xeox.loader.XeoxMod(dev.ultreon.xeox.loader.XeoxMetadata,java.lang.String)"""
        val = _XeoxMod(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def disable(self):
        """public void dev.ultreon.xeox.loader.XeoxMod.disable()"""
        super(XeoxMod, self).disable()

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

    @staticmethod
    @overload
    def importScript(arg0: 'Context', arg1: 'Scriptable', arg2: 'Object', arg3: 'Function') -> 'ScriptableObject':
        """public static org.mozilla.javascript.ScriptableObject dev.ultreon.xeox.loader.XeoxMod.importScript(org.mozilla.javascript.Context,org.mozilla.javascript.Scriptable,java.lang.Object[],org.mozilla.javascript.Function) throws java.io.IOException"""
        return ScriptableObject._wrap(_XeoxMod.importScript(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getAuthors(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.xeox.loader.XeoxMod.getAuthors()"""
        return 'Collection'._wrap(super(XeoxMod, self).getAuthors())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getId()"""
        return str._wrap(super(XeoxMod, self).getId())

        @staticmethod
        @overload
        def dispose():
            """public static void dev.ultreon.xeox.loader.XeoxMod.dispose()"""
            _XeoxMod.dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getPath()"""
        return str._wrap(super(XeoxMod, self).getPath())

    @override
    @overload
    def getRootPaths(self) -> 'Iterable':
        """public java.lang.Iterable<java.nio.file.Path> dev.ultreon.xeox.loader.XeoxMod.getRootPaths()"""
        return 'Iterable'._wrap(super(XeoxMod, self).getRootPaths())

    @override
    @overload
    def getVersion(self) -> str:
        """public java.lang.String dev.ultreon.xeox.loader.XeoxMod.getVersion()"""
        return str._wrap(super(XeoxMod, self).getVersion())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())