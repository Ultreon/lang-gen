from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import dev.ultreon.quantum.events.LoadingEvent as _LoadingEvent_RecipeState
_RecipeState = _LoadingEvent_RecipeState.RecipeState
from abc import abstractmethod, ABC
 
class RecipeState():
    """dev.ultreon.quantum.events.LoadingEvent.RecipeState"""
 
    @staticmethod
    def _wrap(java_value: _RecipeState) -> 'RecipeState':
        return RecipeState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeState):
        """
        Dynamic initializer for RecipeState.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeState__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeState__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRecipeState(self, arg0: 'RecipeManager'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RecipeState.onRecipeState(dev.ultreon.quantum.recipe.RecipeManager)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RecipeState
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import dev.ultreon.quantum.events.LoadingEvent as _LoadingEvent_RecipeState
_RecipeState = _LoadingEvent_RecipeState.RecipeState
from abc import abstractmethod, ABC
 
class RecipeState():
    """dev.ultreon.quantum.events.LoadingEvent.RecipeState"""
 
    @staticmethod
    def _wrap(java_value: _RecipeState) -> 'RecipeState':
        return RecipeState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeState):
        """
        Dynamic initializer for RecipeState.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeState__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeState__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRecipeState(self, arg0: 'RecipeManager'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RecipeState.onRecipeState(dev.ultreon.quantum.recipe.RecipeManager)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RecipeState 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BlockPlaced
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_BlockPlaced
_BlockPlaced = _BlockEvents_BlockPlaced.BlockPlaced
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class BlockPlaced():
    """dev.ultreon.quantum.events.BlockEvents.BlockPlaced"""
 
    @staticmethod
    def _wrap(java_value: _BlockPlaced) -> 'BlockPlaced':
        return BlockPlaced(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockPlaced):
        """
        Dynamic initializer for BlockPlaced.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockPlaced__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockPlaced__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onBlockPlaced(self, arg0: 'Player', arg1: 'Block', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$BlockPlaced.onBlockPlaced(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_ChunkUnloaded
_ChunkUnloaded = _WorldEvents_ChunkUnloaded.ChunkUnloaded
 
class ChunkUnloaded():
    """dev.ultreon.quantum.events.WorldEvents.ChunkUnloaded"""
 
    @staticmethod
    def _wrap(java_value: _ChunkUnloaded) -> 'ChunkUnloaded':
        return ChunkUnloaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkUnloaded):
        """
        Dynamic initializer for ChunkUnloaded.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkUnloaded__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkUnloaded__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onChunkUnloaded(self, arg0: 'World', arg1: 'ChunkPos', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded.onChunkUnloaded(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadChunk
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_LoadChunk
_LoadChunk = _WorldEvents_LoadChunk.LoadChunk
from abc import abstractmethod, ABC
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class LoadChunk():
    """dev.ultreon.quantum.events.WorldEvents.LoadChunk"""
 
    @staticmethod
    def _wrap(java_value: _LoadChunk) -> 'LoadChunk':
        return LoadChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadChunk):
        """
        Dynamic initializer for LoadChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onLoadChunk(self, arg0: 'Chunk', arg1: 'MapType'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadChunk.onLoadChunk(dev.ultreon.quantum.world.Chunk,dev.ultreon.ubo.types.MapType)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkBuilt
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_ChunkBuilt
_ChunkBuilt = _WorldEvents_ChunkBuilt.ChunkBuilt
from abc import abstractmethod, ABC
 
class ChunkBuilt():
    """dev.ultreon.quantum.events.WorldEvents.ChunkBuilt"""
 
    @staticmethod
    def _wrap(java_value: _ChunkBuilt) -> 'ChunkBuilt':
        return ChunkBuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkBuilt):
        """
        Dynamic initializer for ChunkBuilt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkBuilt__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkBuilt__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onChunkGenerated(self, arg0: 'World', arg1: 'Region', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkBuilt.onChunkGenerated(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadWorld
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_LoadWorld
_LoadWorld = _WorldEvents_LoadWorld.LoadWorld
from abc import abstractmethod, ABC
 
class LoadWorld():
    """dev.ultreon.quantum.events.WorldEvents.LoadWorld"""
 
    @staticmethod
    def _wrap(java_value: _LoadWorld) -> 'LoadWorld':
        return LoadWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadWorld):
        """
        Dynamic initializer for LoadWorld.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadWorld__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadWorld__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onLoadWorld(self, arg0: 'World', arg1: 'WorldStorage'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadWorld.onLoadWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.WorldStorage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ConfigEvents
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.events import api
except ImportError:
    api = _import_once("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.events.ConfigEvents as _ConfigEvents
_ConfigEvents = _ConfigEvents
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
 
class ConfigEvents():
    """dev.ultreon.quantum.events.ConfigEvents"""
 
    @staticmethod
    def _wrap(java_value: _ConfigEvents) -> 'ConfigEvents':
        return ConfigEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigEvents):
        """
        Dynamic initializer for ConfigEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ConfigEvents$Load> dev.ultreon.quantum.events.ConfigEvents.LOAD
    LOAD: 'api.Event' = _wrap(_api.Event.LOAD)


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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.ConfigEvents()"""
        val = _ConfigEvents()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.ConfigEvents()"""
        val = _ConfigEvents()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RegisterCommands
import dev.ultreon.quantum.events.LoadingEvent as _LoadingEvent_RegisterCommands
_RegisterCommands = _LoadingEvent_RegisterCommands.RegisterCommands
from abc import abstractmethod, ABC
 
class RegisterCommands():
    """dev.ultreon.quantum.events.LoadingEvent.RegisterCommands"""
 
    @staticmethod
    def _wrap(java_value: _RegisterCommands) -> 'RegisterCommands':
        return RegisterCommands(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegisterCommands):
        """
        Dynamic initializer for RegisterCommands.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegisterCommands__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegisterCommands__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onRegisterCommands(self, ):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RegisterCommands.onRegisterCommands()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_AttemptBlockRemoval
_AttemptBlockRemoval = _BlockEvents_AttemptBlockRemoval.AttemptBlockRemoval
from abc import abstractmethod, ABC
 
class AttemptBlockRemoval():
    """dev.ultreon.quantum.events.BlockEvents.AttemptBlockRemoval"""
 
    @staticmethod
    def _wrap(java_value: _AttemptBlockRemoval) -> 'AttemptBlockRemoval':
        return AttemptBlockRemoval(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AttemptBlockRemoval):
        """
        Dynamic initializer for AttemptBlockRemoval.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AttemptBlockRemoval__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AttemptBlockRemoval__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onAttemptBlockRemoval(self, arg0: 'ServerPlayer', arg1: 'BlockProperties', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval.onAttemptBlockRemoval(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents
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
import dev.ultreon.quantum.events.BlockEvents as _BlockEvents
_BlockEvents = _BlockEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockEvents():
    """dev.ultreon.quantum.events.BlockEvents"""
 
    @staticmethod
    def _wrap(java_value: _BlockEvents) -> 'BlockEvents':
        return BlockEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockEvents):
        """
        Dynamic initializer for BlockEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$SetBlock> dev.ultreon.quantum.events.BlockEvents.SET_BLOCK
    SET_BLOCK: 'api.Event' = _wrap(_api.Event.SET_BLOCK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement> dev.ultreon.quantum.events.BlockEvents.ATTEMPT_BLOCK_PLACEMENT
    ATTEMPT_BLOCK_PLACEMENT: 'api.Event' = _wrap(_api.Event.ATTEMPT_BLOCK_PLACEMENT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BreakBlock> dev.ultreon.quantum.events.BlockEvents.BREAK_BLOCK
    BREAK_BLOCK: 'api.Event' = _wrap(_api.Event.BREAK_BLOCK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval> dev.ultreon.quantum.events.BlockEvents.ATTEMPT_BLOCK_REMOVAL
    ATTEMPT_BLOCK_REMOVAL: 'api.Event' = _wrap(_api.Event.ATTEMPT_BLOCK_REMOVAL)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BlockPlaced> dev.ultreon.quantum.events.BlockEvents.BLOCK_PLACED
    BLOCK_PLACED: 'api.Event' = _wrap(_api.Event.BLOCK_PLACED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BlockRemoved> dev.ultreon.quantum.events.BlockEvents.BLOCK_REMOVED
    BLOCK_REMOVED: 'api.Event' = _wrap(_api.Event.BLOCK_REMOVED)


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
        """public dev.ultreon.quantum.events.BlockEvents()"""
        val = _BlockEvents()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.BlockEvents()"""
        val = _BlockEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveRegion
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_SaveRegion
_SaveRegion = _WorldEvents_SaveRegion.SaveRegion
from abc import abstractmethod, ABC
 
class SaveRegion():
    """dev.ultreon.quantum.events.WorldEvents.SaveRegion"""
 
    @staticmethod
    def _wrap(java_value: _SaveRegion) -> 'SaveRegion':
        return SaveRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SaveRegion):
        """
        Dynamic initializer for SaveRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SaveRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SaveRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSaveRegion(self, arg0: 'World', arg1: 'Region'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveRegion.onSaveRegion(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_AttemptBlockPlacement
_AttemptBlockPlacement = _BlockEvents_AttemptBlockPlacement.AttemptBlockPlacement
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class AttemptBlockPlacement():
    """dev.ultreon.quantum.events.BlockEvents.AttemptBlockPlacement"""
 
    @staticmethod
    def _wrap(java_value: _AttemptBlockPlacement) -> 'AttemptBlockPlacement':
        return AttemptBlockPlacement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AttemptBlockPlacement):
        """
        Dynamic initializer for AttemptBlockPlacement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AttemptBlockPlacement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AttemptBlockPlacement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onAttemptBlockPlacement(self, arg0: 'Player', arg1: 'Block', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement.onAttemptBlockPlacement(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ConfigEvents$Load
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.events.ConfigEvents as _ConfigEvents_Load
_Load = _ConfigEvents_Load.Load
from abc import abstractmethod, ABC
 
class Load():
    """dev.ultreon.quantum.events.ConfigEvents.Load"""
 
    @staticmethod
    def _wrap(java_value: _Load) -> 'Load':
        return Load(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Load):
        """
        Dynamic initializer for Load.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Load__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Load__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onConfigLoad(self, arg0: 'Env'):
        """public abstract void dev.ultreon.quantum.events.ConfigEvents$Load.onConfigLoad(dev.ultreon.quantum.util.Env)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ResourceEvent
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
from builtins import bool
import dev.ultreon.quantum.events.ResourceEvent as _ResourceEvent
_ResourceEvent = _ResourceEvent
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceEvent():
    """dev.ultreon.quantum.events.ResourceEvent"""
 
    @staticmethod
    def _wrap(java_value: _ResourceEvent) -> 'ResourceEvent':
        return ResourceEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceEvent):
        """
        Dynamic initializer for ResourceEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ResourceEvent$PackageImported> dev.ultreon.quantum.events.ResourceEvent.IMPORTED
    IMPORTED: 'api.Event' = _wrap(_api.Event.IMPORTED)


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
        """public dev.ultreon.quantum.events.ResourceEvent()"""
        val = _ResourceEvent()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.ResourceEvent()"""
        val = _ResourceEvent()
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
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents
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
import dev.ultreon.quantum.events.ItemEvents as _ItemEvents
_ItemEvents = _ItemEvents
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemEvents():
    """dev.ultreon.quantum.events.ItemEvents"""
 
    @staticmethod
    def _wrap(java_value: _ItemEvents) -> 'ItemEvents':
        return ItemEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemEvents):
        """
        Dynamic initializer for ItemEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ItemEvents$Dropped> dev.ultreon.quantum.events.ItemEvents.DROPPED
    DROPPED: 'api.Event' = _wrap(_api.Event.DROPPED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ItemEvents$Use> dev.ultreon.quantum.events.ItemEvents.USE
    USE: 'api.Event' = _wrap(_api.Event.USE)


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
        """public dev.ultreon.quantum.events.ItemEvents()"""
        val = _ItemEvents()
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
        """public dev.ultreon.quantum.events.ItemEvents()"""
        val = _ItemEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkLoaded
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_ChunkLoaded
_ChunkLoaded = _WorldEvents_ChunkLoaded.ChunkLoaded
from abc import abstractmethod, ABC
 
class ChunkLoaded():
    """dev.ultreon.quantum.events.WorldEvents.ChunkLoaded"""
 
    @staticmethod
    def _wrap(java_value: _ChunkLoaded) -> 'ChunkLoaded':
        return ChunkLoaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkLoaded):
        """
        Dynamic initializer for ChunkLoaded.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkLoaded__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkLoaded__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onChunkLoaded(self, arg0: 'World', arg1: 'ChunkPos', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkLoaded.onChunkLoaded(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents
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
import dev.ultreon.quantum.events.EntityEvents as _EntityEvents
_EntityEvents = _EntityEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityEvents():
    """dev.ultreon.quantum.events.EntityEvents"""
 
    @staticmethod
    def _wrap(java_value: _EntityEvents) -> 'EntityEvents':
        return EntityEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityEvents):
        """
        Dynamic initializer for EntityEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Death> dev.ultreon.quantum.events.EntityEvents.DEATH
    DEATH: 'api.Event' = _wrap(_api.Event.DEATH)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Move> dev.ultreon.quantum.events.EntityEvents.MOVE
    MOVE: 'api.Event' = _wrap(_api.Event.MOVE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Removed> dev.ultreon.quantum.events.EntityEvents.REMOVED
    REMOVED: 'api.Event' = _wrap(_api.Event.REMOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Damage> dev.ultreon.quantum.events.EntityEvents.DAMAGE
    DAMAGE: 'api.Event' = _wrap(_api.Event.DAMAGE)


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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.EntityEvents()"""
        val = _EntityEvents()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.EntityEvents()"""
        val = _EntityEvents()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.LoadingEvent as _LoadingEvent_ModifyRecipes
_ModifyRecipes = _LoadingEvent_ModifyRecipes.ModifyRecipes
 
class ModifyRecipes():
    """dev.ultreon.quantum.events.LoadingEvent.ModifyRecipes"""
 
    @staticmethod
    def _wrap(java_value: _ModifyRecipes) -> 'ModifyRecipes':
        return ModifyRecipes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModifyRecipes):
        """
        Dynamic initializer for ModifyRecipes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModifyRecipes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModifyRecipes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onModifyRecipes(self, arg0: 'RecipeManager', arg1: 'RecipeType', arg2: 'RecipeRegistry'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes.onModifyRecipes(dev.ultreon.quantum.recipe.RecipeManager,dev.ultreon.quantum.recipe.RecipeType,dev.ultreon.quantum.recipe.RecipeRegistry<dev.ultreon.quantum.recipe.Recipe>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ResourceEvent$PackageImported
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.ResourceEvent as _ResourceEvent_PackageImported
_PackageImported = _ResourceEvent_PackageImported.PackageImported
 
class PackageImported():
    """dev.ultreon.quantum.events.ResourceEvent.PackageImported"""
 
    @staticmethod
    def _wrap(java_value: _PackageImported) -> 'PackageImported':
        return PackageImported(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PackageImported):
        """
        Dynamic initializer for PackageImported.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PackageImported__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PackageImported__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onImported(self, arg0: 'ResourcePackage'):
        """public abstract void dev.ultreon.quantum.events.ResourceEvent$PackageImported.onImported(dev.ultreon.quantum.resources.ResourcePackage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Death
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.EntityEvents as _EntityEvents_Death
_Death = _EntityEvents_Death.Death
 
class Death():
    """dev.ultreon.quantum.events.EntityEvents.Death"""
 
    @staticmethod
    def _wrap(java_value: _Death) -> 'Death':
        return Death(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Death):
        """
        Dynamic initializer for Death.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Death__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Death__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onEntityDeath(self, arg0: 'LivingEntity', arg1: 'DamageSource'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.EntityEvents$Death.onEntityDeath(dev.ultreon.quantum.entity.LivingEntity,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BreakBlock
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_BreakBlock
_BreakBlock = _BlockEvents_BreakBlock.BreakBlock
from abc import abstractmethod, ABC
 
class BreakBlock():
    """dev.ultreon.quantum.events.BlockEvents.BreakBlock"""
 
    @staticmethod
    def _wrap(java_value: _BreakBlock) -> 'BreakBlock':
        return BreakBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BreakBlock):
        """
        Dynamic initializer for BreakBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BreakBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BreakBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onBreakBlock(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$BreakBlock.onBreakBlock(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldLifecycleEvents
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.WorldLifecycleEvents as _WorldLifecycleEvents
_WorldLifecycleEvents = _WorldLifecycleEvents
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldLifecycleEvents():
    """dev.ultreon.quantum.events.WorldLifecycleEvents"""
 
    @staticmethod
    def _wrap(java_value: _WorldLifecycleEvents) -> 'WorldLifecycleEvents':
        return WorldLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldLifecycleEvents):
        """
        Dynamic initializer for WorldLifecycleEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldLifecycleEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldLifecycleEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt> dev.ultreon.quantum.events.WorldLifecycleEvents.BIOME_LAYERS_BUILT
    BIOME_LAYERS_BUILT: 'api.Event' = _wrap(_api.Event.BIOME_LAYERS_BUILT)


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
        """public dev.ultreon.quantum.events.WorldLifecycleEvents()"""
        val = _WorldLifecycleEvents()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.WorldLifecycleEvents()"""
        val = _WorldLifecycleEvents()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$PostTick
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_PostTick
_PostTick = _WorldEvents_PostTick.PostTick
from abc import abstractmethod, ABC
 
class PostTick():
    """dev.ultreon.quantum.events.WorldEvents.PostTick"""
 
    @staticmethod
    def _wrap(java_value: _PostTick) -> 'PostTick':
        return PostTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PostTick):
        """
        Dynamic initializer for PostTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PostTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PostTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPostTick(self, arg0: 'World'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$PostTick.onPostTick(dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveChunk
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_SaveChunk
_SaveChunk = _WorldEvents_SaveChunk.SaveChunk
from abc import abstractmethod, ABC
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class SaveChunk():
    """dev.ultreon.quantum.events.WorldEvents.SaveChunk"""
 
    @staticmethod
    def _wrap(java_value: _SaveChunk) -> 'SaveChunk':
        return SaveChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SaveChunk):
        """
        Dynamic initializer for SaveChunk.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SaveChunk__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SaveChunk__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSaveChunk(self, arg0: 'Chunk', arg1: 'MapType'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveChunk.onSaveChunk(dev.ultreon.quantum.world.Chunk,dev.ultreon.ubo.types.MapType)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuClickEvent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.events.MenuEvents as _MenuEvents_MenuClickEvent
_MenuClickEvent = _MenuEvents_MenuClickEvent.MenuClickEvent
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class MenuClickEvent():
    """dev.ultreon.quantum.events.MenuEvents.MenuClickEvent"""
 
    @staticmethod
    def _wrap(java_value: _MenuClickEvent) -> 'MenuClickEvent':
        return MenuClickEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuClickEvent):
        """
        Dynamic initializer for MenuClickEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuClickEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuClickEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMenuClick(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer', arg2: 'ItemSlot', arg3: bool):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.MenuEvents$MenuClickEvent.onMenuClick(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.ItemSlot,boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$CreateBiome
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_CreateBiome
_CreateBiome = _WorldEvents_CreateBiome.CreateBiome
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = _import_once("pyquantum.world.gen.noise")

from abc import abstractmethod, ABC
import java.util.List as List
 
class CreateBiome():
    """dev.ultreon.quantum.events.WorldEvents.CreateBiome"""
 
    @staticmethod
    def _wrap(java_value: _CreateBiome) -> 'CreateBiome':
        return CreateBiome(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CreateBiome):
        """
        Dynamic initializer for CreateBiome.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CreateBiome__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CreateBiome__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onCreateBiome(self, arg0: 'World', arg1: 'DomainWarping', arg2: 'List', arg3: 'List'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$CreateBiome.onCreateBiome(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.gen.noise.DomainWarping,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadRegion
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_LoadRegion
_LoadRegion = _WorldEvents_LoadRegion.LoadRegion
from abc import abstractmethod, ABC
 
class LoadRegion():
    """dev.ultreon.quantum.events.WorldEvents.LoadRegion"""
 
    @staticmethod
    def _wrap(java_value: _LoadRegion) -> 'LoadRegion':
        return LoadRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadRegion):
        """
        Dynamic initializer for LoadRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onLoadRegion(self, arg0: 'World', arg1: 'Region'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadRegion.onLoadRegion(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents
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
import dev.ultreon.quantum.events.MenuEvents as _MenuEvents
_MenuEvents = _MenuEvents
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MenuEvents():
    """dev.ultreon.quantum.events.MenuEvents"""
 
    @staticmethod
    def _wrap(java_value: _MenuEvents) -> 'MenuEvents':
        return MenuEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuEvents):
        """
        Dynamic initializer for MenuEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuClickEvent> dev.ultreon.quantum.events.MenuEvents.MENU_CLICK
    MENU_CLICK: 'api.Event' = _wrap(_api.Event.MENU_CLICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent> dev.ultreon.quantum.events.MenuEvents.MENU_OPEN
    MENU_OPEN: 'api.Event' = _wrap(_api.Event.MENU_OPEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent> dev.ultreon.quantum.events.MenuEvents.MENU_CLOSE
    MENU_CLOSE: 'api.Event' = _wrap(_api.Event.MENU_CLOSE)


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
        """public dev.ultreon.quantum.events.MenuEvents()"""
        val = _MenuEvents()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.MenuEvents()"""
        val = _MenuEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Move
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.events.EntityEvents as _EntityEvents_Move
_Move = _EntityEvents_Move.Move
from abc import abstractmethod, ABC
 
class Move():
    """dev.ultreon.quantum.events.EntityEvents.Move"""
 
    @staticmethod
    def _wrap(java_value: _Move) -> 'Move':
        return Move(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Move):
        """
        Dynamic initializer for Move.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Move__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Move__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onEntityMove(self, arg0: 'Entity', arg1: float, arg2: float, arg3: float):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.events.EntityEvents$Move.onEntityMove(dev.ultreon.quantum.entity.Entity,double,double,double)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Spawned
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.PlayerEvents as _PlayerEvents_Spawned
_Spawned = _PlayerEvents_Spawned.Spawned
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from abc import abstractmethod, ABC
 
class Spawned():
    """dev.ultreon.quantum.events.PlayerEvents.Spawned"""
 
    @staticmethod
    def _wrap(java_value: _Spawned) -> 'Spawned':
        return Spawned(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Spawned):
        """
        Dynamic initializer for Spawned.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Spawned__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Spawned__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerSpawned(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Spawned.onPlayerSpawned(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.WorldEvents as _WorldEvents
_WorldEvents = _WorldEvents
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldEvents():
    """dev.ultreon.quantum.events.WorldEvents"""
 
    @staticmethod
    def _wrap(java_value: _WorldEvents) -> 'WorldEvents':
        return WorldEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldEvents):
        """
        Dynamic initializer for WorldEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkBuilt> dev.ultreon.quantum.events.WorldEvents.CHUNK_BUILT
    CHUNK_BUILT: 'api.Event' = _wrap(_api.Event.CHUNK_BUILT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded> dev.ultreon.quantum.events.WorldEvents.CHUNK_UNLOADED
    CHUNK_UNLOADED: 'api.Event' = _wrap(_api.Event.CHUNK_UNLOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveRegion> dev.ultreon.quantum.events.WorldEvents.SAVE_REGION
    SAVE_REGION: 'api.Event' = _wrap(_api.Event.SAVE_REGION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkLoaded> dev.ultreon.quantum.events.WorldEvents.CHUNK_LOADED
    CHUNK_LOADED: 'api.Event' = _wrap(_api.Event.CHUNK_LOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$PreTick> dev.ultreon.quantum.events.WorldEvents.PRE_TICK
    PRE_TICK: 'api.Event' = _wrap(_api.Event.PRE_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$CreateBiome> dev.ultreon.quantum.events.WorldEvents.CREATE_BIOME
    CREATE_BIOME: 'api.Event' = _wrap(_api.Event.CREATE_BIOME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveWorld> dev.ultreon.quantum.events.WorldEvents.SAVE_WORLD
    SAVE_WORLD: 'api.Event' = _wrap(_api.Event.SAVE_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadWorld> dev.ultreon.quantum.events.WorldEvents.LOAD_WORLD
    LOAD_WORLD: 'api.Event' = _wrap(_api.Event.LOAD_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadRegion> dev.ultreon.quantum.events.WorldEvents.LOAD_REGION
    LOAD_REGION: 'api.Event' = _wrap(_api.Event.LOAD_REGION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadChunk> dev.ultreon.quantum.events.WorldEvents.LOAD_CHUNK
    LOAD_CHUNK: 'api.Event' = _wrap(_api.Event.LOAD_CHUNK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$PostTick> dev.ultreon.quantum.events.WorldEvents.POST_TICK
    POST_TICK: 'api.Event' = _wrap(_api.Event.POST_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveChunk> dev.ultreon.quantum.events.WorldEvents.SAVE_CHUNK
    SAVE_CHUNK: 'api.Event' = _wrap(_api.Event.SAVE_CHUNK)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.WorldEvents()"""
        val = _WorldEvents()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.WorldEvents()"""
        val = _WorldEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$InitialItems
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.events.PlayerEvents as _PlayerEvents_InitialItems
_InitialItems = _PlayerEvents_InitialItems.InitialItems
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class InitialItems():
    """dev.ultreon.quantum.events.PlayerEvents.InitialItems"""
 
    @staticmethod
    def _wrap(java_value: _InitialItems) -> 'InitialItems':
        return InitialItems(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InitialItems):
        """
        Dynamic initializer for InitialItems.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InitialItems__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InitialItems__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerInitialItems(self, arg0: 'ServerPlayer', arg1: 'Inventory'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.PlayerEvents$InitialItems.onPlayerInitialItems(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.Inventory)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Removed
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import dev.ultreon.quantum.events.EntityEvents as _EntityEvents_Removed
_Removed = _EntityEvents_Removed.Removed
from abc import abstractmethod, ABC
 
class Removed():
    """dev.ultreon.quantum.events.EntityEvents.Removed"""
 
    @staticmethod
    def _wrap(java_value: _Removed) -> 'Removed':
        return Removed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Removed):
        """
        Dynamic initializer for Removed.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Removed__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Removed__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onEntityRemoved(self, arg0: 'Entity'):
        """public abstract void dev.ultreon.quantum.events.EntityEvents$Removed.onEntityRemoved(dev.ultreon.quantum.entity.Entity)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$PreTick
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_PreTick
_PreTick = _WorldEvents_PreTick.PreTick
from abc import abstractmethod, ABC
 
class PreTick():
    """dev.ultreon.quantum.events.WorldEvents.PreTick"""
 
    @staticmethod
    def _wrap(java_value: _PreTick) -> 'PreTick':
        return PreTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PreTick):
        """
        Dynamic initializer for PreTick.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PreTick__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PreTick__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPreTick(self, arg0: 'World'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$PreTick.onPreTick(dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BlockRemoved
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_BlockRemoved
_BlockRemoved = _BlockEvents_BlockRemoved.BlockRemoved
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class BlockRemoved():
    """dev.ultreon.quantum.events.BlockEvents.BlockRemoved"""
 
    @staticmethod
    def _wrap(java_value: _BlockRemoved) -> 'BlockRemoved':
        return BlockRemoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockRemoved):
        """
        Dynamic initializer for BlockRemoved.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockRemoved__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockRemoved__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onBlockRemoved(self, arg0: 'ServerPlayer', arg1: 'BlockProperties', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$BlockRemoved.onBlockRemoved(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents$Dropped
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.events.ItemEvents as _ItemEvents_Dropped
_Dropped = _ItemEvents_Dropped.Dropped
from abc import abstractmethod, ABC
 
class Dropped():
    """dev.ultreon.quantum.events.ItemEvents.Dropped"""
 
    @staticmethod
    def _wrap(java_value: _Dropped) -> 'Dropped':
        return Dropped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Dropped):
        """
        Dynamic initializer for Dropped.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Dropped__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Dropped__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onDropped(self, arg0: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.ItemEvents$Dropped.onDropped(dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$SetBlock
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import dev.ultreon.quantum.events.BlockEvents as _BlockEvents_SetBlock
_SetBlock = _BlockEvents_SetBlock.SetBlock
from abc import abstractmethod, ABC
 
class SetBlock():
    """dev.ultreon.quantum.events.BlockEvents.SetBlock"""
 
    @staticmethod
    def _wrap(java_value: _SetBlock) -> 'SetBlock':
        return SetBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetBlock):
        """
        Dynamic initializer for SetBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSetBlock(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$SetBlock.onSetBlock(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveWorld
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as _WorldEvents_SaveWorld
_SaveWorld = _WorldEvents_SaveWorld.SaveWorld
from abc import abstractmethod, ABC
 
class SaveWorld():
    """dev.ultreon.quantum.events.WorldEvents.SaveWorld"""
 
    @staticmethod
    def _wrap(java_value: _SaveWorld) -> 'SaveWorld':
        return SaveWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SaveWorld):
        """
        Dynamic initializer for SaveWorld.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SaveWorld__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SaveWorld__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onSaveWorld(self, arg0: 'World', arg1: 'WorldStorage'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveWorld.onSaveWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.WorldStorage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.events.MenuEvents as _MenuEvents_MenuOpenEvent
_MenuOpenEvent = _MenuEvents_MenuOpenEvent.MenuOpenEvent
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class MenuOpenEvent():
    """dev.ultreon.quantum.events.MenuEvents.MenuOpenEvent"""
 
    @staticmethod
    def _wrap(java_value: _MenuOpenEvent) -> 'MenuOpenEvent':
        return MenuOpenEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuOpenEvent):
        """
        Dynamic initializer for MenuOpenEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuOpenEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuOpenEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMenuOpen(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent.onMenuOpen(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.MenuEvents as _MenuEvents_MenuCloseEvent
_MenuCloseEvent = _MenuEvents_MenuCloseEvent.MenuCloseEvent
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class MenuCloseEvent():
    """dev.ultreon.quantum.events.MenuEvents.MenuCloseEvent"""
 
    @staticmethod
    def _wrap(java_value: _MenuCloseEvent) -> 'MenuCloseEvent':
        return MenuCloseEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MenuCloseEvent):
        """
        Dynamic initializer for MenuCloseEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MenuCloseEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MenuCloseEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onMenuClose(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent.onMenuClose(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Damage
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = _import_once("pyquantum.entity.damagesource")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.EntityEvents as _EntityEvents_Damage
_Damage = _EntityEvents_Damage.Damage
 
class Damage():
    """dev.ultreon.quantum.events.EntityEvents.Damage"""
 
    @staticmethod
    def _wrap(java_value: _Damage) -> 'Damage':
        return Damage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Damage):
        """
        Dynamic initializer for Damage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Damage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Damage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onEntityDamage(self, arg0: 'LivingEntity', arg1: 'DamageSource', arg2: float):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<java.lang.Float> dev.ultreon.quantum.events.EntityEvents$Damage.onEntityDamage(dev.ultreon.quantum.entity.LivingEntity,dev.ultreon.quantum.entity.damagesource.DamageSource,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.events.WorldLifecycleEvents as _WorldLifecycleEvents_BiomeLayersBuilt
_BiomeLayersBuilt = _WorldLifecycleEvents_BiomeLayersBuilt.BiomeLayersBuilt
from abc import abstractmethod, ABC
import java.util.List as List
 
class BiomeLayersBuilt():
    """dev.ultreon.quantum.events.WorldLifecycleEvents.BiomeLayersBuilt"""
 
    @staticmethod
    def _wrap(java_value: _BiomeLayersBuilt) -> 'BiomeLayersBuilt':
        return BiomeLayersBuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiomeLayersBuilt):
        """
        Dynamic initializer for BiomeLayersBuilt.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiomeLayersBuilt__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiomeLayersBuilt__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onBiomeLayersBuilt(self, arg0: 'Biome', arg1: 'List', arg2: 'List'):
        """public abstract void dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt.onBiomeLayersBuilt(dev.ultreon.quantum.world.Biome,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Joined
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.PlayerEvents as _PlayerEvents_Joined
_Joined = _PlayerEvents_Joined.Joined
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from abc import abstractmethod, ABC
 
class Joined():
    """dev.ultreon.quantum.events.PlayerEvents.Joined"""
 
    @staticmethod
    def _wrap(java_value: _Joined) -> 'Joined':
        return Joined(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Joined):
        """
        Dynamic initializer for Joined.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Joined__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Joined__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerJoined(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Joined.onPlayerJoined(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Left
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.PlayerEvents as _PlayerEvents_Left
_Left = _PlayerEvents_Left.Left
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

from abc import abstractmethod, ABC
 
class Left():
    """dev.ultreon.quantum.events.PlayerEvents.Left"""
 
    @staticmethod
    def _wrap(java_value: _Left) -> 'Left':
        return Left(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Left):
        """
        Dynamic initializer for Left.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Left__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Left__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onPlayerLeft(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Left.onPlayerLeft(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents
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
import dev.ultreon.quantum.events.PlayerEvents as _PlayerEvents
_PlayerEvents = _PlayerEvents
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerEvents():
    """dev.ultreon.quantum.events.PlayerEvents"""
 
    @staticmethod
    def _wrap(java_value: _PlayerEvents) -> 'PlayerEvents':
        return PlayerEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerEvents):
        """
        Dynamic initializer for PlayerEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerEvents__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Joined> dev.ultreon.quantum.events.PlayerEvents.PLAYER_JOINED
    PLAYER_JOINED: 'api.Event' = _wrap(_api.Event.PLAYER_JOINED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Left> dev.ultreon.quantum.events.PlayerEvents.PLAYER_LEFT
    PLAYER_LEFT: 'api.Event' = _wrap(_api.Event.PLAYER_LEFT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Spawned> dev.ultreon.quantum.events.PlayerEvents.PLAYER_SPAWNED
    PLAYER_SPAWNED: 'api.Event' = _wrap(_api.Event.PLAYER_SPAWNED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$InitialItems> dev.ultreon.quantum.events.PlayerEvents.INITIAL_ITEMS
    INITIAL_ITEMS: 'api.Event' = _wrap(_api.Event.INITIAL_ITEMS)


    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.PlayerEvents()"""
        val = _PlayerEvents()
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
        """public dev.ultreon.quantum.events.PlayerEvents()"""
        val = _PlayerEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent
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
import dev.ultreon.quantum.events.LoadingEvent as _LoadingEvent
_LoadingEvent = _LoadingEvent
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoadingEvent():
    """dev.ultreon.quantum.events.LoadingEvent"""
 
    @staticmethod
    def _wrap(java_value: _LoadingEvent) -> 'LoadingEvent':
        return LoadingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadingEvent):
        """
        Dynamic initializer for LoadingEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadingEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadingEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RecipeState> dev.ultreon.quantum.events.LoadingEvent.LOAD_RECIPES
    LOAD_RECIPES: 'api.Event' = _wrap(_api.Event.LOAD_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes> dev.ultreon.quantum.events.LoadingEvent.MODIFY_RECIPES
    MODIFY_RECIPES: 'api.Event' = _wrap(_api.Event.MODIFY_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RecipeState> dev.ultreon.quantum.events.LoadingEvent.UNLOAD_RECIPES
    UNLOAD_RECIPES: 'api.Event' = _wrap(_api.Event.UNLOAD_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RegisterCommands> dev.ultreon.quantum.events.LoadingEvent.REGISTER_COMMANDS
    REGISTER_COMMANDS: 'api.Event' = _wrap(_api.Event.REGISTER_COMMANDS)


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
        """public dev.ultreon.quantum.events.LoadingEvent()"""
        val = _LoadingEvent()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.LoadingEvent()"""
        val = _LoadingEvent()
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
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents$Use
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.events.ItemEvents as _ItemEvents_Use
_Use = _ItemEvents_Use.Use
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from abc import abstractmethod, ABC
 
class Use():
    """dev.ultreon.quantum.events.ItemEvents.Use"""
 
    @staticmethod
    def _wrap(java_value: _Use) -> 'Use':
        return Use(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Use):
        """
        Dynamic initializer for Use.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Use__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Use__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onUseItem(self, arg0: 'Item', arg1: 'UseItemContext'):
        """public abstract void dev.ultreon.quantum.events.ItemEvents$Use.onUseItem(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.item.UseItemContext)"""
        pass