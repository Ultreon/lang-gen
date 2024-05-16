from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as _ClientRegistrationEvents
_ClientRegistrationEvents = _ClientRegistrationEvents
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientRegistrationEvents():
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientRegistrationEvents) -> 'ClientRegistrationEvents':
        return ClientRegistrationEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientRegistrationEvents):
        """
        Dynamic initializer for ClientRegistrationEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientRegistrationEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientRegistrationEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_ENTITY_MODELS
    BLOCK_ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDER_TYPES
    BLOCK_RENDER_TYPES: 'api.Event' = _wrap(_api.Event.BLOCK_RENDER_TYPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDERERS
    BLOCK_RENDERERS: 'api.Event' = _wrap(_api.Event.BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_MODELS
    BLOCK_MODELS: 'api.Event' = _wrap(_api.Event.BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_RENDERERS
    ENTITY_RENDERERS: 'api.Event' = _wrap(_api.Event.ENTITY_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_MODELS
    ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.ENTITY_MODELS)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = _ClientRegistrationEvents()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = _ClientRegistrationEvents()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents
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
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as _ClientRegistrationEvents
_ClientRegistrationEvents = _ClientRegistrationEvents
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientRegistrationEvents():
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientRegistrationEvents) -> 'ClientRegistrationEvents':
        return ClientRegistrationEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientRegistrationEvents):
        """
        Dynamic initializer for ClientRegistrationEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientRegistrationEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientRegistrationEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_ENTITY_MODELS
    BLOCK_ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDER_TYPES
    BLOCK_RENDER_TYPES: 'api.Event' = _wrap(_api.Event.BLOCK_RENDER_TYPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDERERS
    BLOCK_RENDERERS: 'api.Event' = _wrap(_api.Event.BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_MODELS
    BLOCK_MODELS: 'api.Event' = _wrap(_api.Event.BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_RENDERERS
    ENTITY_RENDERERS: 'api.Event' = _wrap(_api.Event.ENTITY_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_MODELS
    ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.ENTITY_MODELS)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = _ClientRegistrationEvents()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = _ClientRegistrationEvents()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowCreated
_WindowCreated = _WindowEvents_WindowCreated.WindowCreated
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
 
class WindowCreated():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowCreated"""
 
    @staticmethod
    def _wrap(java_value: _WindowCreated) -> 'WindowCreated':
        return WindowCreated(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowCreated):
        """
        Dynamic initializer for WindowCreated.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowCreated__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowCreated__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowCreated(self, arg0: 'GameWindow'):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated.onWindowCreated(dev.ultreon.quantum.GameWindow)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as _ClientLifecycleEvents_ClientStarted
_ClientStarted = _ClientLifecycleEvents_ClientStarted.ClientStarted
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

from abc import abstractmethod, ABC
 
class ClientStarted():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.ClientStarted"""
 
    @staticmethod
    def _wrap(java_value: _ClientStarted) -> 'ClientStarted':
        return ClientStarted(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientStarted):
        """
        Dynamic initializer for ClientStarted.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientStarted__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientStarted__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onGameLoaded(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted.onGameLoaded(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PreGameTick
_PreGameTick = _ClientTickEvents_PreGameTick.PreGameTick
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

from abc import abstractmethod, ABC
 
class PreGameTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PreGameTick"""
 
    @staticmethod
    def _wrap(java_value: _PreGameTick) -> 'PreGameTick':
        return PreGameTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PreGameTick):
        """
        Dynamic initializer for PreGameTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PreGameTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PreGameTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onGameTick(self, arg0: 'QuantumClient'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick.onGameTick(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PrePlayerTick
_PrePlayerTick = _ClientTickEvents_PrePlayerTick.PrePlayerTick
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

from abc import abstractmethod, ABC
 
class PrePlayerTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PrePlayerTick"""
 
    @staticmethod
    def _wrap(java_value: _PrePlayerTick) -> 'PrePlayerTick':
        return PrePlayerTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrePlayerTick):
        """
        Dynamic initializer for PrePlayerTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrePlayerTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrePlayerTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerTick(self, arg0: 'ClientPlayer'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick.onPlayerTick(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.RenderEvents as _RenderEvents_RenderWorld
_RenderWorld = _RenderEvents_RenderWorld.RenderWorld
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class RenderWorld():
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderWorld"""
 
    @staticmethod
    def _wrap(java_value: _RenderWorld) -> 'RenderWorld':
        return RenderWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderWorld):
        """
        Dynamic initializer for RenderWorld.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderWorld__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderWorld__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRenderWorld(self, arg0: 'World', arg1: 'WorldRenderer'):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld.onRenderWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.client.world.WorldRenderer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as _ClientPlayerEvents_PlayerJoined
_PlayerJoined = _ClientPlayerEvents_PlayerJoined.PlayerJoined
from abc import abstractmethod, ABC
 
class PlayerJoined():
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PlayerJoined"""
 
    @staticmethod
    def _wrap(java_value: _PlayerJoined) -> 'PlayerJoined':
        return PlayerJoined(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerJoined):
        """
        Dynamic initializer for PlayerJoined.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerJoined__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerJoined__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerJoined(self, arg0: 'ClientPlayer'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined.onPlayerJoined(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized
from pyquantum_helper import import_once as _import_once
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowResized
_WindowResized = _WindowEvents_WindowResized.WindowResized
 
class WindowResized():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowResized"""
 
    @staticmethod
    def _wrap(java_value: _WindowResized) -> 'WindowResized':
        return WindowResized(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowResized):
        """
        Dynamic initializer for WindowResized.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowResized__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowResized__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowResized(self, arg0: 'GameWindow', arg1: int, arg2: int):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized.onWindowResized(dev.ultreon.quantum.GameWindow,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as _ClientReloadEvent_SkinReload
_SkinReload = _ClientReloadEvent_SkinReload.SkinReload
from abc import abstractmethod, ABC
 
class SkinReload():
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent.SkinReload"""
 
    @staticmethod
    def _wrap(java_value: _SkinReload) -> 'SkinReload':
        return SkinReload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkinReload):
        """
        Dynamic initializer for SkinReload.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkinReload__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkinReload__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSkinReload(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload.onSkinReload()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.api.events.RenderEvents as _RenderEvents
_RenderEvents = _RenderEvents
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderEvents():
    """dev.ultreon.quantum.client.api.events.RenderEvents"""
 
    @staticmethod
    def _wrap(java_value: _RenderEvents) -> 'RenderEvents':
        return RenderEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderEvents):
        """
        Dynamic initializer for RenderEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_WORLD
    POST_RENDER_WORLD: 'api.Event' = _wrap(_api.Event.POST_RENDER_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_SCREEN
    PRE_RENDER_SCREEN: 'api.Event' = _wrap(_api.Event.PRE_RENDER_SCREEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_SCREEN
    POST_RENDER_SCREEN: 'api.Event' = _wrap(_api.Event.POST_RENDER_SCREEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_GAME
    PRE_RENDER_GAME: 'api.Event' = _wrap(_api.Event.PRE_RENDER_GAME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay> dev.ultreon.quantum.client.api.events.RenderEvents.RENDER_OVERLAY
    RENDER_OVERLAY: 'api.Event' = _wrap(_api.Event.RENDER_OVERLAY)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_GAME
    POST_RENDER_GAME: 'api.Event' = _wrap(_api.Event.POST_RENDER_GAME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_WORLD
    PRE_RENDER_WORLD: 'api.Event' = _wrap(_api.Event.PRE_RENDER_WORLD)


    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.RenderEvents()"""
        val = _RenderEvents()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.RenderEvents()"""
        val = _RenderEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowFocusChanged
_WindowFocusChanged = _WindowEvents_WindowFocusChanged.WindowFocusChanged
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
 
class WindowFocusChanged():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowFocusChanged"""
 
    @staticmethod
    def _wrap(java_value: _WindowFocusChanged) -> 'WindowFocusChanged':
        return WindowFocusChanged(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowFocusChanged):
        """
        Dynamic initializer for WindowFocusChanged.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowFocusChanged__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowFocusChanged__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowFocusChanged(self, arg0: 'GameWindow', arg1: bool):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged.onWindowFocusChanged(dev.ultreon.quantum.GameWindow,boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PostWorldTick
_PostWorldTick = _ClientTickEvents_PostWorldTick.PostWorldTick
from abc import abstractmethod, ABC
 
class PostWorldTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostWorldTick"""
 
    @staticmethod
    def _wrap(java_value: _PostWorldTick) -> 'PostWorldTick':
        return PostWorldTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PostWorldTick):
        """
        Dynamic initializer for PostWorldTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PostWorldTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PostWorldTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWorldTick(self, arg0: 'ClientWorld'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick.onWorldTick(dev.ultreon.quantum.client.world.ClientWorld)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents
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
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents
_WindowEvents = _WindowEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WindowEvents():
    """dev.ultreon.quantum.client.api.events.WindowEvents"""
 
    @staticmethod
    def _wrap(java_value: _WindowEvents) -> 'WindowEvents':
        return WindowEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowEvents):
        """
        Dynamic initializer for WindowEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_FOCUS_CHANGED
    WINDOW_FOCUS_CHANGED: 'api.Event' = _wrap(_api.Event.WINDOW_FOCUS_CHANGED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_FILES_DROPPED
    WINDOW_FILES_DROPPED: 'api.Event' = _wrap(_api.Event.WINDOW_FILES_DROPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_RESIZED
    WINDOW_RESIZED: 'api.Event' = _wrap(_api.Event.WINDOW_RESIZED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_CLOSE_REQUESTED
    WINDOW_CLOSE_REQUESTED: 'api.Event' = _wrap(_api.Event.WINDOW_CLOSE_REQUESTED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_MOVED
    WINDOW_MOVED: 'api.Event' = _wrap(_api.Event.WINDOW_MOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_CREATED
    WINDOW_CREATED: 'api.Event' = _wrap(_api.Event.WINDOW_CREATED)


    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.WindowEvents()"""
        val = _WindowEvents()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.WindowEvents()"""
        val = _WindowEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PostGameTick
_PostGameTick = _ClientTickEvents_PostGameTick.PostGameTick
from abc import abstractmethod, ABC
 
class PostGameTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostGameTick"""
 
    @staticmethod
    def _wrap(java_value: _PostGameTick) -> 'PostGameTick':
        return PostGameTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PostGameTick):
        """
        Dynamic initializer for PostGameTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PostGameTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PostGameTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onGameTick(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick.onGameTick(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PostPlayerTick
_PostPlayerTick = _ClientTickEvents_PostPlayerTick.PostPlayerTick
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

from abc import abstractmethod, ABC
 
class PostPlayerTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostPlayerTick"""
 
    @staticmethod
    def _wrap(java_value: _PostPlayerTick) -> 'PostPlayerTick':
        return PostPlayerTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PostPlayerTick):
        """
        Dynamic initializer for PostPlayerTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PostPlayerTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PostPlayerTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerTick(self, arg0: 'ClientPlayer'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick.onPlayerTick(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Built
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

import dev.ultreon.quantum.client.api.events.ClientChunkEvents as _ClientChunkEvents_Built
_Built = _ClientChunkEvents_Built.Built
from abc import abstractmethod, ABC
 
class Built():
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Built"""
 
    @staticmethod
    def _wrap(java_value: _Built) -> 'Built':
        return Built(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Built):
        """
        Dynamic initializer for Built.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Built__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Built__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onClientChunkBuilt(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Built.onClientChunkBuilt(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as _ClientLifecycleEvents_Registration
_Registration = _ClientLifecycleEvents_Registration.Registration
from abc import abstractmethod, ABC
 
class Registration():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.Registration"""
 
    @staticmethod
    def _wrap(java_value: _Registration) -> 'Registration':
        return Registration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Registration):
        """
        Dynamic initializer for Registration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Registration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Registration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegister(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.RenderEvents as _RenderEvents_RenderScreen
_RenderScreen = _RenderEvents_RenderScreen.RenderScreen
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class RenderScreen():
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderScreen"""
 
    @staticmethod
    def _wrap(java_value: _RenderScreen) -> 'RenderScreen':
        return RenderScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderScreen):
        """
        Dynamic initializer for RenderScreen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderScreen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderScreen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRenderScreen(self, arg0: 'Screen', arg1: 'Renderer', arg2: float, arg3: float, arg4: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen.onRenderScreen(dev.ultreon.quantum.client.gui.Screen,dev.ultreon.quantum.client.gui.Renderer,float,float,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

import dev.ultreon.quantum.client.api.events.RenderEvents as _RenderEvents_RenderGame
_RenderGame = _RenderEvents_RenderGame.RenderGame
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

from abc import abstractmethod, ABC
 
class RenderGame():
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderGame"""
 
    @staticmethod
    def _wrap(java_value: _RenderGame) -> 'RenderGame':
        return RenderGame(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderGame):
        """
        Dynamic initializer for RenderGame.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderGame__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderGame__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRenderGame(self, arg0: 'GameRenderer', arg1: 'Renderer', arg2: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame.onRenderGame(dev.ultreon.quantum.client.GameRenderer,dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as _ClientRegistrationEvents_Registration
_Registration = _ClientRegistrationEvents_Registration.Registration
from abc import abstractmethod, ABC
 
class Registration():
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.Registration"""
 
    @staticmethod
    def _wrap(java_value: _Registration) -> 'Registration':
        return Registration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Registration):
        """
        Dynamic initializer for Registration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Registration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Registration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegister(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as _ClientLifecycleEvents_ClientStopped
_ClientStopped = _ClientLifecycleEvents_ClientStopped.ClientStopped
from abc import abstractmethod, ABC
 
class ClientStopped():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.ClientStopped"""
 
    @staticmethod
    def _wrap(java_value: _ClientStopped) -> 'ClientStopped':
        return ClientStopped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientStopped):
        """
        Dynamic initializer for ClientStopped.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientStopped__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientStopped__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onGameDisposed(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped.onGameDisposed()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents
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
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as _ClientLifecycleEvents
_ClientLifecycleEvents = _ClientLifecycleEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientLifecycleEvents():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientLifecycleEvents) -> 'ClientLifecycleEvents':
        return ClientLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientLifecycleEvents):
        """
        Dynamic initializer for ClientLifecycleEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientLifecycleEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientLifecycleEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.GAME_LOADED
    GAME_LOADED: 'api.Event' = _wrap(_api.Event.GAME_LOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_ENTITY_RENDERERS
    REGISTER_ENTITY_RENDERERS: 'api.Event' = _wrap(_api.Event.REGISTER_ENTITY_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_ENTITY_MODELS
    REGISTER_BLOCK_ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.REGISTER_BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.WINDOW_CLOSED
    WINDOW_CLOSED: 'api.Event' = _wrap(_api.Event.WINDOW_CLOSED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.CLIENT_STARTED
    CLIENT_STARTED: 'api.Event' = _wrap(_api.Event.CLIENT_STARTED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_MODELS
    REGISTER_BLOCK_MODELS: 'api.Event' = _wrap(_api.Event.REGISTER_BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.CLIENT_STOPPED
    CLIENT_STOPPED: 'api.Event' = _wrap(_api.Event.CLIENT_STOPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_RENDERERS
    REGISTER_BLOCK_RENDERERS: 'api.Event' = _wrap(_api.Event.REGISTER_BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.GAME_DISPOSED
    GAME_DISPOSED: 'api.Event' = _wrap(_api.Event.GAME_DISPOSED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_RENDER_TYPES
    REGISTER_BLOCK_RENDER_TYPES: 'api.Event' = _wrap(_api.Event.REGISTER_BLOCK_RENDER_TYPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_ENTITY_MODELS
    REGISTER_ENTITY_MODELS: 'api.Event' = _wrap(_api.Event.REGISTER_ENTITY_MODELS)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientLifecycleEvents()"""
        val = _ClientLifecycleEvents()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientLifecycleEvents()"""
        val = _ClientLifecycleEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.RenderEvents as _RenderEvents_RenderOverlay
_RenderOverlay = _RenderEvents_RenderOverlay.RenderOverlay
try:
    from pyquantum.client import gui
except ImportError:
    gui = _import_once("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class RenderOverlay():
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderOverlay"""
 
    @staticmethod
    def _wrap(java_value: _RenderOverlay) -> 'RenderOverlay':
        return RenderOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderOverlay):
        """
        Dynamic initializer for RenderOverlay.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderOverlay__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderOverlay__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRenderOverlay(self, arg0: 'Renderer', arg1: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay.onRenderOverlay(dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.client import player
except ImportError:
    player = _import_once("pyquantum.client.player")

import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as _ClientPlayerEvents_PlayerLeft
_PlayerLeft = _ClientPlayerEvents_PlayerLeft.PlayerLeft
from abc import abstractmethod, ABC
 
class PlayerLeft():
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PlayerLeft"""
 
    @staticmethod
    def _wrap(java_value: _PlayerLeft) -> 'PlayerLeft':
        return PlayerLeft(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerLeft):
        """
        Dynamic initializer for PlayerLeft.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerLeft__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerLeft__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerLeft(self, arg0: 'ClientPlayer', arg1: str):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft.onPlayerLeft(dev.ultreon.quantum.client.player.ClientPlayer,java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents
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
import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as _ClientPlayerEvents
_ClientPlayerEvents = _ClientPlayerEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientPlayerEvents():
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientPlayerEvents) -> 'ClientPlayerEvents':
        return ClientPlayerEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientPlayerEvents):
        """
        Dynamic initializer for ClientPlayerEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientPlayerEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientPlayerEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft> dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PLAYER_LEFT
    PLAYER_LEFT: 'api.Event' = _wrap(_api.Event.PLAYER_LEFT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined> dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PLAYER_JOINED
    PLAYER_JOINED: 'api.Event' = _wrap(_api.Event.PLAYER_JOINED)


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
        """public dev.ultreon.quantum.client.api.events.ClientPlayerEvents()"""
        val = _ClientPlayerEvents()
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
        """public dev.ultreon.quantum.client.api.events.ClientPlayerEvents()"""
        val = _ClientPlayerEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowMoved
_WindowMoved = _WindowEvents_WindowMoved.WindowMoved
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
 
class WindowMoved():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowMoved"""
 
    @staticmethod
    def _wrap(java_value: _WindowMoved) -> 'WindowMoved':
        return WindowMoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowMoved):
        """
        Dynamic initializer for WindowMoved.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowMoved__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowMoved__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowMoved(self, arg0: 'GameWindow', arg1: int, arg2: int):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved.onWindowMoved(dev.ultreon.quantum.GameWindow,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as _ClientLifecycleEvents_WindowClosed
_WindowClosed = _ClientLifecycleEvents_WindowClosed.WindowClosed
from abc import abstractmethod, ABC
 
class WindowClosed():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.WindowClosed"""
 
    @staticmethod
    def _wrap(java_value: _WindowClosed) -> 'WindowClosed':
        return WindowClosed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowClosed):
        """
        Dynamic initializer for WindowClosed.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowClosed__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowClosed__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowClose(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed.onWindowClose()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as _ClientChunkEvents_Received
_Received = _ClientChunkEvents_Received.Received
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class Received():
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Received"""
 
    @staticmethod
    def _wrap(java_value: _Received) -> 'Received':
        return Received(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Received):
        """
        Dynamic initializer for Received.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Received__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Received__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onClientChunkReceived(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received.onClientChunkReceived(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent
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
import java.lang.Integer as _int
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as _ClientReloadEvent
_ClientReloadEvent = _ClientReloadEvent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientReloadEvent():
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent"""
 
    @staticmethod
    def _wrap(java_value: _ClientReloadEvent) -> 'ClientReloadEvent':
        return ClientReloadEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientReloadEvent):
        """
        Dynamic initializer for ClientReloadEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientReloadEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientReloadEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload> dev.ultreon.quantum.client.api.events.ClientReloadEvent.SKIN_RELOAD
    SKIN_RELOAD: 'api.Event' = _wrap(_api.Event.SKIN_RELOAD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded> dev.ultreon.quantum.client.api.events.ClientReloadEvent.SKIN_LOADED
    SKIN_LOADED: 'api.Event' = _wrap(_api.Event.SKIN_LOADED)


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
        """public dev.ultreon.quantum.client.api.events.ClientReloadEvent()"""
        val = _ClientReloadEvent()
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
        """public dev.ultreon.quantum.client.api.events.ClientReloadEvent()"""
        val = _ClientReloadEvent()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as _ClientReloadEvent_SkinLoaded
_SkinLoaded = _ClientReloadEvent_SkinLoaded.SkinLoaded
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

 
class SkinLoaded():
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent.SkinLoaded"""
 
    @staticmethod
    def _wrap(java_value: _SkinLoaded) -> 'SkinLoaded':
        return SkinLoaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SkinLoaded):
        """
        Dynamic initializer for SkinLoaded.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SkinLoaded__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SkinLoaded__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSkinLoaded(self, arg0: 'Texture', arg1: 'Pixmap'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded.onSkinLoaded(com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Pixmap)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowFilesDropped
_WindowFilesDropped = _WindowEvents_WindowFilesDropped.WindowFilesDropped
 
class WindowFilesDropped():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowFilesDropped"""
 
    @staticmethod
    def _wrap(java_value: _WindowFilesDropped) -> 'WindowFilesDropped':
        return WindowFilesDropped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowFilesDropped):
        """
        Dynamic initializer for WindowFilesDropped.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowFilesDropped__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowFilesDropped__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowFilesDropped(self, arg0: 'GameWindow', arg1: 'String'):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped.onWindowFilesDropped(dev.ultreon.quantum.GameWindow,java.lang.String[])"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents
_ClientTickEvents = _ClientTickEvents
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientTickEvents():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientTickEvents) -> 'ClientTickEvents':
        return ClientTickEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientTickEvents):
        """
        Dynamic initializer for ClientTickEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientTickEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientTickEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_WORLD_TICK
    PRE_WORLD_TICK: 'api.Event' = _wrap(_api.Event.PRE_WORLD_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_GAME_TICK
    POST_GAME_TICK: 'api.Event' = _wrap(_api.Event.POST_GAME_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_PLAYER_TICK
    PRE_PLAYER_TICK: 'api.Event' = _wrap(_api.Event.PRE_PLAYER_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_WORLD_TICK
    POST_WORLD_TICK: 'api.Event' = _wrap(_api.Event.POST_WORLD_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_GAME_TICK
    PRE_GAME_TICK: 'api.Event' = _wrap(_api.Event.PRE_GAME_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_PLAYER_TICK
    POST_PLAYER_TICK: 'api.Event' = _wrap(_api.Event.POST_PLAYER_TICK)


    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientTickEvents()"""
        val = _ClientTickEvents()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientTickEvents()"""
        val = _ClientTickEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as _ClientChunkEvents_Rebuilt
_Rebuilt = _ClientChunkEvents_Rebuilt.Rebuilt
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class Rebuilt():
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Rebuilt"""
 
    @staticmethod
    def _wrap(java_value: _Rebuilt) -> 'Rebuilt':
        return Rebuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rebuilt):
        """
        Dynamic initializer for Rebuilt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rebuilt__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rebuilt__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onClientChunkRebuilt(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt.onClientChunkRebuilt(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.WindowEvents as _WindowEvents_WindowCloseRequested
_WindowCloseRequested = _WindowEvents_WindowCloseRequested.WindowCloseRequested
try:
    import pyquantum
except ImportError:
    pyquantum = _import_once("pyquantum")

from abc import abstractmethod, ABC
 
class WindowCloseRequested():
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowCloseRequested"""
 
    @staticmethod
    def _wrap(java_value: _WindowCloseRequested) -> 'WindowCloseRequested':
        return WindowCloseRequested(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowCloseRequested):
        """
        Dynamic initializer for WindowCloseRequested.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowCloseRequested__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowCloseRequested__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWindowCloseRequested(self, arg0: 'GameWindow'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested.onWindowCloseRequested(dev.ultreon.quantum.GameWindow)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.api.events.ClientTickEvents as _ClientTickEvents_PreWorldTick
_PreWorldTick = _ClientTickEvents_PreWorldTick.PreWorldTick
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class PreWorldTick():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PreWorldTick"""
 
    @staticmethod
    def _wrap(java_value: _PreWorldTick) -> 'PreWorldTick':
        return PreWorldTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PreWorldTick):
        """
        Dynamic initializer for PreWorldTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PreWorldTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PreWorldTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onWorldTick(self, arg0: 'ClientWorld'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick.onWorldTick(dev.ultreon.quantum.client.world.ClientWorld)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents
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
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as _ClientChunkEvents
_ClientChunkEvents = _ClientChunkEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientChunkEvents():
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents"""
 
    @staticmethod
    def _wrap(java_value: _ClientChunkEvents) -> 'ClientChunkEvents':
        return ClientChunkEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientChunkEvents):
        """
        Dynamic initializer for ClientChunkEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientChunkEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientChunkEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received> dev.ultreon.quantum.client.api.events.ClientChunkEvents.RECEIVED
    RECEIVED: 'api.Event' = _wrap(_api.Event.RECEIVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt> dev.ultreon.quantum.client.api.events.ClientChunkEvents.BUILT
    BUILT: 'api.Event' = _wrap(_api.Event.BUILT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt> dev.ultreon.quantum.client.api.events.ClientChunkEvents.REBUILT
    REBUILT: 'api.Event' = _wrap(_api.Event.REBUILT)


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
        """public dev.ultreon.quantum.client.api.events.ClientChunkEvents()"""
        val = _ClientChunkEvents()
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
        """public dev.ultreon.quantum.client.api.events.ClientChunkEvents()"""
        val = _ClientChunkEvents()
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