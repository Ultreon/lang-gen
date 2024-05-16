from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import dev.ultreon.quantum.events.LoadingEvent as __LoadingEvent_RecipeState
__RecipeState = __LoadingEvent_RecipeState.RecipeState
from abc import abstractmethod, ABC
 
class RecipeState(ABC):
    """dev.ultreon.quantum.events.LoadingEvent.RecipeState"""
 
    @staticmethod
    def __wrap(java_value: __RecipeState) -> 'RecipeState':
        return RecipeState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeState):
        """
        Dynamic initializer for RecipeState.
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
    def onRecipeState(self, arg0: 'RecipeManager'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RecipeState.onRecipeState(dev.ultreon.quantum.recipe.RecipeManager)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RecipeState
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import dev.ultreon.quantum.events.LoadingEvent as __LoadingEvent_RecipeState
__RecipeState = __LoadingEvent_RecipeState.RecipeState
from abc import abstractmethod, ABC
 
class RecipeState(ABC):
    """dev.ultreon.quantum.events.LoadingEvent.RecipeState"""
 
    @staticmethod
    def __wrap(java_value: __RecipeState) -> 'RecipeState':
        return RecipeState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeState):
        """
        Dynamic initializer for RecipeState.
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
    def onRecipeState(self, arg0: 'RecipeManager'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RecipeState.onRecipeState(dev.ultreon.quantum.recipe.RecipeManager)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RecipeState 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BlockPlaced
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_BlockPlaced
__BlockPlaced = __BlockEvents_BlockPlaced.BlockPlaced
 
class BlockPlaced(ABC):
    """dev.ultreon.quantum.events.BlockEvents.BlockPlaced"""
 
    @staticmethod
    def __wrap(java_value: __BlockPlaced) -> 'BlockPlaced':
        return BlockPlaced(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockPlaced):
        """
        Dynamic initializer for BlockPlaced.
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
    def onBlockPlaced(self, arg0: 'Player', arg1: 'Block', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$BlockPlaced.onBlockPlaced(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_ChunkUnloaded
__ChunkUnloaded = __WorldEvents_ChunkUnloaded.ChunkUnloaded
from abc import abstractmethod, ABC
 
class ChunkUnloaded(ABC):
    """dev.ultreon.quantum.events.WorldEvents.ChunkUnloaded"""
 
    @staticmethod
    def __wrap(java_value: __ChunkUnloaded) -> 'ChunkUnloaded':
        return ChunkUnloaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkUnloaded):
        """
        Dynamic initializer for ChunkUnloaded.
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
    def onChunkUnloaded(self, arg0: 'World', arg1: 'ChunkPos', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded.onChunkUnloaded(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadChunk
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_LoadChunk
__LoadChunk = __WorldEvents_LoadChunk.LoadChunk
from abc import abstractmethod, ABC
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class LoadChunk(ABC):
    """dev.ultreon.quantum.events.WorldEvents.LoadChunk"""
 
    @staticmethod
    def __wrap(java_value: __LoadChunk) -> 'LoadChunk':
        return LoadChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadChunk):
        """
        Dynamic initializer for LoadChunk.
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
    def onLoadChunk(self, arg0: 'Chunk', arg1: 'MapType'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadChunk.onLoadChunk(dev.ultreon.quantum.world.Chunk,dev.ultreon.ubo.types.MapType)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkBuilt
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_ChunkBuilt
__ChunkBuilt = __WorldEvents_ChunkBuilt.ChunkBuilt
from abc import abstractmethod, ABC
 
class ChunkBuilt(ABC):
    """dev.ultreon.quantum.events.WorldEvents.ChunkBuilt"""
 
    @staticmethod
    def __wrap(java_value: __ChunkBuilt) -> 'ChunkBuilt':
        return ChunkBuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkBuilt):
        """
        Dynamic initializer for ChunkBuilt.
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
    def onChunkGenerated(self, arg0: 'World', arg1: 'Region', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkBuilt.onChunkGenerated(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadWorld
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_LoadWorld
__LoadWorld = __WorldEvents_LoadWorld.LoadWorld
from abc import abstractmethod, ABC
 
class LoadWorld(ABC):
    """dev.ultreon.quantum.events.WorldEvents.LoadWorld"""
 
    @staticmethod
    def __wrap(java_value: __LoadWorld) -> 'LoadWorld':
        return LoadWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadWorld):
        """
        Dynamic initializer for LoadWorld.
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
    def onLoadWorld(self, arg0: 'World', arg1: 'WorldStorage'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadWorld.onLoadWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.WorldStorage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ConfigEvents
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
import dev.ultreon.quantum.events.ConfigEvents as __ConfigEvents
__ConfigEvents = __ConfigEvents
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConfigEvents():
    """dev.ultreon.quantum.events.ConfigEvents"""
 
    @staticmethod
    def __wrap(java_value: __ConfigEvents) -> 'ConfigEvents':
        return ConfigEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConfigEvents):
        """
        Dynamic initializer for ConfigEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ConfigEvents$Load> dev.ultreon.quantum.events.ConfigEvents.LOAD
    LOAD: 'api.Event' = __wrap(__api.Event.LOAD)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.ConfigEvents()"""
        val = __ConfigEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.ConfigEvents()"""
        val = __ConfigEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$RegisterCommands
import dev.ultreon.quantum.events.LoadingEvent as __LoadingEvent_RegisterCommands
__RegisterCommands = __LoadingEvent_RegisterCommands.RegisterCommands
from abc import abstractmethod, ABC
 
class RegisterCommands(ABC):
    """dev.ultreon.quantum.events.LoadingEvent.RegisterCommands"""
 
    @staticmethod
    def __wrap(java_value: __RegisterCommands) -> 'RegisterCommands':
        return RegisterCommands(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegisterCommands):
        """
        Dynamic initializer for RegisterCommands.
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
    def onRegisterCommands(self, ):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$RegisterCommands.onRegisterCommands()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_AttemptBlockRemoval
__AttemptBlockRemoval = __BlockEvents_AttemptBlockRemoval.AttemptBlockRemoval
from abc import abstractmethod, ABC
 
class AttemptBlockRemoval(ABC):
    """dev.ultreon.quantum.events.BlockEvents.AttemptBlockRemoval"""
 
    @staticmethod
    def __wrap(java_value: __AttemptBlockRemoval) -> 'AttemptBlockRemoval':
        return AttemptBlockRemoval(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AttemptBlockRemoval):
        """
        Dynamic initializer for AttemptBlockRemoval.
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
    def onAttemptBlockRemoval(self, arg0: 'ServerPlayer', arg1: 'BlockProperties', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval.onAttemptBlockRemoval(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents
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
import dev.ultreon.quantum.events.BlockEvents as __BlockEvents
__BlockEvents = __BlockEvents
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockEvents():
    """dev.ultreon.quantum.events.BlockEvents"""
 
    @staticmethod
    def __wrap(java_value: __BlockEvents) -> 'BlockEvents':
        return BlockEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockEvents):
        """
        Dynamic initializer for BlockEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BlockPlaced> dev.ultreon.quantum.events.BlockEvents.BLOCK_PLACED
    BLOCK_PLACED: 'api.Event' = __wrap(__api.Event.BLOCK_PLACED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BlockRemoved> dev.ultreon.quantum.events.BlockEvents.BLOCK_REMOVED
    BLOCK_REMOVED: 'api.Event' = __wrap(__api.Event.BLOCK_REMOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$AttemptBlockRemoval> dev.ultreon.quantum.events.BlockEvents.ATTEMPT_BLOCK_REMOVAL
    ATTEMPT_BLOCK_REMOVAL: 'api.Event' = __wrap(__api.Event.ATTEMPT_BLOCK_REMOVAL)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$BreakBlock> dev.ultreon.quantum.events.BlockEvents.BREAK_BLOCK
    BREAK_BLOCK: 'api.Event' = __wrap(__api.Event.BREAK_BLOCK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement> dev.ultreon.quantum.events.BlockEvents.ATTEMPT_BLOCK_PLACEMENT
    ATTEMPT_BLOCK_PLACEMENT: 'api.Event' = __wrap(__api.Event.ATTEMPT_BLOCK_PLACEMENT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.BlockEvents$SetBlock> dev.ultreon.quantum.events.BlockEvents.SET_BLOCK
    SET_BLOCK: 'api.Event' = __wrap(__api.Event.SET_BLOCK)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.BlockEvents()"""
        val = __BlockEvents()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.events.BlockEvents()"""
        val = __BlockEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveRegion
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_SaveRegion
__SaveRegion = __WorldEvents_SaveRegion.SaveRegion
from abc import abstractmethod, ABC
 
class SaveRegion(ABC):
    """dev.ultreon.quantum.events.WorldEvents.SaveRegion"""
 
    @staticmethod
    def __wrap(java_value: __SaveRegion) -> 'SaveRegion':
        return SaveRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SaveRegion):
        """
        Dynamic initializer for SaveRegion.
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
    def onSaveRegion(self, arg0: 'World', arg1: 'Region'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveRegion.onSaveRegion(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_AttemptBlockPlacement
__AttemptBlockPlacement = __BlockEvents_AttemptBlockPlacement.AttemptBlockPlacement
from abc import abstractmethod, ABC
 
class AttemptBlockPlacement(ABC):
    """dev.ultreon.quantum.events.BlockEvents.AttemptBlockPlacement"""
 
    @staticmethod
    def __wrap(java_value: __AttemptBlockPlacement) -> 'AttemptBlockPlacement':
        return AttemptBlockPlacement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AttemptBlockPlacement):
        """
        Dynamic initializer for AttemptBlockPlacement.
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
    def onAttemptBlockPlacement(self, arg0: 'Player', arg1: 'Block', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$AttemptBlockPlacement.onAttemptBlockPlacement(dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.block.Block,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ConfigEvents$Load
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.events.ConfigEvents as __ConfigEvents_Load
__Load = __ConfigEvents_Load.Load
from abc import abstractmethod, ABC
 
class Load(ABC):
    """dev.ultreon.quantum.events.ConfigEvents.Load"""
 
    @staticmethod
    def __wrap(java_value: __Load) -> 'Load':
        return Load(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Load):
        """
        Dynamic initializer for Load.
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
    def onConfigLoad(self, arg0: 'Env'):
        """public abstract void dev.ultreon.quantum.events.ConfigEvents$Load.onConfigLoad(dev.ultreon.quantum.util.Env)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ResourceEvent
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
import dev.ultreon.quantum.events.ResourceEvent as __ResourceEvent
__ResourceEvent = __ResourceEvent
from builtins import int
 
class ResourceEvent():
    """dev.ultreon.quantum.events.ResourceEvent"""
 
    @staticmethod
    def __wrap(java_value: __ResourceEvent) -> 'ResourceEvent':
        return ResourceEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceEvent):
        """
        Dynamic initializer for ResourceEvent.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ResourceEvent$PackageImported> dev.ultreon.quantum.events.ResourceEvent.IMPORTED
    IMPORTED: 'api.Event' = __wrap(__api.Event.IMPORTED)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.ResourceEvent()"""
        val = __ResourceEvent()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.ResourceEvent()"""
        val = __ResourceEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.ItemEvents as __ItemEvents
__ItemEvents = __ItemEvents
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
 
class ItemEvents():
    """dev.ultreon.quantum.events.ItemEvents"""
 
    @staticmethod
    def __wrap(java_value: __ItemEvents) -> 'ItemEvents':
        return ItemEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemEvents):
        """
        Dynamic initializer for ItemEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ItemEvents$Use> dev.ultreon.quantum.events.ItemEvents.USE
    USE: 'api.Event' = __wrap(__api.Event.USE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.ItemEvents$Dropped> dev.ultreon.quantum.events.ItemEvents.DROPPED
    DROPPED: 'api.Event' = __wrap(__api.Event.DROPPED)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.events.ItemEvents()"""
        val = __ItemEvents()
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
    def __init__(self):
        """public dev.ultreon.quantum.events.ItemEvents()"""
        val = __ItemEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$ChunkLoaded
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_ChunkLoaded
__ChunkLoaded = __WorldEvents_ChunkLoaded.ChunkLoaded
from abc import abstractmethod, ABC
 
class ChunkLoaded(ABC):
    """dev.ultreon.quantum.events.WorldEvents.ChunkLoaded"""
 
    @staticmethod
    def __wrap(java_value: __ChunkLoaded) -> 'ChunkLoaded':
        return ChunkLoaded(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkLoaded):
        """
        Dynamic initializer for ChunkLoaded.
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
    def onChunkLoaded(self, arg0: 'World', arg1: 'ChunkPos', arg2: 'Chunk'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$ChunkLoaded.onChunkLoaded(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents
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
import dev.ultreon.quantum.events.EntityEvents as __EntityEvents
__EntityEvents = __EntityEvents
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntityEvents():
    """dev.ultreon.quantum.events.EntityEvents"""
 
    @staticmethod
    def __wrap(java_value: __EntityEvents) -> 'EntityEvents':
        return EntityEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityEvents):
        """
        Dynamic initializer for EntityEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Move> dev.ultreon.quantum.events.EntityEvents.MOVE
    MOVE: 'api.Event' = __wrap(__api.Event.MOVE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Removed> dev.ultreon.quantum.events.EntityEvents.REMOVED
    REMOVED: 'api.Event' = __wrap(__api.Event.REMOVED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Death> dev.ultreon.quantum.events.EntityEvents.DEATH
    DEATH: 'api.Event' = __wrap(__api.Event.DEATH)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.EntityEvents$Damage> dev.ultreon.quantum.events.EntityEvents.DAMAGE
    DAMAGE: 'api.Event' = __wrap(__api.Event.DAMAGE)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.EntityEvents()"""
        val = __EntityEvents()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.events.EntityEvents()"""
        val = __EntityEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import dev.ultreon.quantum.events.LoadingEvent as __LoadingEvent_ModifyRecipes
__ModifyRecipes = __LoadingEvent_ModifyRecipes.ModifyRecipes
from abc import abstractmethod, ABC
 
class ModifyRecipes(ABC):
    """dev.ultreon.quantum.events.LoadingEvent.ModifyRecipes"""
 
    @staticmethod
    def __wrap(java_value: __ModifyRecipes) -> 'ModifyRecipes':
        return ModifyRecipes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModifyRecipes):
        """
        Dynamic initializer for ModifyRecipes.
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
    def onModifyRecipes(self, arg0: 'RecipeManager', arg1: 'RecipeType', arg2: 'RecipeRegistry'):
        """public abstract void dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes.onModifyRecipes(dev.ultreon.quantum.recipe.RecipeManager,dev.ultreon.quantum.recipe.RecipeType,dev.ultreon.quantum.recipe.RecipeRegistry<dev.ultreon.quantum.recipe.Recipe>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ResourceEvent$PackageImported
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.ResourceEvent as __ResourceEvent_PackageImported
__PackageImported = __ResourceEvent_PackageImported.PackageImported
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

from abc import abstractmethod, ABC
 
class PackageImported(ABC):
    """dev.ultreon.quantum.events.ResourceEvent.PackageImported"""
 
    @staticmethod
    def __wrap(java_value: __PackageImported) -> 'PackageImported':
        return PackageImported(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PackageImported):
        """
        Dynamic initializer for PackageImported.
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
    def onImported(self, arg0: 'ResourcePackage'):
        """public abstract void dev.ultreon.quantum.events.ResourceEvent$PackageImported.onImported(dev.ultreon.quantum.resources.ResourcePackage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Death
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = __import_once__("pyquantum.entity.damagesource")

import dev.ultreon.quantum.events.EntityEvents as __EntityEvents_Death
__Death = __EntityEvents_Death.Death
from abc import abstractmethod, ABC
 
class Death(ABC):
    """dev.ultreon.quantum.events.EntityEvents.Death"""
 
    @staticmethod
    def __wrap(java_value: __Death) -> 'Death':
        return Death(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Death):
        """
        Dynamic initializer for Death.
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
    def onEntityDeath(self, arg0: 'LivingEntity', arg1: 'DamageSource'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.EntityEvents$Death.onEntityDeath(dev.ultreon.quantum.entity.LivingEntity,dev.ultreon.quantum.entity.damagesource.DamageSource)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BreakBlock
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_BreakBlock
__BreakBlock = __BlockEvents_BreakBlock.BreakBlock
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

from abc import abstractmethod, ABC
 
class BreakBlock(ABC):
    """dev.ultreon.quantum.events.BlockEvents.BreakBlock"""
 
    @staticmethod
    def __wrap(java_value: __BreakBlock) -> 'BreakBlock':
        return BreakBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BreakBlock):
        """
        Dynamic initializer for BreakBlock.
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
    def onBreakBlock(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.BlockEvents$BreakBlock.onBreakBlock(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldLifecycleEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.events.WorldLifecycleEvents as __WorldLifecycleEvents
__WorldLifecycleEvents = __WorldLifecycleEvents
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
 
class WorldLifecycleEvents():
    """dev.ultreon.quantum.events.WorldLifecycleEvents"""
 
    @staticmethod
    def __wrap(java_value: __WorldLifecycleEvents) -> 'WorldLifecycleEvents':
        return WorldLifecycleEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldLifecycleEvents):
        """
        Dynamic initializer for WorldLifecycleEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt> dev.ultreon.quantum.events.WorldLifecycleEvents.BIOME_LAYERS_BUILT
    BIOME_LAYERS_BUILT: 'api.Event' = __wrap(__api.Event.BIOME_LAYERS_BUILT)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.WorldLifecycleEvents()"""
        val = __WorldLifecycleEvents()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.WorldLifecycleEvents()"""
        val = __WorldLifecycleEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$PostTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_PostTick
__PostTick = __WorldEvents_PostTick.PostTick
 
class PostTick(ABC):
    """dev.ultreon.quantum.events.WorldEvents.PostTick"""
 
    @staticmethod
    def __wrap(java_value: __PostTick) -> 'PostTick':
        return PostTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PostTick):
        """
        Dynamic initializer for PostTick.
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
    def onPostTick(self, arg0: 'World'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$PostTick.onPostTick(dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveChunk
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_SaveChunk
__SaveChunk = __WorldEvents_SaveChunk.SaveChunk
from abc import abstractmethod, ABC
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class SaveChunk(ABC):
    """dev.ultreon.quantum.events.WorldEvents.SaveChunk"""
 
    @staticmethod
    def __wrap(java_value: __SaveChunk) -> 'SaveChunk':
        return SaveChunk(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SaveChunk):
        """
        Dynamic initializer for SaveChunk.
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
    def onSaveChunk(self, arg0: 'Chunk', arg1: 'MapType'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveChunk.onSaveChunk(dev.ultreon.quantum.world.Chunk,dev.ultreon.ubo.types.MapType)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuClickEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.MenuEvents as __MenuEvents_MenuClickEvent
__MenuClickEvent = __MenuEvents_MenuClickEvent.MenuClickEvent
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class MenuClickEvent(ABC):
    """dev.ultreon.quantum.events.MenuEvents.MenuClickEvent"""
 
    @staticmethod
    def __wrap(java_value: __MenuClickEvent) -> 'MenuClickEvent':
        return MenuClickEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuClickEvent):
        """
        Dynamic initializer for MenuClickEvent.
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
    def onMenuClick(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer', arg2: 'ItemSlot', arg3: bool):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.MenuEvents$MenuClickEvent.onMenuClick(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.ItemSlot,boolean)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$CreateBiome
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_CreateBiome
__CreateBiome = __WorldEvents_CreateBiome.CreateBiome
try:
    from pyquantum.world.gen import noise
except ImportError:
    noise = __import_once__("pyquantum.world.gen.noise")

from abc import abstractmethod, ABC
import java.util.List as List
 
class CreateBiome(ABC):
    """dev.ultreon.quantum.events.WorldEvents.CreateBiome"""
 
    @staticmethod
    def __wrap(java_value: __CreateBiome) -> 'CreateBiome':
        return CreateBiome(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CreateBiome):
        """
        Dynamic initializer for CreateBiome.
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
    def onCreateBiome(self, arg0: 'World', arg1: 'DomainWarping', arg2: 'List', arg3: 'List'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$CreateBiome.onCreateBiome(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.gen.noise.DomainWarping,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$LoadRegion
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_LoadRegion
__LoadRegion = __WorldEvents_LoadRegion.LoadRegion
from abc import abstractmethod, ABC
 
class LoadRegion(ABC):
    """dev.ultreon.quantum.events.WorldEvents.LoadRegion"""
 
    @staticmethod
    def __wrap(java_value: __LoadRegion) -> 'LoadRegion':
        return LoadRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadRegion):
        """
        Dynamic initializer for LoadRegion.
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
    def onLoadRegion(self, arg0: 'World', arg1: 'Region'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$LoadRegion.onLoadRegion(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.ServerWorld$Region)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.events.MenuEvents as __MenuEvents
__MenuEvents = __MenuEvents
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
 
class MenuEvents():
    """dev.ultreon.quantum.events.MenuEvents"""
 
    @staticmethod
    def __wrap(java_value: __MenuEvents) -> 'MenuEvents':
        return MenuEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuEvents):
        """
        Dynamic initializer for MenuEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent> dev.ultreon.quantum.events.MenuEvents.MENU_CLOSE
    MENU_CLOSE: 'api.Event' = __wrap(__api.Event.MENU_CLOSE)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent> dev.ultreon.quantum.events.MenuEvents.MENU_OPEN
    MENU_OPEN: 'api.Event' = __wrap(__api.Event.MENU_OPEN)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.MenuEvents$MenuClickEvent> dev.ultreon.quantum.events.MenuEvents.MENU_CLICK
    MENU_CLICK: 'api.Event' = __wrap(__api.Event.MENU_CLICK)


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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.MenuEvents()"""
        val = __MenuEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.MenuEvents()"""
        val = __MenuEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Move
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.EntityEvents as __EntityEvents_Move
__Move = __EntityEvents_Move.Move
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from abc import abstractmethod, ABC
 
class Move(ABC):
    """dev.ultreon.quantum.events.EntityEvents.Move"""
 
    @staticmethod
    def __wrap(java_value: __Move) -> 'Move':
        return Move(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Move):
        """
        Dynamic initializer for Move.
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
    def onEntityMove(self, arg0: 'Entity', arg1: float, arg2: float, arg3: float):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<dev.ultreon.libs.commons.v0.vector.Vec3d> dev.ultreon.quantum.events.EntityEvents$Move.onEntityMove(dev.ultreon.quantum.entity.Entity,double,double,double)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Spawned
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.events.PlayerEvents as __PlayerEvents_Spawned
__Spawned = __PlayerEvents_Spawned.Spawned
from abc import abstractmethod, ABC
 
class Spawned(ABC):
    """dev.ultreon.quantum.events.PlayerEvents.Spawned"""
 
    @staticmethod
    def __wrap(java_value: __Spawned) -> 'Spawned':
        return Spawned(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Spawned):
        """
        Dynamic initializer for Spawned.
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
    def onPlayerSpawned(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Spawned.onPlayerSpawned(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents
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
import dev.ultreon.quantum.events.WorldEvents as __WorldEvents
__WorldEvents = __WorldEvents
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldEvents():
    """dev.ultreon.quantum.events.WorldEvents"""
 
    @staticmethod
    def __wrap(java_value: __WorldEvents) -> 'WorldEvents':
        return WorldEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldEvents):
        """
        Dynamic initializer for WorldEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveRegion> dev.ultreon.quantum.events.WorldEvents.SAVE_REGION
    SAVE_REGION: 'api.Event' = __wrap(__api.Event.SAVE_REGION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$PreTick> dev.ultreon.quantum.events.WorldEvents.PRE_TICK
    PRE_TICK: 'api.Event' = __wrap(__api.Event.PRE_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadRegion> dev.ultreon.quantum.events.WorldEvents.LOAD_REGION
    LOAD_REGION: 'api.Event' = __wrap(__api.Event.LOAD_REGION)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveChunk> dev.ultreon.quantum.events.WorldEvents.SAVE_CHUNK
    SAVE_CHUNK: 'api.Event' = __wrap(__api.Event.SAVE_CHUNK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadChunk> dev.ultreon.quantum.events.WorldEvents.LOAD_CHUNK
    LOAD_CHUNK: 'api.Event' = __wrap(__api.Event.LOAD_CHUNK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkBuilt> dev.ultreon.quantum.events.WorldEvents.CHUNK_BUILT
    CHUNK_BUILT: 'api.Event' = __wrap(__api.Event.CHUNK_BUILT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$CreateBiome> dev.ultreon.quantum.events.WorldEvents.CREATE_BIOME
    CREATE_BIOME: 'api.Event' = __wrap(__api.Event.CREATE_BIOME)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkUnloaded> dev.ultreon.quantum.events.WorldEvents.CHUNK_UNLOADED
    CHUNK_UNLOADED: 'api.Event' = __wrap(__api.Event.CHUNK_UNLOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$SaveWorld> dev.ultreon.quantum.events.WorldEvents.SAVE_WORLD
    SAVE_WORLD: 'api.Event' = __wrap(__api.Event.SAVE_WORLD)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$PostTick> dev.ultreon.quantum.events.WorldEvents.POST_TICK
    POST_TICK: 'api.Event' = __wrap(__api.Event.POST_TICK)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$ChunkLoaded> dev.ultreon.quantum.events.WorldEvents.CHUNK_LOADED
    CHUNK_LOADED: 'api.Event' = __wrap(__api.Event.CHUNK_LOADED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.WorldEvents$LoadWorld> dev.ultreon.quantum.events.WorldEvents.LOAD_WORLD
    LOAD_WORLD: 'api.Event' = __wrap(__api.Event.LOAD_WORLD)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.events.WorldEvents()"""
        val = __WorldEvents()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.WorldEvents()"""
        val = __WorldEvents()
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
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$InitialItems
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.PlayerEvents as __PlayerEvents_InitialItems
__InitialItems = __PlayerEvents_InitialItems.InitialItems
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class InitialItems(ABC):
    """dev.ultreon.quantum.events.PlayerEvents.InitialItems"""
 
    @staticmethod
    def __wrap(java_value: __InitialItems) -> 'InitialItems':
        return InitialItems(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InitialItems):
        """
        Dynamic initializer for InitialItems.
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
    def onPlayerInitialItems(self, arg0: 'ServerPlayer', arg1: 'Inventory'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.PlayerEvents$InitialItems.onPlayerInitialItems(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.menu.Inventory)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Removed
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.EntityEvents as __EntityEvents_Removed
__Removed = __EntityEvents_Removed.Removed
 
class Removed(ABC):
    """dev.ultreon.quantum.events.EntityEvents.Removed"""
 
    @staticmethod
    def __wrap(java_value: __Removed) -> 'Removed':
        return Removed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Removed):
        """
        Dynamic initializer for Removed.
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
    def onEntityRemoved(self, arg0: 'Entity'):
        """public abstract void dev.ultreon.quantum.events.EntityEvents$Removed.onEntityRemoved(dev.ultreon.quantum.entity.Entity)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$PreTick
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_PreTick
__PreTick = __WorldEvents_PreTick.PreTick
 
class PreTick(ABC):
    """dev.ultreon.quantum.events.WorldEvents.PreTick"""
 
    @staticmethod
    def __wrap(java_value: __PreTick) -> 'PreTick':
        return PreTick(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PreTick):
        """
        Dynamic initializer for PreTick.
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
    def onPreTick(self, arg0: 'World'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$PreTick.onPreTick(dev.ultreon.quantum.world.World)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$BlockRemoved
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_BlockRemoved
__BlockRemoved = __BlockEvents_BlockRemoved.BlockRemoved
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
 
class BlockRemoved(ABC):
    """dev.ultreon.quantum.events.BlockEvents.BlockRemoved"""
 
    @staticmethod
    def __wrap(java_value: __BlockRemoved) -> 'BlockRemoved':
        return BlockRemoved(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockRemoved):
        """
        Dynamic initializer for BlockRemoved.
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
    def onBlockRemoved(self, arg0: 'ServerPlayer', arg1: 'BlockProperties', arg2: 'BlockPos', arg3: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$BlockRemoved.onBlockRemoved(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents$Dropped
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.ItemEvents as __ItemEvents_Dropped
__Dropped = __ItemEvents_Dropped.Dropped
 
class Dropped(ABC):
    """dev.ultreon.quantum.events.ItemEvents.Dropped"""
 
    @staticmethod
    def __wrap(java_value: __Dropped) -> 'Dropped':
        return Dropped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Dropped):
        """
        Dynamic initializer for Dropped.
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
    def onDropped(self, arg0: 'ItemStack'):
        """public abstract void dev.ultreon.quantum.events.ItemEvents$Dropped.onDropped(dev.ultreon.quantum.item.ItemStack)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.BlockEvents$SetBlock
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.BlockEvents as __BlockEvents_SetBlock
__SetBlock = __BlockEvents_SetBlock.SetBlock
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

from abc import abstractmethod, ABC
 
class SetBlock(ABC):
    """dev.ultreon.quantum.events.BlockEvents.SetBlock"""
 
    @staticmethod
    def __wrap(java_value: __SetBlock) -> 'SetBlock':
        return SetBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetBlock):
        """
        Dynamic initializer for SetBlock.
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
    def onSetBlock(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public abstract void dev.ultreon.quantum.events.BlockEvents$SetBlock.onSetBlock(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldEvents$SaveWorld
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.events.WorldEvents as __WorldEvents_SaveWorld
__SaveWorld = __WorldEvents_SaveWorld.SaveWorld
from abc import abstractmethod, ABC
 
class SaveWorld(ABC):
    """dev.ultreon.quantum.events.WorldEvents.SaveWorld"""
 
    @staticmethod
    def __wrap(java_value: __SaveWorld) -> 'SaveWorld':
        return SaveWorld(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SaveWorld):
        """
        Dynamic initializer for SaveWorld.
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
    def onSaveWorld(self, arg0: 'World', arg1: 'WorldStorage'):
        """public abstract void dev.ultreon.quantum.events.WorldEvents$SaveWorld.onSaveWorld(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.WorldStorage)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.events.MenuEvents as __MenuEvents_MenuOpenEvent
__MenuOpenEvent = __MenuEvents_MenuOpenEvent.MenuOpenEvent
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class MenuOpenEvent(ABC):
    """dev.ultreon.quantum.events.MenuEvents.MenuOpenEvent"""
 
    @staticmethod
    def __wrap(java_value: __MenuOpenEvent) -> 'MenuOpenEvent':
        return MenuOpenEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuOpenEvent):
        """
        Dynamic initializer for MenuOpenEvent.
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
    def onMenuOpen(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer'):
        """public abstract dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.MenuEvents$MenuOpenEvent.onMenuOpen(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.events.MenuEvents as __MenuEvents_MenuCloseEvent
__MenuCloseEvent = __MenuEvents_MenuCloseEvent.MenuCloseEvent
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class MenuCloseEvent(ABC):
    """dev.ultreon.quantum.events.MenuEvents.MenuCloseEvent"""
 
    @staticmethod
    def __wrap(java_value: __MenuCloseEvent) -> 'MenuCloseEvent':
        return MenuCloseEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MenuCloseEvent):
        """
        Dynamic initializer for MenuCloseEvent.
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
    def onMenuClose(self, arg0: 'ContainerMenu', arg1: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.MenuEvents$MenuCloseEvent.onMenuClose(dev.ultreon.quantum.menu.ContainerMenu,dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.EntityEvents$Damage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.EntityEvents as __EntityEvents_Damage
__Damage = __EntityEvents_Damage.Damage
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

try:
    from pyquantum.entity import damagesource
except ImportError:
    damagesource = __import_once__("pyquantum.entity.damagesource")

from abc import abstractmethod, ABC
 
class Damage(ABC):
    """dev.ultreon.quantum.events.EntityEvents.Damage"""
 
    @staticmethod
    def __wrap(java_value: __Damage) -> 'Damage':
        return Damage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Damage):
        """
        Dynamic initializer for Damage.
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
    def onEntityDamage(self, arg0: 'LivingEntity', arg1: 'DamageSource', arg2: float):
        """public abstract dev.ultreon.quantum.events.api.ValueEventResult<java.lang.Float> dev.ultreon.quantum.events.EntityEvents$Damage.onEntityDamage(dev.ultreon.quantum.entity.LivingEntity,dev.ultreon.quantum.entity.damagesource.DamageSource,float)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.WorldLifecycleEvents as __WorldLifecycleEvents_BiomeLayersBuilt
__BiomeLayersBuilt = __WorldLifecycleEvents_BiomeLayersBuilt.BiomeLayersBuilt
import java.util.List as List
 
class BiomeLayersBuilt(ABC):
    """dev.ultreon.quantum.events.WorldLifecycleEvents.BiomeLayersBuilt"""
 
    @staticmethod
    def __wrap(java_value: __BiomeLayersBuilt) -> 'BiomeLayersBuilt':
        return BiomeLayersBuilt(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiomeLayersBuilt):
        """
        Dynamic initializer for BiomeLayersBuilt.
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
    def onBiomeLayersBuilt(self, arg0: 'Biome', arg1: 'List', arg2: 'List'):
        """public abstract void dev.ultreon.quantum.events.WorldLifecycleEvents$BiomeLayersBuilt.onBiomeLayersBuilt(dev.ultreon.quantum.world.Biome,java.util.List<dev.ultreon.quantum.world.gen.layer.TerrainLayer>,java.util.List<dev.ultreon.quantum.world.gen.WorldGenFeature>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Joined
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.PlayerEvents as __PlayerEvents_Joined
__Joined = __PlayerEvents_Joined.Joined
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

from abc import abstractmethod, ABC
 
class Joined(ABC):
    """dev.ultreon.quantum.events.PlayerEvents.Joined"""
 
    @staticmethod
    def __wrap(java_value: __Joined) -> 'Joined':
        return Joined(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Joined):
        """
        Dynamic initializer for Joined.
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
    def onPlayerJoined(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Joined.onPlayerJoined(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents$Left
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.events.PlayerEvents as __PlayerEvents_Left
__Left = __PlayerEvents_Left.Left
from abc import abstractmethod, ABC
 
class Left(ABC):
    """dev.ultreon.quantum.events.PlayerEvents.Left"""
 
    @staticmethod
    def __wrap(java_value: __Left) -> 'Left':
        return Left(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Left):
        """
        Dynamic initializer for Left.
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
    def onPlayerLeft(self, arg0: 'ServerPlayer'):
        """public abstract void dev.ultreon.quantum.events.PlayerEvents$Left.onPlayerLeft(dev.ultreon.quantum.server.player.ServerPlayer)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.PlayerEvents
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.PlayerEvents as __PlayerEvents
__PlayerEvents = __PlayerEvents
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
 
class PlayerEvents():
    """dev.ultreon.quantum.events.PlayerEvents"""
 
    @staticmethod
    def __wrap(java_value: __PlayerEvents) -> 'PlayerEvents':
        return PlayerEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerEvents):
        """
        Dynamic initializer for PlayerEvents.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Joined> dev.ultreon.quantum.events.PlayerEvents.PLAYER_JOINED
    PLAYER_JOINED: 'api.Event' = __wrap(__api.Event.PLAYER_JOINED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Spawned> dev.ultreon.quantum.events.PlayerEvents.PLAYER_SPAWNED
    PLAYER_SPAWNED: 'api.Event' = __wrap(__api.Event.PLAYER_SPAWNED)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$Left> dev.ultreon.quantum.events.PlayerEvents.PLAYER_LEFT
    PLAYER_LEFT: 'api.Event' = __wrap(__api.Event.PLAYER_LEFT)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.PlayerEvents$InitialItems> dev.ultreon.quantum.events.PlayerEvents.INITIAL_ITEMS
    INITIAL_ITEMS: 'api.Event' = __wrap(__api.Event.INITIAL_ITEMS)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.PlayerEvents()"""
        val = __PlayerEvents()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.PlayerEvents()"""
        val = __PlayerEvents()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.LoadingEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.events import api
except ImportError:
    api = __import_once__("pyquantum.events.api")

from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.events.LoadingEvent as __LoadingEvent
__LoadingEvent = __LoadingEvent
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
 
class LoadingEvent():
    """dev.ultreon.quantum.events.LoadingEvent"""
 
    @staticmethod
    def __wrap(java_value: __LoadingEvent) -> 'LoadingEvent':
        return LoadingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadingEvent):
        """
        Dynamic initializer for LoadingEvent.
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
 
    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$ModifyRecipes> dev.ultreon.quantum.events.LoadingEvent.MODIFY_RECIPES
    MODIFY_RECIPES: 'api.Event' = __wrap(__api.Event.MODIFY_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RecipeState> dev.ultreon.quantum.events.LoadingEvent.LOAD_RECIPES
    LOAD_RECIPES: 'api.Event' = __wrap(__api.Event.LOAD_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RecipeState> dev.ultreon.quantum.events.LoadingEvent.UNLOAD_RECIPES
    UNLOAD_RECIPES: 'api.Event' = __wrap(__api.Event.UNLOAD_RECIPES)

    # public static final dev.ultreon.quantum.events.api.Event<dev.ultreon.quantum.events.LoadingEvent$RegisterCommands> dev.ultreon.quantum.events.LoadingEvent.REGISTER_COMMANDS
    REGISTER_COMMANDS: 'api.Event' = __wrap(__api.Event.REGISTER_COMMANDS)


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
    def __init__(self):
        """public dev.ultreon.quantum.events.LoadingEvent()"""
        val = __LoadingEvent()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.LoadingEvent()"""
        val = __LoadingEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.ItemEvents$Use
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.events.ItemEvents as __ItemEvents_Use
__Use = __ItemEvents_Use.Use
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from abc import abstractmethod, ABC
 
class Use(ABC):
    """dev.ultreon.quantum.events.ItemEvents.Use"""
 
    @staticmethod
    def __wrap(java_value: __Use) -> 'Use':
        return Use(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Use):
        """
        Dynamic initializer for Use.
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
    def onUseItem(self, arg0: 'Item', arg1: 'UseItemContext'):
        """public abstract void dev.ultreon.quantum.events.ItemEvents$Use.onUseItem(dev.ultreon.quantum.item.Item,dev.ultreon.quantum.item.UseItemContext)"""
        pass