from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.block.SlabBlock as __SlabBlock
__SlabBlock = __SlabBlock
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SlabBlock(__Block, Block):
    """dev.ultreon.quantum.block.SlabBlock"""
 
    @staticmethod
    def __wrap(java_value: __SlabBlock) -> 'SlabBlock':
        return SlabBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SlabBlock):
        """
        Dynamic initializer for SlabBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = __SlabBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__SlabBlock, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.SlabBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __SlabBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.SlabBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__SlabBlock, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = __SlabBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(SlabBlock, self).createMeta())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent())

 
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.block.SlabBlock as __SlabBlock
__SlabBlock = __SlabBlock
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SlabBlock(__Block, Block):
    """dev.ultreon.quantum.block.SlabBlock"""
 
    @staticmethod
    def __wrap(java_value: __SlabBlock) -> 'SlabBlock':
        return SlabBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SlabBlock):
        """
        Dynamic initializer for SlabBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = __SlabBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__SlabBlock, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.SlabBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __SlabBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.SlabBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__SlabBlock, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = __SlabBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(SlabBlock, self).createMeta())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent())

 
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock 
 
 
# CLASS: dev.ultreon.quantum.block.EntityBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import dev.ultreon.quantum.block.EntityBlock as __EntityBlock
__EntityBlock = __EntityBlock
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class EntityBlock(ABC, __Block, Block):
    """dev.ultreon.quantum.block.EntityBlock"""
 
    @staticmethod
    def __wrap(java_value: __EntityBlock) -> 'EntityBlock':
        return EntityBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityBlock):
        """
        Dynamic initializer for EntityBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return EntityBlock.__wrap(__EntityBlock.simple(arg0))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.EntityBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __EntityBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType', arg1: 'Properties') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.block.Block$Properties)"""
        return EntityBlock.__wrap(__EntityBlock.simple(arg0, arg1))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.EntityBlock()"""
        val = __EntityBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.EntityBlock()"""
        val = __EntityBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(Block, self).createMeta())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

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
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.EntityBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__EntityBlock, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5)) 
 
 
# CLASS: dev.ultreon.quantum.block.MetaSwitchTestBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.MetaSwitchTestBlock as __MetaSwitchTestBlock
__MetaSwitchTestBlock = __MetaSwitchTestBlock
try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MetaSwitchTestBlock(__Block, Block):
    """dev.ultreon.quantum.block.MetaSwitchTestBlock"""
 
    @staticmethod
    def __wrap(java_value: __MetaSwitchTestBlock) -> 'MetaSwitchTestBlock':
        return MetaSwitchTestBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MetaSwitchTestBlock):
        """
        Dynamic initializer for MetaSwitchTestBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.MetaSwitchTestBlock()"""
        val = __MetaSwitchTestBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.MetaSwitchTestBlock.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(MetaSwitchTestBlock, self).createMeta())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.MetaSwitchTestBlock.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__MetaSwitchTestBlock, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.MetaSwitchTestBlock()"""
        val = __MetaSwitchTestBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.block.Block$Properties
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.block.Block as __Block_Properties
__Properties = __Block_Properties.Properties
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Properties():
    """dev.ultreon.quantum.block.Block.Properties"""
 
    @staticmethod
    def __wrap(java_value: __Properties) -> 'Properties':
        return Properties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Properties):
        """
        Dynamic initializer for Properties.
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
    def noOcclude(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noOcclude()"""
        return 'Properties'.__wrap(super(Properties, self).noOcclude())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def unbreakable(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.unbreakable()"""
        return 'Properties'.__wrap(super(Properties, self).unbreakable())

    @overload
    def noCollision(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noCollision()"""
        return 'Properties'.__wrap(super(Properties, self).noCollision())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Block$Properties()"""
        val = __Properties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dropsItems(self, *arg0: 'item.ItemStack') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.item.ItemStack...)"""
        return 'Properties'.__wrap(super(__Properties, self).dropsItems(arg0))

    @overload
    def usesCustomRender(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.usesCustomRender()"""
        return 'Properties'.__wrap(super(Properties, self).usesCustomRender())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def dropsItems(self, *arg0: 'item.Item') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.item.Item...)"""
        return 'Properties'.__wrap(super(__Properties, self).dropsItems(arg0))

    @overload
    def noGreedyMerge(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noGreedyMerge()"""
        return 'Properties'.__wrap(super(Properties, self).noGreedyMerge())

    @overload
    def effectiveTool(self, arg0: 'ToolType') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.effectiveTool(dev.ultreon.quantum.item.tool.ToolType)"""
        return 'Properties'.__wrap(super(__Properties, self).effectiveTool(arg0))

    @overload
    def hardness(self, arg0: float) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.hardness(float)"""
        return 'Properties'.__wrap(super(__Properties, self).hardness(__float.valueOf(arg0)))

    @overload
    def dropsItems(self, arg0: 'LootGenerator') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.world.loot.LootGenerator)"""
        return 'Properties'.__wrap(super(__Properties, self).dropsItems(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def toolRequirement(self, arg0: 'ToolLevel') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.toolRequirement(dev.ultreon.quantum.block.ToolLevel)"""
        return 'Properties'.__wrap(super(__Properties, self).toolRequirement(arg0))

    @overload
    def instaBreak(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.instaBreak()"""
        return 'Properties'.__wrap(super(Properties, self).instaBreak())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def requiresTool(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.requiresTool()"""
        return 'Properties'.__wrap(super(Properties, self).requiresTool())

    @overload
    def fluid(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.fluid()"""
        return 'Properties'.__wrap(super(Properties, self).fluid())

    @overload
    def transparent(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.transparent()"""
        return 'Properties'.__wrap(super(Properties, self).transparent())

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
    def replaceable(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.replaceable()"""
        return 'Properties'.__wrap(super(Properties, self).replaceable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.Block$Properties()"""
        val = __Properties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def noRendering(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noRendering()"""
        return 'Properties'.__wrap(super(Properties, self).noRendering()) 
 
 
# CLASS: dev.ultreon.quantum.block.BlockTags
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.block.BlockTags as __BlockTags
__BlockTags = __BlockTags
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum import tags
except ImportError:
    tags = __import_once__("pyquantum.tags")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlockTags():
    """dev.ultreon.quantum.block.BlockTags"""
 
    @staticmethod
    def __wrap(java_value: __BlockTags) -> 'BlockTags':
        return BlockTags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlockTags):
        """
        Dynamic initializer for BlockTags.
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
 
    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_CHUNK_STEEL_TOOL
    REQUIRES_CHUNK_STEEL_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_CHUNK_STEEL_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_ULTRINIUM_TOOL
    REQUIRES_ULTRINIUM_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_ULTRINIUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_STONE_TOOL
    REQUIRES_STONE_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_STONE_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_DIAMOND_TOOL
    REQUIRES_DIAMOND_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_DIAMOND_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_COPPER_TOOL
    REQUIRES_COPPER_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_COPPER_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_PLATINUM_TOOL
    REQUIRES_PLATINUM_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_PLATINUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_GOLDEN_TOOL
    REQUIRES_GOLDEN_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_GOLDEN_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_WOODEN_TOOL
    REQUIRES_WOODEN_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_WOODEN_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_TITANIUM_TOOL
    REQUIRES_TITANIUM_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_TITANIUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_COBALT_TOOL
    REQUIRES_COBALT_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_COBALT_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_IRON_TOOL
    REQUIRES_IRON_TOOL: 'tags.NamedTag' = __wrap(__tags.NamedTag.REQUIRES_IRON_TOOL)


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
        """public dev.ultreon.quantum.block.BlockTags()"""
        val = __BlockTags()
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
        """public dev.ultreon.quantum.block.BlockTags()"""
        val = __BlockTags()
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
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.block.SlabBlock as __SlabBlock_Type
__Type = __SlabBlock_Type.Type
from typing import List
import java.lang.Enum as Enum
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
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type(__Enum, Enum):
    """dev.ultreon.quantum.block.SlabBlock.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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
 
    # public static final dev.ultreon.quantum.block.SlabBlock$Type dev.ultreon.quantum.block.SlabBlock$Type.TOP
    TOP: 'Type' = __wrap(__Type.TOP)

    # public static final dev.ultreon.quantum.block.SlabBlock$Type dev.ultreon.quantum.block.SlabBlock$Type.DOUBLE
    DOUBLE: 'Type' = __wrap(__Type.DOUBLE)

    # public static final dev.ultreon.quantum.block.SlabBlock$Type dev.ultreon.quantum.block.SlabBlock$Type.BOTTOM
    BOTTOM: 'Type' = __wrap(__Type.BOTTOM)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.block.SlabBlock$Type dev.ultreon.quantum.block.SlabBlock$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.block.SlabBlock$Type[] dev.ultreon.quantum.block.SlabBlock$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.block.CactusBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.block.CactusBlock as __CactusBlock
__CactusBlock = __CactusBlock
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CactusBlock(__Block, Block):
    """dev.ultreon.quantum.block.CactusBlock"""
 
    @staticmethod
    def __wrap(java_value: __CactusBlock) -> 'CactusBlock':
        return CactusBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CactusBlock):
        """
        Dynamic initializer for CactusBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.CactusBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __CactusBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.CactusBlock()"""
        val = __CactusBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(Block, self).createMeta())

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.CactusBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__CactusBlock, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.CactusBlock()"""
        val = __CactusBlock()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent()) 
 
 
# CLASS: dev.ultreon.quantum.block.Blocks
import dev.ultreon.quantum.block.Blocks as __Blocks
__Blocks = __Blocks
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Blocks():
    """dev.ultreon.quantum.block.Blocks"""
 
    @staticmethod
    def __wrap(java_value: __Blocks) -> 'Blocks':
        return Blocks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Blocks):
        """
        Dynamic initializer for Blocks.
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
 
    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.LOG
    LOG: 'Block' = __wrap(__Block.LOG)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.PLANKS_SLAB
    PLANKS_SLAB: 'Block' = __wrap(__Block.PLANKS_SLAB)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.TALL_GRASS
    TALL_GRASS: 'Block' = __wrap(__Block.TALL_GRASS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.SAND
    SAND: 'Block' = __wrap(__Block.SAND)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.SANDSTONE
    SANDSTONE: 'Block' = __wrap(__Block.SANDSTONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.GRAVEL
    GRAVEL: 'Block' = __wrap(__Block.GRAVEL)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.ERROR
    ERROR: 'Block' = __wrap(__Block.ERROR)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.VOIDGUARD
    VOIDGUARD: 'Block' = __wrap(__Block.VOIDGUARD)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.LEAVES
    LEAVES: 'Block' = __wrap(__Block.LEAVES)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.GRASS_BLOCK
    GRASS_BLOCK: 'Block' = __wrap(__Block.GRASS_BLOCK)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.COBBLESTONE
    COBBLESTONE: 'Block' = __wrap(__Block.COBBLESTONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.BARRIER
    BARRIER: 'Block' = __wrap(__Block.BARRIER)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.WATER
    WATER: 'Block' = __wrap(__Block.WATER)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.BLAST_FURNACE
    BLAST_FURNACE: 'Block' = __wrap(__Block.BLAST_FURNACE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CAVE_AIR
    CAVE_AIR: 'Block' = __wrap(__Block.CAVE_AIR)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.STONE
    STONE: 'Block' = __wrap(__Block.STONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.PLANKS
    PLANKS: 'Block' = __wrap(__Block.PLANKS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.DIRT
    DIRT: 'Block' = __wrap(__Block.DIRT)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CRAFTING_BENCH
    CRAFTING_BENCH: 'Block' = __wrap(__Block.CRAFTING_BENCH)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CACTUS
    CACTUS: 'Block' = __wrap(__Block.CACTUS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CRATE
    CRATE: 'Block' = __wrap(__Block.CRATE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.META_SWITCH_TEST
    META_SWITCH_TEST: 'Block' = __wrap(__Block.META_SWITCH_TEST)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.IRON_ORE
    IRON_ORE: 'Block' = __wrap(__Block.IRON_ORE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.AIR
    AIR: 'Block' = __wrap(__Block.AIR)


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
        """public dev.ultreon.quantum.block.Blocks()"""
        val = __Blocks()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Blocks()"""
        val = __Blocks()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.block.Blocks.init()"""
            __Blocks.init()

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
 
 
# CLASS: dev.ultreon.quantum.block.Block
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.String as __String
__String = __String
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Block(pyquantum.__DataWriter, ubo.DataWriter):
    """dev.ultreon.quantum.block.Block"""
 
    @staticmethod
    def __wrap(java_value: __Block) -> 'Block':
        return Block(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Block):
        """
        Dynamic initializer for Block.
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
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.Block()"""
        val = __Block()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Block()"""
        val = __Block()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(Block, self).createMeta())

    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.Block(dev.ultreon.quantum.block.Block$Properties)"""
        val = __Block(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent())

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5)) 
 
 
# CLASS: dev.ultreon.quantum.block.BlastFurnaceBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
import dev.ultreon.quantum.block.BlastFurnaceBlock as __BlastFurnaceBlock
__BlastFurnaceBlock = __BlastFurnaceBlock
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class BlastFurnaceBlock(__Block, Block):
    """dev.ultreon.quantum.block.BlastFurnaceBlock"""
 
    @staticmethod
    def __wrap(java_value: __BlastFurnaceBlock) -> 'BlastFurnaceBlock':
        return BlastFurnaceBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlastFurnaceBlock):
        """
        Dynamic initializer for BlastFurnaceBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.BlastFurnaceBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __BlastFurnaceBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.BlastFurnaceBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__BlastFurnaceBlock, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.BlastFurnaceBlock.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__BlastFurnaceBlock, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.BlastFurnaceBlock.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(BlastFurnaceBlock, self).createMeta())

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent()) 
 
 
# CLASS: dev.ultreon.quantum.block.CrateBlock
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = __import_once__("pyquantum.world.loot")

import dev.ultreon.quantum.world.loot.LootGenerator as __LootGenerator
__LootGenerator = __LootGenerator
import dev.ultreon.quantum.block.EntityBlock as __EntityBlock
__EntityBlock = __EntityBlock
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = __import_once__("pyquantum.item.tool")

import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
import dev.ultreon.quantum.block.Block as __Block
__Block = __Block
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import dev.ultreon.quantum.item.tool.ToolType as __ToolType
__ToolType = __ToolType
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.world.UseResult as __UseResult
__UseResult = __UseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum.block import entity
except ImportError:
    entity = __import_once__("pyquantum.block.entity")

try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.block.CrateBlock as __CrateBlock
__CrateBlock = __CrateBlock
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CrateBlock(__EntityBlock, EntityBlock):
    """dev.ultreon.quantum.block.CrateBlock"""
 
    @staticmethod
    def __wrap(java_value: __CrateBlock) -> 'CrateBlock':
        return CrateBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrateBlock):
        """
        Dynamic initializer for CrateBlock.
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
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__Block, self).update(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.CrateBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = __CrateBlock(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float.__wrap(super(Block, self).getHardness())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool.__wrap(super(__Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(__Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool.__wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'.__wrap(super(Block, self).save())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'.__wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool.__wrap(super(Block, self).hasCustomRender())

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool.__wrap(super(Block, self).isReplaceable())

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

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType', arg1: 'Properties') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.block.Block$Properties)"""
        return EntityBlock.__wrap(__EntityBlock.simple(arg0, arg1))

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return EntityBlock.__wrap(__EntityBlock.simple(arg0))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool.__wrap(super(Block, self).isUnbreakable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool.__wrap(super(__Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.CrateBlock.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'.__wrap(super(__CrateBlock, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool.__wrap(super(Block, self).isFluid())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(__Block, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'.__wrap(super(Block, self).getTranslation())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).boundingBox(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'.__wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'.__wrap(super(Block, self).createMeta())

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'.__wrap(super(Block, self).getId())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'.__wrap(super(__Block, self).getBoundingBox(arg0))

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'.__wrap(super(__Block, self).getDrops(arg0, arg1, arg2))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str.__wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str.__wrap(super(Block, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool.__wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'.__wrap(super(__Block, self).getLootGen(arg0))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.EntityBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__EntityBlock, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int.__wrap(super(Block, self).getRawId())

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool.__wrap(super(Block, self).hasCollider())

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool.__wrap(super(Block, self).doesOcclude())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool.__wrap(super(__Block, self).shouldOcclude(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool.__wrap(super(Block, self).isAir())

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block.__wrap(__Block.load(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'.__wrap(super(__Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool.__wrap(super(Block, self).doesRender())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool.__wrap(super(Block, self).isTransparent()) 
 
 
# CLASS: dev.ultreon.quantum.block.ToolLevel
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.tags.NamedTag as __NamedTag
__NamedTag = __NamedTag
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.block.ToolLevel as __ToolLevel
__ToolLevel = __ToolLevel
try:
    from pyquantum import tags
except ImportError:
    tags = __import_once__("pyquantum.tags")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ToolLevel():
    """dev.ultreon.quantum.block.ToolLevel"""
 
    @staticmethod
    def __wrap(java_value: __ToolLevel) -> 'ToolLevel':
        return ToolLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ToolLevel):
        """
        Dynamic initializer for ToolLevel.
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
 
    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.CHUNK_STEEL
    CHUNK_STEEL: 'ToolLevel' = __wrap(__ToolLevel.CHUNK_STEEL)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.DIAMOND
    DIAMOND: 'ToolLevel' = __wrap(__ToolLevel.DIAMOND)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.PLATINUM
    PLATINUM: 'ToolLevel' = __wrap(__ToolLevel.PLATINUM)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.STONE
    STONE: 'ToolLevel' = __wrap(__ToolLevel.STONE)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.IRON
    IRON: 'ToolLevel' = __wrap(__ToolLevel.IRON)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.COBALT
    COBALT: 'ToolLevel' = __wrap(__ToolLevel.COBALT)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.TITANIUM
    TITANIUM: 'ToolLevel' = __wrap(__ToolLevel.TITANIUM)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.GOLD
    GOLD: 'ToolLevel' = __wrap(__ToolLevel.GOLD)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.WOOD
    WOOD: 'ToolLevel' = __wrap(__ToolLevel.WOOD)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.ULTRINIUM
    ULTRINIUM: 'ToolLevel' = __wrap(__ToolLevel.ULTRINIUM)

    # public static final dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.ToolLevel.COPPER
    COPPER: 'ToolLevel' = __wrap(__ToolLevel.COPPER)


    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.ToolLevel.toString()"""
        return str.__wrap(super(ToolLevel, self).toString())

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
    def tag(self) -> 'tags.NamedTag':
        """public dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.ToolLevel.tag()"""
        return 'tags.NamedTag'.__wrap(super(ToolLevel, self).tag())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))