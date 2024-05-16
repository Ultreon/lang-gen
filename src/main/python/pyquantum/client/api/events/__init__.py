from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as __ClientRegistrationEvents
__ClientRegistrationEvents = __ClientRegistrationEvents
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientRegistrationEvents():
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientRegistrationEvents) -> 'ClientRegistrationEvents':
        return ClientRegistrationEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientRegistrationEvents):
        """
        Dynamic initializer for ClientRegistrationEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDER_TYPES
    BLOCK_RENDER_TYPES: 'api.Event' = __wrap(__api.Event.BLOCK_RENDER_TYPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDERERS
    BLOCK_RENDERERS: 'api.Event' = __wrap(__api.Event.BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_ENTITY_MODELS
    BLOCK_ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_MODELS
    BLOCK_MODELS: 'api.Event' = __wrap(__api.Event.BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_MODELS
    ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_RENDERERS
    ENTITY_RENDERERS: 'api.Event' = __wrap(__api.Event.ENTITY_RENDERERS)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = __ClientRegistrationEvents()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = __ClientRegistrationEvents()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as __ClientRegistrationEvents
__ClientRegistrationEvents = __ClientRegistrationEvents
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientRegistrationEvents():
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientRegistrationEvents) -> 'ClientRegistrationEvents':
        return ClientRegistrationEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientRegistrationEvents):
        """
        Dynamic initializer for ClientRegistrationEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDER_TYPES
    BLOCK_RENDER_TYPES: 'api.Event' = __wrap(__api.Event.BLOCK_RENDER_TYPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_RENDERERS
    BLOCK_RENDERERS: 'api.Event' = __wrap(__api.Event.BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_ENTITY_MODELS
    BLOCK_ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.BLOCK_MODELS
    BLOCK_MODELS: 'api.Event' = __wrap(__api.Event.BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_MODELS
    ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration> dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.ENTITY_RENDERERS
    ENTITY_RENDERERS: 'api.Event' = __wrap(__api.Event.ENTITY_RENDERERS)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = __ClientRegistrationEvents()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientRegistrationEvents()"""
        val = __ClientRegistrationEvents()
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

 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowCreated
__WindowCreated = __WindowEvents_WindowCreated.WindowCreated
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
 
class WindowCreated(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowCreated"""
 
    @staticmethod
    def __wrap(java_value: __WindowCreated) -> 'WindowCreated':
        return WindowCreated(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowCreated):
        """
        Dynamic initializer for WindowCreated.
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
    def onWindowCreated(self, arg0: 'GameWindow'):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated.onWindowCreated(dev.ultreon.quantum.GameWindow)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as __ClientLifecycleEvents_ClientStarted
__ClientStarted = __ClientLifecycleEvents_ClientStarted.ClientStarted
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

from abc import abstractmethod, ABC
 
class ClientStarted(ABC):
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.ClientStarted"""
 
    @staticmethod
    def __wrap(java_value: __ClientStarted) -> 'ClientStarted':
        return ClientStarted(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientStarted):
        """
        Dynamic initializer for ClientStarted.
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
    def onGameLoaded(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted.onGameLoaded(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PreGameTick
__PreGameTick = __ClientTickEvents_PreGameTick.PreGameTick
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

from abc import abstractmethod, ABC
 
class PreGameTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PreGameTick"""
 
    @staticmethod
    def __wrap(java_value: __PreGameTick) -> 'PreGameTick':
        return PreGameTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PreGameTick):
        """
        Dynamic initializer for PreGameTick.
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
    def onGameTick(self, arg0: 'QuantumClient'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick.onGameTick(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PrePlayerTick
__PrePlayerTick = __ClientTickEvents_PrePlayerTick.PrePlayerTick
from abc import abstractmethod, ABC
 
class PrePlayerTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PrePlayerTick"""
 
    @staticmethod
    def __wrap(java_value: __PrePlayerTick) -> 'PrePlayerTick':
        return PrePlayerTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrePlayerTick):
        """
        Dynamic initializer for PrePlayerTick.
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
    def onPlayerTick(self, arg0: 'ClientPlayer'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick.onPlayerTick(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.client.api.events.RenderEvents as __RenderEvents_RenderWorld
__RenderWorld = __RenderEvents_RenderWorld.RenderWorld
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class RenderWorld(ABC):
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderWorld"""
 
    @staticmethod
    def __wrap(java_value: __RenderWorld) -> 'RenderWorld':
        return RenderWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderWorld):
        """
        Dynamic initializer for RenderWorld.
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
    def onRenderWorld(self, arg0: 'World', arg1: 'WorldRenderer'):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld.onRenderWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.client.world.WorldRenderer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as __ClientPlayerEvents_PlayerJoined
__PlayerJoined = __ClientPlayerEvents_PlayerJoined.PlayerJoined
 
class PlayerJoined(ABC):
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PlayerJoined"""
 
    @staticmethod
    def __wrap(java_value: __PlayerJoined) -> 'PlayerJoined':
        return PlayerJoined(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerJoined):
        """
        Dynamic initializer for PlayerJoined.
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
    def onPlayerJoined(self, arg0: 'ClientPlayer'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined.onPlayerJoined(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowResized
__WindowResized = __WindowEvents_WindowResized.WindowResized
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
 
class WindowResized(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowResized"""
 
    @staticmethod
    def __wrap(java_value: __WindowResized) -> 'WindowResized':
        return WindowResized(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowResized):
        """
        Dynamic initializer for WindowResized.
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
    def onWindowResized(self, arg0: 'GameWindow', arg1: int, arg2: int):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized.onWindowResized(dev.ultreon.quantum.GameWindow,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as __ClientReloadEvent_SkinReload
__SkinReload = __ClientReloadEvent_SkinReload.SkinReload
from abc import abstractmethod, ABC
 
class SkinReload(ABC):
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent.SkinReload"""
 
    @staticmethod
    def __wrap(java_value: __SkinReload) -> 'SkinReload':
        return SkinReload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkinReload):
        """
        Dynamic initializer for SkinReload.
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
    def onSkinReload(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload.onSkinReload()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents
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
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.client.api.events.RenderEvents as __RenderEvents
__RenderEvents = __RenderEvents
from builtins import int
 
class RenderEvents():
    """dev.ultreon.quantum.client.api.events.RenderEvents"""
 
    @staticmethod
    def __wrap(java_value: __RenderEvents) -> 'RenderEvents':
        return RenderEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderEvents):
        """
        Dynamic initializer for RenderEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay> dev.ultreon.quantum.client.api.events.RenderEvents.RENDER_OVERLAY
    RENDER_OVERLAY: 'api.Event' = __wrap(__api.Event.RENDER_OVERLAY)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_WORLD
    PRE_RENDER_WORLD: 'api.Event' = __wrap(__api.Event.PRE_RENDER_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_GAME
    PRE_RENDER_GAME: 'api.Event' = __wrap(__api.Event.PRE_RENDER_GAME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen> dev.ultreon.quantum.client.api.events.RenderEvents.PRE_RENDER_SCREEN
    PRE_RENDER_SCREEN: 'api.Event' = __wrap(__api.Event.PRE_RENDER_SCREEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderWorld> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_WORLD
    POST_RENDER_WORLD: 'api.Event' = __wrap(__api.Event.POST_RENDER_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_GAME
    POST_RENDER_GAME: 'api.Event' = __wrap(__api.Event.POST_RENDER_GAME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen> dev.ultreon.quantum.client.api.events.RenderEvents.POST_RENDER_SCREEN
    POST_RENDER_SCREEN: 'api.Event' = __wrap(__api.Event.POST_RENDER_SCREEN)


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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.RenderEvents()"""
        val = __RenderEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.RenderEvents()"""
        val = __RenderEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowFocusChanged
__WindowFocusChanged = __WindowEvents_WindowFocusChanged.WindowFocusChanged
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
 
class WindowFocusChanged(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowFocusChanged"""
 
    @staticmethod
    def __wrap(java_value: __WindowFocusChanged) -> 'WindowFocusChanged':
        return WindowFocusChanged(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowFocusChanged):
        """
        Dynamic initializer for WindowFocusChanged.
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
    def onWindowFocusChanged(self, arg0: 'GameWindow', arg1: bool):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged.onWindowFocusChanged(dev.ultreon.quantum.GameWindow,boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PostWorldTick
__PostWorldTick = __ClientTickEvents_PostWorldTick.PostWorldTick
from abc import abstractmethod, ABC
 
class PostWorldTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostWorldTick"""
 
    @staticmethod
    def __wrap(java_value: __PostWorldTick) -> 'PostWorldTick':
        return PostWorldTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PostWorldTick):
        """
        Dynamic initializer for PostWorldTick.
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
    def onWorldTick(self, arg0: 'ClientWorld'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick.onWorldTick(dev.ultreon.quantum.client.world.ClientWorld)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents
__WindowEvents = __WindowEvents
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WindowEvents():
    """dev.ultreon.quantum.client.api.events.WindowEvents"""
 
    @staticmethod
    def __wrap(java_value: __WindowEvents) -> 'WindowEvents':
        return WindowEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowEvents):
        """
        Dynamic initializer for WindowEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowFocusChanged> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_FOCUS_CHANGED
    WINDOW_FOCUS_CHANGED: 'api.Event' = __wrap(__api.Event.WINDOW_FOCUS_CHANGED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_MOVED
    WINDOW_MOVED: 'api.Event' = __wrap(__api.Event.WINDOW_MOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowResized> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_RESIZED
    WINDOW_RESIZED: 'api.Event' = __wrap(__api.Event.WINDOW_RESIZED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_CLOSE_REQUESTED
    WINDOW_CLOSE_REQUESTED: 'api.Event' = __wrap(__api.Event.WINDOW_CLOSE_REQUESTED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_FILES_DROPPED
    WINDOW_FILES_DROPPED: 'api.Event' = __wrap(__api.Event.WINDOW_FILES_DROPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.WindowEvents$WindowCreated> dev.ultreon.quantum.client.api.events.WindowEvents.WINDOW_CREATED
    WINDOW_CREATED: 'api.Event' = __wrap(__api.Event.WINDOW_CREATED)


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
        """public dev.ultreon.quantum.client.api.events.WindowEvents()"""
        val = __WindowEvents()
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
        """public dev.ultreon.quantum.client.api.events.WindowEvents()"""
        val = __WindowEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PostGameTick
__PostGameTick = __ClientTickEvents_PostGameTick.PostGameTick
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

from abc import abstractmethod, ABC
 
class PostGameTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostGameTick"""
 
    @staticmethod
    def __wrap(java_value: __PostGameTick) -> 'PostGameTick':
        return PostGameTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PostGameTick):
        """
        Dynamic initializer for PostGameTick.
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
    def onGameTick(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick.onGameTick(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PostPlayerTick
__PostPlayerTick = __ClientTickEvents_PostPlayerTick.PostPlayerTick
from abc import abstractmethod, ABC
 
class PostPlayerTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PostPlayerTick"""
 
    @staticmethod
    def __wrap(java_value: __PostPlayerTick) -> 'PostPlayerTick':
        return PostPlayerTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PostPlayerTick):
        """
        Dynamic initializer for PostPlayerTick.
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
    def onPlayerTick(self, arg0: 'ClientPlayer'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick.onPlayerTick(dev.ultreon.quantum.client.player.ClientPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Built
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import dev.ultreon.quantum.client.api.events.ClientChunkEvents as __ClientChunkEvents_Built
__Built = __ClientChunkEvents_Built.Built
from abc import abstractmethod, ABC
 
class Built(ABC):
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Built"""
 
    @staticmethod
    def __wrap(java_value: __Built) -> 'Built':
        return Built(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Built):
        """
        Dynamic initializer for Built.
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
    def onClientChunkBuilt(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Built.onClientChunkBuilt(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as __ClientLifecycleEvents_Registration
__Registration = __ClientLifecycleEvents_Registration.Registration
from abc import abstractmethod, ABC
 
class Registration(ABC):
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.Registration"""
 
    @staticmethod
    def __wrap(java_value: __Registration) -> 'Registration':
        return Registration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Registration):
        """
        Dynamic initializer for Registration.
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
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.RenderEvents as __RenderEvents_RenderScreen
__RenderScreen = __RenderEvents_RenderScreen.RenderScreen
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

from abc import abstractmethod, ABC
 
class RenderScreen(ABC):
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderScreen"""
 
    @staticmethod
    def __wrap(java_value: __RenderScreen) -> 'RenderScreen':
        return RenderScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderScreen):
        """
        Dynamic initializer for RenderScreen.
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
    def onRenderScreen(self, arg0: 'Screen', arg1: 'Renderer', arg2: float, arg3: float, arg4: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderScreen.onRenderScreen(dev.ultreon.quantum.client.gui.Screen,dev.ultreon.quantum.client.gui.Renderer,float,float,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.RenderEvents as __RenderEvents_RenderGame
__RenderGame = __RenderEvents_RenderGame.RenderGame
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

from abc import abstractmethod, ABC
 
class RenderGame(ABC):
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderGame"""
 
    @staticmethod
    def __wrap(java_value: __RenderGame) -> 'RenderGame':
        return RenderGame(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderGame):
        """
        Dynamic initializer for RenderGame.
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
    def onRenderGame(self, arg0: 'GameRenderer', arg1: 'Renderer', arg2: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderGame.onRenderGame(dev.ultreon.quantum.client.GameRenderer,dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.ClientRegistrationEvents as __ClientRegistrationEvents_Registration
__Registration = __ClientRegistrationEvents_Registration.Registration
 
class Registration(ABC):
    """dev.ultreon.quantum.client.api.events.ClientRegistrationEvents.Registration"""
 
    @staticmethod
    def __wrap(java_value: __Registration) -> 'Registration':
        return Registration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Registration):
        """
        Dynamic initializer for Registration.
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
        """public abstract void dev.ultreon.quantum.client.api.events.ClientRegistrationEvents$Registration.onRegister()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as __ClientLifecycleEvents_ClientStopped
__ClientStopped = __ClientLifecycleEvents_ClientStopped.ClientStopped
from abc import abstractmethod, ABC
 
class ClientStopped(ABC):
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.ClientStopped"""
 
    @staticmethod
    def __wrap(java_value: __ClientStopped) -> 'ClientStopped':
        return ClientStopped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientStopped):
        """
        Dynamic initializer for ClientStopped.
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
    def onGameDisposed(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped.onGameDisposed()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents
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
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as __ClientLifecycleEvents
__ClientLifecycleEvents = __ClientLifecycleEvents
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientLifecycleEvents():
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientLifecycleEvents) -> 'ClientLifecycleEvents':
        return ClientLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientLifecycleEvents):
        """
        Dynamic initializer for ClientLifecycleEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_ENTITY_MODELS
    REGISTER_BLOCK_ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.REGISTER_BLOCK_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_MODELS
    REGISTER_BLOCK_MODELS: 'api.Event' = __wrap(__api.Event.REGISTER_BLOCK_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_ENTITY_MODELS
    REGISTER_ENTITY_MODELS: 'api.Event' = __wrap(__api.Event.REGISTER_ENTITY_MODELS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.CLIENT_STOPPED
    CLIENT_STOPPED: 'api.Event' = __wrap(__api.Event.CLIENT_STOPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_ENTITY_RENDERERS
    REGISTER_ENTITY_RENDERERS: 'api.Event' = __wrap(__api.Event.REGISTER_ENTITY_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.WINDOW_CLOSED
    WINDOW_CLOSED: 'api.Event' = __wrap(__api.Event.WINDOW_CLOSED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStopped> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.GAME_DISPOSED
    GAME_DISPOSED: 'api.Event' = __wrap(__api.Event.GAME_DISPOSED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.CLIENT_STARTED
    CLIENT_STARTED: 'api.Event' = __wrap(__api.Event.CLIENT_STARTED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$ClientStarted> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.GAME_LOADED
    GAME_LOADED: 'api.Event' = __wrap(__api.Event.GAME_LOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_RENDERERS
    REGISTER_BLOCK_RENDERERS: 'api.Event' = __wrap(__api.Event.REGISTER_BLOCK_RENDERERS)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$Registration> dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.REGISTER_BLOCK_RENDER_TYPES
    REGISTER_BLOCK_RENDER_TYPES: 'api.Event' = __wrap(__api.Event.REGISTER_BLOCK_RENDER_TYPES)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientLifecycleEvents()"""
        val = __ClientLifecycleEvents()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientLifecycleEvents()"""
        val = __ClientLifecycleEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.api.events.RenderEvents as __RenderEvents_RenderOverlay
__RenderOverlay = __RenderEvents_RenderOverlay.RenderOverlay
from abc import abstractmethod, ABC
 
class RenderOverlay(ABC):
    """dev.ultreon.quantum.client.api.events.RenderEvents.RenderOverlay"""
 
    @staticmethod
    def __wrap(java_value: __RenderOverlay) -> 'RenderOverlay':
        return RenderOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderOverlay):
        """
        Dynamic initializer for RenderOverlay.
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
    def onRenderOverlay(self, arg0: 'Renderer', arg1: float):
        """public abstract void dev.ultreon.quantum.client.api.events.RenderEvents$RenderOverlay.onRenderOverlay(dev.ultreon.quantum.client.gui.Renderer,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as __ClientPlayerEvents_PlayerLeft
__PlayerLeft = __ClientPlayerEvents_PlayerLeft.PlayerLeft
try:
    from pyquantum.client import player
except ImportError:
    player = __import_once__("pyquantum.client.player")

from abc import abstractmethod, ABC
 
class PlayerLeft(ABC):
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PlayerLeft"""
 
    @staticmethod
    def __wrap(java_value: __PlayerLeft) -> 'PlayerLeft':
        return PlayerLeft(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerLeft):
        """
        Dynamic initializer for PlayerLeft.
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
    def onPlayerLeft(self, arg0: 'ClientPlayer', arg1: str):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft.onPlayerLeft(dev.ultreon.quantum.client.player.ClientPlayer,java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientPlayerEvents
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientPlayerEvents as __ClientPlayerEvents
__ClientPlayerEvents = __ClientPlayerEvents
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientPlayerEvents():
    """dev.ultreon.quantum.client.api.events.ClientPlayerEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientPlayerEvents) -> 'ClientPlayerEvents':
        return ClientPlayerEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientPlayerEvents):
        """
        Dynamic initializer for ClientPlayerEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerLeft> dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PLAYER_LEFT
    PLAYER_LEFT: 'api.Event' = __wrap(__api.Event.PLAYER_LEFT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientPlayerEvents$PlayerJoined> dev.ultreon.quantum.client.api.events.ClientPlayerEvents.PLAYER_JOINED
    PLAYER_JOINED: 'api.Event' = __wrap(__api.Event.PLAYER_JOINED)


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
        """public dev.ultreon.quantum.client.api.events.ClientPlayerEvents()"""
        val = __ClientPlayerEvents()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientPlayerEvents()"""
        val = __ClientPlayerEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowMoved
__WindowMoved = __WindowEvents_WindowMoved.WindowMoved
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
 
class WindowMoved(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowMoved"""
 
    @staticmethod
    def __wrap(java_value: __WindowMoved) -> 'WindowMoved':
        return WindowMoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowMoved):
        """
        Dynamic initializer for WindowMoved.
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
    def onWindowMoved(self, arg0: 'GameWindow', arg1: int, arg2: int):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowMoved.onWindowMoved(dev.ultreon.quantum.GameWindow,int,int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.ClientLifecycleEvents as __ClientLifecycleEvents_WindowClosed
__WindowClosed = __ClientLifecycleEvents_WindowClosed.WindowClosed
 
class WindowClosed(ABC):
    """dev.ultreon.quantum.client.api.events.ClientLifecycleEvents.WindowClosed"""
 
    @staticmethod
    def __wrap(java_value: __WindowClosed) -> 'WindowClosed':
        return WindowClosed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowClosed):
        """
        Dynamic initializer for WindowClosed.
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
    def onWindowClose(self, ):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientLifecycleEvents$WindowClosed.onWindowClose()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as __ClientChunkEvents_Received
__Received = __ClientChunkEvents_Received.Received
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class Received(ABC):
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Received"""
 
    @staticmethod
    def __wrap(java_value: __Received) -> 'Received':
        return Received(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Received):
        """
        Dynamic initializer for Received.
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
    def onClientChunkReceived(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received.onClientChunkReceived(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as __ClientReloadEvent
__ClientReloadEvent = __ClientReloadEvent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientReloadEvent():
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent"""
 
    @staticmethod
    def __wrap(java_value: __ClientReloadEvent) -> 'ClientReloadEvent':
        return ClientReloadEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientReloadEvent):
        """
        Dynamic initializer for ClientReloadEvent.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded> dev.ultreon.quantum.client.api.events.ClientReloadEvent.SKIN_LOADED
    SKIN_LOADED: 'api.Event' = __wrap(__api.Event.SKIN_LOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinReload> dev.ultreon.quantum.client.api.events.ClientReloadEvent.SKIN_RELOAD
    SKIN_RELOAD: 'api.Event' = __wrap(__api.Event.SKIN_RELOAD)


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
        """public dev.ultreon.quantum.client.api.events.ClientReloadEvent()"""
        val = __ClientReloadEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientReloadEvent()"""
        val = __ClientReloadEvent()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientReloadEvent as __ClientReloadEvent_SkinLoaded
__SkinLoaded = __ClientReloadEvent_SkinLoaded.SkinLoaded
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

 
class SkinLoaded(ABC):
    """dev.ultreon.quantum.client.api.events.ClientReloadEvent.SkinLoaded"""
 
    @staticmethod
    def __wrap(java_value: __SkinLoaded) -> 'SkinLoaded':
        return SkinLoaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkinLoaded):
        """
        Dynamic initializer for SkinLoaded.
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
    def onSkinLoaded(self, arg0: 'Texture', arg1: 'Pixmap'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientReloadEvent$SkinLoaded.onSkinLoaded(com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Pixmap)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowFilesDropped
__WindowFilesDropped = __WindowEvents_WindowFilesDropped.WindowFilesDropped
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
 
class WindowFilesDropped(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowFilesDropped"""
 
    @staticmethod
    def __wrap(java_value: __WindowFilesDropped) -> 'WindowFilesDropped':
        return WindowFilesDropped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowFilesDropped):
        """
        Dynamic initializer for WindowFilesDropped.
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
    def onWindowFilesDropped(self, arg0: 'GameWindow', arg1: 'String'):
        """public abstract void dev.ultreon.quantum.client.api.events.WindowEvents$WindowFilesDropped.onWindowFilesDropped(dev.ultreon.quantum.GameWindow,java.lang.String[])"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents
__ClientTickEvents = __ClientTickEvents
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientTickEvents():
    """dev.ultreon.quantum.client.api.events.ClientTickEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientTickEvents) -> 'ClientTickEvents':
        return ClientTickEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientTickEvents):
        """
        Dynamic initializer for ClientTickEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PreGameTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_GAME_TICK
    PRE_GAME_TICK: 'api.Event' = __wrap(__api.Event.PRE_GAME_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_WORLD_TICK
    PRE_WORLD_TICK: 'api.Event' = __wrap(__api.Event.PRE_WORLD_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostGameTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_GAME_TICK
    POST_GAME_TICK: 'api.Event' = __wrap(__api.Event.POST_GAME_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostWorldTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_WORLD_TICK
    POST_WORLD_TICK: 'api.Event' = __wrap(__api.Event.POST_WORLD_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PostPlayerTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.POST_PLAYER_TICK
    POST_PLAYER_TICK: 'api.Event' = __wrap(__api.Event.POST_PLAYER_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientTickEvents$PrePlayerTick> dev.ultreon.quantum.client.api.events.ClientTickEvents.PRE_PLAYER_TICK
    PRE_PLAYER_TICK: 'api.Event' = __wrap(__api.Event.PRE_PLAYER_TICK)


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
        """public dev.ultreon.quantum.client.api.events.ClientTickEvents()"""
        val = __ClientTickEvents()
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
        """public dev.ultreon.quantum.client.api.events.ClientTickEvents()"""
        val = __ClientTickEvents()
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
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as __ClientChunkEvents_Rebuilt
__Rebuilt = __ClientChunkEvents_Rebuilt.Rebuilt
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

from abc import abstractmethod, ABC
 
class Rebuilt(ABC):
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents.Rebuilt"""
 
    @staticmethod
    def __wrap(java_value: __Rebuilt) -> 'Rebuilt':
        return Rebuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rebuilt):
        """
        Dynamic initializer for Rebuilt.
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
    def onClientChunkRebuilt(self, arg0: 'ClientChunk'):
        """public abstract void dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt.onClientChunkRebuilt(dev.ultreon.quantum.client.world.ClientChunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested
from pyquantum_helper import import_once as __import_once__
try:
    import pyquantum
except ImportError:
    pyquantum = __import_once__("pyquantum")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.api.events.WindowEvents as __WindowEvents_WindowCloseRequested
__WindowCloseRequested = __WindowEvents_WindowCloseRequested.WindowCloseRequested
 
class WindowCloseRequested(ABC):
    """dev.ultreon.quantum.client.api.events.WindowEvents.WindowCloseRequested"""
 
    @staticmethod
    def __wrap(java_value: __WindowCloseRequested) -> 'WindowCloseRequested':
        return WindowCloseRequested(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowCloseRequested):
        """
        Dynamic initializer for WindowCloseRequested.
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
    def onWindowCloseRequested(self, arg0: 'GameWindow'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.WindowEvents$WindowCloseRequested.onWindowCloseRequested(dev.ultreon.quantum.GameWindow)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import dev.ultreon.quantum.client.api.events.ClientTickEvents as __ClientTickEvents_PreWorldTick
__PreWorldTick = __ClientTickEvents_PreWorldTick.PreWorldTick
from abc import abstractmethod, ABC
 
class PreWorldTick(ABC):
    """dev.ultreon.quantum.client.api.events.ClientTickEvents.PreWorldTick"""
 
    @staticmethod
    def __wrap(java_value: __PreWorldTick) -> 'PreWorldTick':
        return PreWorldTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PreWorldTick):
        """
        Dynamic initializer for PreWorldTick.
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
    def onWorldTick(self, arg0: 'ClientWorld'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.client.api.events.ClientTickEvents$PreWorldTick.onWorldTick(dev.ultreon.quantum.client.world.ClientWorld)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.api.events.ClientChunkEvents
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
import dev.ultreon.quantum.client.api.events.ClientChunkEvents as __ClientChunkEvents
__ClientChunkEvents = __ClientChunkEvents
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientChunkEvents():
    """dev.ultreon.quantum.client.api.events.ClientChunkEvents"""
 
    @staticmethod
    def __wrap(java_value: __ClientChunkEvents) -> 'ClientChunkEvents':
        return ClientChunkEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientChunkEvents):
        """
        Dynamic initializer for ClientChunkEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt> dev.ultreon.quantum.client.api.events.ClientChunkEvents.REBUILT
    REBUILT: 'api.Event' = __wrap(__api.Event.REBUILT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Rebuilt> dev.ultreon.quantum.client.api.events.ClientChunkEvents.BUILT
    BUILT: 'api.Event' = __wrap(__api.Event.BUILT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.client.api.events.ClientChunkEvents$Received> dev.ultreon.quantum.client.api.events.ClientChunkEvents.RECEIVED
    RECEIVED: 'api.Event' = __wrap(__api.Event.RECEIVED)


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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.api.events.ClientChunkEvents()"""
        val = __ClientChunkEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.api.events.ClientChunkEvents()"""
        val = __ClientChunkEvents()
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