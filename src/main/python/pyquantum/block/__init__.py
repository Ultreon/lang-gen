from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.block.SlabBlock as _SlabBlock
_SlabBlock = _SlabBlock
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SlabBlock():
    """dev.ultreon.quantum.block.SlabBlock"""
 
    @staticmethod
    def _wrap(java_value: _SlabBlock) -> 'SlabBlock':
        return SlabBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SlabBlock):
        """
        Dynamic initializer for SlabBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SlabBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SlabBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.createMeta()"""
        return 'state.BlockProperties'._wrap(super(SlabBlock, self).createMeta())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_SlabBlock, self).onPlacedBy(arg0, arg1, arg2))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.SlabBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_SlabBlock, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.SlabBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _SlabBlock(arg0)
        self.__wrapper = val

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = _SlabBlock()
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = _SlabBlock()
        self.__wrapper = val

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.block.SlabBlock as _SlabBlock
_SlabBlock = _SlabBlock
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SlabBlock():
    """dev.ultreon.quantum.block.SlabBlock"""
 
    @staticmethod
    def _wrap(java_value: _SlabBlock) -> 'SlabBlock':
        return SlabBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SlabBlock):
        """
        Dynamic initializer for SlabBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SlabBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SlabBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.createMeta()"""
        return 'state.BlockProperties'._wrap(super(SlabBlock, self).createMeta())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.SlabBlock.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_SlabBlock, self).onPlacedBy(arg0, arg1, arg2))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.SlabBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_SlabBlock, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.SlabBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _SlabBlock(arg0)
        self.__wrapper = val

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = _SlabBlock()
        self.__wrapper = val

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.SlabBlock()"""
        val = _SlabBlock()
        self.__wrapper = val

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock 
 
 
# CLASS: dev.ultreon.quantum.block.EntityBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.EntityBlock as _EntityBlock
_EntityBlock = _EntityBlock
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityBlock():
    """dev.ultreon.quantum.block.EntityBlock"""
 
    @staticmethod
    def _wrap(java_value: _EntityBlock) -> 'EntityBlock':
        return EntityBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityBlock):
        """
        Dynamic initializer for EntityBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.EntityBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _EntityBlock(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return EntityBlock._wrap(_EntityBlock.simple(arg0))

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

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
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType', arg1: 'Properties') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.block.Block$Properties)"""
        return EntityBlock._wrap(_EntityBlock.simple(arg0, arg1))

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'._wrap(super(Block, self).createMeta())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.EntityBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_EntityBlock, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.EntityBlock()"""
        val = _EntityBlock()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.EntityBlock()"""
        val = _EntityBlock()
        self.__wrapper = val

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3)) 
 
 
# CLASS: dev.ultreon.quantum.block.MetaSwitchTestBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

import dev.ultreon.quantum.block.MetaSwitchTestBlock as _MetaSwitchTestBlock
_MetaSwitchTestBlock = _MetaSwitchTestBlock
from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MetaSwitchTestBlock():
    """dev.ultreon.quantum.block.MetaSwitchTestBlock"""
 
    @staticmethod
    def _wrap(java_value: _MetaSwitchTestBlock) -> 'MetaSwitchTestBlock':
        return MetaSwitchTestBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MetaSwitchTestBlock):
        """
        Dynamic initializer for MetaSwitchTestBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MetaSwitchTestBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MetaSwitchTestBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.MetaSwitchTestBlock.createMeta()"""
        return 'state.BlockProperties'._wrap(super(MetaSwitchTestBlock, self).createMeta())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.MetaSwitchTestBlock()"""
        val = _MetaSwitchTestBlock()
        self.__wrapper = val

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.MetaSwitchTestBlock()"""
        val = _MetaSwitchTestBlock()
        self.__wrapper = val

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.MetaSwitchTestBlock.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_MetaSwitchTestBlock, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.Block$Properties
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.block.Block as _Block_Properties
_Properties = _Block_Properties.Properties
import java.lang.Integer as _int
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Properties():
    """dev.ultreon.quantum.block.Block.Properties"""
 
    @staticmethod
    def _wrap(java_value: _Properties) -> 'Properties':
        return Properties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Properties):
        """
        Dynamic initializer for Properties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Properties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Properties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.Block$Properties()"""
        val = _Properties()
        self.__wrapper = val

    @overload
    def usesCustomRender(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.usesCustomRender()"""
        return 'Properties'._wrap(super(Properties, self).usesCustomRender())

    @overload
    def replaceable(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.replaceable()"""
        return 'Properties'._wrap(super(Properties, self).replaceable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transparent(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.transparent()"""
        return 'Properties'._wrap(super(Properties, self).transparent())

    @overload
    def fluid(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.fluid()"""
        return 'Properties'._wrap(super(Properties, self).fluid())

    @overload
    def dropsItems(self, *arg0: 'item.ItemStack') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.item.ItemStack...)"""
        return 'Properties'._wrap(super(_Properties, self).dropsItems(arg0))

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
    def hardness(self, arg0: float) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.hardness(float)"""
        return 'Properties'._wrap(super(_Properties, self).hardness(_float.valueOf(arg0)))

    @overload
    def noRendering(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noRendering()"""
        return 'Properties'._wrap(super(Properties, self).noRendering())

    @overload
    def unbreakable(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.unbreakable()"""
        return 'Properties'._wrap(super(Properties, self).unbreakable())

    @overload
    def toolRequirement(self, arg0: 'ToolLevel') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.toolRequirement(dev.ultreon.quantum.block.ToolLevel)"""
        return 'Properties'._wrap(super(_Properties, self).toolRequirement(arg0))

    @overload
    def dropsItems(self, *arg0: 'item.Item') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.item.Item...)"""
        return 'Properties'._wrap(super(_Properties, self).dropsItems(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def noCollision(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noCollision()"""
        return 'Properties'._wrap(super(Properties, self).noCollision())

    @overload
    def noGreedyMerge(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noGreedyMerge()"""
        return 'Properties'._wrap(super(Properties, self).noGreedyMerge())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Block$Properties()"""
        val = _Properties()
        self.__wrapper = val

    @overload
    def effectiveTool(self, arg0: 'ToolType') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.effectiveTool(dev.ultreon.quantum.item.tool.ToolType)"""
        return 'Properties'._wrap(super(_Properties, self).effectiveTool(arg0))

    @overload
    def noOcclude(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.noOcclude()"""
        return 'Properties'._wrap(super(Properties, self).noOcclude())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def requiresTool(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.requiresTool()"""
        return 'Properties'._wrap(super(Properties, self).requiresTool())

    @overload
    def instaBreak(self) -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.instaBreak()"""
        return 'Properties'._wrap(super(Properties, self).instaBreak())

    @overload
    def dropsItems(self, arg0: 'LootGenerator') -> 'Properties':
        """public dev.ultreon.quantum.block.Block$Properties dev.ultreon.quantum.block.Block$Properties.dropsItems(dev.ultreon.quantum.world.loot.LootGenerator)"""
        return 'Properties'._wrap(super(_Properties, self).dropsItems(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.BlockTags
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pyquantum import tags
except ImportError:
    tags = _import_once("pyquantum.tags")

import dev.ultreon.quantum.block.BlockTags as _BlockTags
_BlockTags = _BlockTags
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockTags():
    """dev.ultreon.quantum.block.BlockTags"""
 
    @staticmethod
    def _wrap(java_value: _BlockTags) -> 'BlockTags':
        return BlockTags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockTags):
        """
        Dynamic initializer for BlockTags.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockTags__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockTags__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_TITANIUM_TOOL
    REQUIRES_TITANIUM_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_TITANIUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_COBALT_TOOL
    REQUIRES_COBALT_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_COBALT_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_PLATINUM_TOOL
    REQUIRES_PLATINUM_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_PLATINUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_ULTRINIUM_TOOL
    REQUIRES_ULTRINIUM_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_ULTRINIUM_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_WOODEN_TOOL
    REQUIRES_WOODEN_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_WOODEN_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_STONE_TOOL
    REQUIRES_STONE_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_STONE_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_CHUNK_STEEL_TOOL
    REQUIRES_CHUNK_STEEL_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_CHUNK_STEEL_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_COPPER_TOOL
    REQUIRES_COPPER_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_COPPER_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_GOLDEN_TOOL
    REQUIRES_GOLDEN_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_GOLDEN_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_IRON_TOOL
    REQUIRES_IRON_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_IRON_TOOL)

    # public static final dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.BlockTags.REQUIRES_DIAMOND_TOOL
    REQUIRES_DIAMOND_TOOL: 'tags.NamedTag' = _wrap(_tags.NamedTag.REQUIRES_DIAMOND_TOOL)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.BlockTags()"""
        val = _BlockTags()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.BlockTags()"""
        val = _BlockTags()
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
 
 
# CLASS: dev.ultreon.quantum.block.SlabBlock$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.block.SlabBlock as _SlabBlock_Type
_Type = _SlabBlock_Type.Type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.block.SlabBlock.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.block.SlabBlock$Type dev.ultreon.quantum.block.SlabBlock$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.block.SlabBlock$Type[] dev.ultreon.quantum.block.SlabBlock$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Type.TOP = Type._wrap(_TOP.TOP)

Type.DOUBLE = Type._wrap(_DOUBLE.DOUBLE)

Type.BOTTOM = Type._wrap(_BOTTOM.BOTTOM) 
 
 
# CLASS: dev.ultreon.quantum.block.CactusBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import dev.ultreon.quantum.block.CactusBlock as _CactusBlock
_CactusBlock = _CactusBlock
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CactusBlock():
    """dev.ultreon.quantum.block.CactusBlock"""
 
    @staticmethod
    def _wrap(java_value: _CactusBlock) -> 'CactusBlock':
        return CactusBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CactusBlock):
        """
        Dynamic initializer for CactusBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CactusBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CactusBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.CactusBlock.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_CactusBlock, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'._wrap(super(Block, self).createMeta())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.CactusBlock()"""
        val = _CactusBlock()
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.CactusBlock()"""
        val = _CactusBlock()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.CactusBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _CactusBlock(arg0)
        self.__wrapper = val

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.Blocks
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.block.Blocks as _Blocks
_Blocks = _Blocks
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Blocks():
    """dev.ultreon.quantum.block.Blocks"""
 
    @staticmethod
    def _wrap(java_value: _Blocks) -> 'Blocks':
        return Blocks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Blocks):
        """
        Dynamic initializer for Blocks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Blocks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Blocks__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.SAND
    SAND: 'Block' = _wrap(_Block.SAND)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.PLANKS_SLAB
    PLANKS_SLAB: 'Block' = _wrap(_Block.PLANKS_SLAB)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.COBBLESTONE
    COBBLESTONE: 'Block' = _wrap(_Block.COBBLESTONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.GRAVEL
    GRAVEL: 'Block' = _wrap(_Block.GRAVEL)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CACTUS
    CACTUS: 'Block' = _wrap(_Block.CACTUS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.TALL_GRASS
    TALL_GRASS: 'Block' = _wrap(_Block.TALL_GRASS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CRATE
    CRATE: 'Block' = _wrap(_Block.CRATE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.DIRT
    DIRT: 'Block' = _wrap(_Block.DIRT)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.WATER
    WATER: 'Block' = _wrap(_Block.WATER)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.AIR
    AIR: 'Block' = _wrap(_Block.AIR)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.LOG
    LOG: 'Block' = _wrap(_Block.LOG)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CAVE_AIR
    CAVE_AIR: 'Block' = _wrap(_Block.CAVE_AIR)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.VOIDGUARD
    VOIDGUARD: 'Block' = _wrap(_Block.VOIDGUARD)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.STONE
    STONE: 'Block' = _wrap(_Block.STONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.CRAFTING_BENCH
    CRAFTING_BENCH: 'Block' = _wrap(_Block.CRAFTING_BENCH)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.SANDSTONE
    SANDSTONE: 'Block' = _wrap(_Block.SANDSTONE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.BARRIER
    BARRIER: 'Block' = _wrap(_Block.BARRIER)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.GRASS_BLOCK
    GRASS_BLOCK: 'Block' = _wrap(_Block.GRASS_BLOCK)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.BLAST_FURNACE
    BLAST_FURNACE: 'Block' = _wrap(_Block.BLAST_FURNACE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.IRON_ORE
    IRON_ORE: 'Block' = _wrap(_Block.IRON_ORE)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.META_SWITCH_TEST
    META_SWITCH_TEST: 'Block' = _wrap(_Block.META_SWITCH_TEST)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.ERROR
    ERROR: 'Block' = _wrap(_Block.ERROR)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.PLANKS
    PLANKS: 'Block' = _wrap(_Block.PLANKS)

    # public static final dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Blocks.LEAVES
    LEAVES: 'Block' = _wrap(_Block.LEAVES)


    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Blocks()"""
        val = _Blocks()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.Blocks()"""
        val = _Blocks()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.block.Blocks.init()"""
            _Blocks.init()

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
 
 
# CLASS: dev.ultreon.quantum.block.Block
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Block():
    """dev.ultreon.quantum.block.Block"""
 
    @staticmethod
    def _wrap(java_value: _Block) -> 'Block':
        return Block(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Block):
        """
        Dynamic initializer for Block.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Block__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Block__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.block.Block()"""
        val = _Block()
        self.__wrapper = val

    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).onPlace(arg0, arg1, arg2)

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'._wrap(super(Block, self).createMeta())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.block.Block()"""
        val = _Block()
        self.__wrapper = val

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.Block(dev.ultreon.quantum.block.Block$Properties)"""
        val = _Block(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.BlastFurnaceBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.BlastFurnaceBlock as _BlastFurnaceBlock
_BlastFurnaceBlock = _BlastFurnaceBlock
try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlastFurnaceBlock():
    """dev.ultreon.quantum.block.BlastFurnaceBlock"""
 
    @staticmethod
    def _wrap(java_value: _BlastFurnaceBlock) -> 'BlastFurnaceBlock':
        return BlastFurnaceBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlastFurnaceBlock):
        """
        Dynamic initializer for BlastFurnaceBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlastFurnaceBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlastFurnaceBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.BlastFurnaceBlock.createMeta()"""
        return 'state.BlockProperties'._wrap(super(BlastFurnaceBlock, self).createMeta())

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.BlastFurnaceBlock.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_BlastFurnaceBlock, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.BlastFurnaceBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_BlastFurnaceBlock, self).onPlace(arg0, arg1, arg2)

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.BlastFurnaceBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _BlastFurnaceBlock(arg0)
        self.__wrapper = val

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.Block.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_Block, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.CrateBlock
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.block.Block as _Block
_Block = _Block
import dev.ultreon.quantum.item.tool.ToolType as _ToolType
_ToolType = _ToolType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.block.CrateBlock as _CrateBlock
_CrateBlock = _CrateBlock
try:
    from pyquantum.world import loot
except ImportError:
    loot = _import_once("pyquantum.world.loot")

import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.item import tool
except ImportError:
    tool = _import_once("pyquantum.item.tool")

from builtins import bool
import dev.ultreon.quantum.util.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _object
import dev.ultreon.quantum.block.EntityBlock as _EntityBlock
_EntityBlock = _EntityBlock
import dev.ultreon.quantum.block.state.BlockProperties as _BlockProperties
_BlockProperties = _BlockProperties
from builtins import float
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
try:
    from pyquantum.block import entity
except ImportError:
    entity = _import_once("pyquantum.block.entity")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.world.loot.LootGenerator as _LootGenerator
_LootGenerator = _LootGenerator
import dev.ultreon.quantum.world.UseResult as _UseResult
_UseResult = _UseResult
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrateBlock():
    """dev.ultreon.quantum.block.CrateBlock"""
 
    @staticmethod
    def _wrap(java_value: _CrateBlock) -> 'CrateBlock':
        return CrateBlock(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrateBlock):
        """
        Dynamic initializer for CrateBlock.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrateBlock__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrateBlock__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def update(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.Block.update(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_Block, self).update(arg0, arg1, arg2)

    @override
    @overload
    def doesOcclude(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesOcclude()"""
        return bool._wrap(super(Block, self).doesOcclude())

    @override
    @overload
    def isFluid(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isFluid()"""
        return bool._wrap(super(Block, self).isFluid())

    @overload
    def getDrops(self, arg0: 'BlockPos', arg1: 'BlockProperties', arg2: 'Player') -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.block.Block.getDrops(dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        return 'Iterable'._wrap(super(_Block, self).getDrops(arg0, arg1, arg2))

    @overload
    def boundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties', arg4: 'BoundingBox') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.boundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.util.BoundingBox)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).boundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def isUnbreakable(self) -> bool:
        """public final boolean dev.ultreon.quantum.block.Block.isUnbreakable()"""
        return bool._wrap(super(Block, self).isUnbreakable())

    @override
    @overload
    def isAir(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isAir()"""
        return bool._wrap(super(Block, self).isAir())

    @override
    @overload
    def getHardness(self) -> float:
        """public float dev.ultreon.quantum.block.Block.getHardness()"""
        return float._wrap(super(Block, self).getHardness())

    @overload
    def onPlacedBy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player', arg4: 'ItemStack', arg5: 'CubicDirection') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def load(arg0: 'MapType') -> 'Block':
        """public static dev.ultreon.quantum.block.Block dev.ultreon.quantum.block.Block.load(dev.ultreon.ubo.types.MapType)"""
        return Block._wrap(_Block.load(arg0))

    @override
    @overload
    def createMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.createMeta()"""
        return 'state.BlockProperties'._wrap(super(Block, self).createMeta())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hasCollider(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCollider()"""
        return bool._wrap(super(Block, self).hasCollider())

    @overload
    def __init__(self, arg0: 'Properties'):
        """public dev.ultreon.quantum.block.CrateBlock(dev.ultreon.quantum.block.Block$Properties)"""
        val = _CrateBlock(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>)"""
        return EntityBlock._wrap(_EntityBlock.simple(arg0))

    @override
    @overload
    def isToolRequired(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isToolRequired()"""
        return bool._wrap(super(Block, self).isToolRequired())

    @overload
    def canBePlacedAt(self, arg0: 'World', arg1: 'BlockPos', arg2: 'Player', arg3: 'ItemStack', arg4: 'CubicDirection') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBePlacedAt(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.ItemStack,dev.ultreon.quantum.world.CubicDirection)"""
        return bool._wrap(super(_Block, self).canBePlacedAt(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getTranslationId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.getTranslationId()"""
        return str._wrap(super(Block, self).getTranslationId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getToolRequirement(self) -> 'ToolLevel':
        """public dev.ultreon.quantum.block.ToolLevel dev.ultreon.quantum.block.Block.getToolRequirement()"""
        return 'ToolLevel'._wrap(super(Block, self).getToolRequirement())

    @override
    @overload
    def getEffectiveTool(self) -> 'tool.ToolType':
        """public dev.ultreon.quantum.item.tool.ToolType dev.ultreon.quantum.block.Block.getEffectiveTool()"""
        return 'tool.ToolType'._wrap(super(Block, self).getEffectiveTool())

    @overload
    def onPlacedBy(self, arg0: 'BlockProperties', arg1: 'BlockPos', arg2: 'UseItemContext') -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.block.Block.onPlacedBy(dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.item.UseItemContext)"""
        return 'state.BlockProperties'._wrap(super(_Block, self).onPlacedBy(arg0, arg1, arg2))

    @override
    @overload
    def hasCustomRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.hasCustomRender()"""
        return bool._wrap(super(Block, self).hasCustomRender())

    @overload
    def getBoundingBox(self, arg0: 'Vec3i') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(arg0))

    @override
    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.block.Block.getId()"""
        return 'util.Identifier'._wrap(super(Block, self).getId())

    @override
    @overload
    def getTranslation(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.block.Block.getTranslation()"""
        return 'text.TextObject'._wrap(super(Block, self).getTranslation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isTransparent(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isTransparent()"""
        return bool._wrap(super(Block, self).isTransparent())

    @staticmethod
    @overload
    def simple(arg0: 'BlockEntityType', arg1: 'Properties') -> 'EntityBlock':
        """public static dev.ultreon.quantum.block.EntityBlock dev.ultreon.quantum.block.EntityBlock.simple(dev.ultreon.quantum.block.entity.BlockEntityType<?>,dev.ultreon.quantum.block.Block$Properties)"""
        return EntityBlock._wrap(_EntityBlock.simple(arg0, arg1))

    @override
    @overload
    def doesRender(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.doesRender()"""
        return bool._wrap(super(Block, self).doesRender())

    @override
    @overload
    def write(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.block.Block.write(dev.ultreon.quantum.network.PacketIO)"""
        super(_Block, self).write(arg0)

    @overload
    def getLootGen(self, arg0: 'BlockProperties') -> 'loot.LootGenerator':
        """public dev.ultreon.quantum.world.loot.LootGenerator dev.ultreon.quantum.block.Block.getLootGen(dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'loot.LootGenerator'._wrap(super(_Block, self).getLootGen(arg0))

    @override
    @overload
    def getRawId(self) -> int:
        """public int dev.ultreon.quantum.block.Block.getRawId()"""
        return int._wrap(super(Block, self).getRawId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onPlace(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties'):
        """public void dev.ultreon.quantum.block.EntityBlock.onPlace(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties)"""
        super(_EntityBlock, self).onPlace(arg0, arg1, arg2)

    @override
    @overload
    def onDestroy(self, arg0: 'World', arg1: 'BlockPos', arg2: 'BlockProperties', arg3: 'Player'):
        """public void dev.ultreon.quantum.block.Block.onDestroy(dev.ultreon.quantum.world.World,dev.ultreon.quantum.world.BlockPos,dev.ultreon.quantum.block.state.BlockProperties,dev.ultreon.quantum.entity.player.Player)"""
        super(_Block, self).onDestroy(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isReplaceable(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.isReplaceable()"""
        return bool._wrap(super(Block, self).isReplaceable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.Block.toString()"""
        return str._wrap(super(Block, self).toString())

    @overload
    def use(self, arg0: 'World', arg1: 'Player', arg2: 'Item', arg3: 'BlockPos') -> 'world.UseResult':
        """public dev.ultreon.quantum.world.UseResult dev.ultreon.quantum.block.CrateBlock.use(dev.ultreon.quantum.world.World,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,dev.ultreon.quantum.world.BlockPos)"""
        return 'world.UseResult'._wrap(super(_CrateBlock, self).use(arg0, arg1, arg2, arg3))

    @override
    @overload
    def save(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.block.Block.save()"""
        return 'types.MapType'._wrap(super(Block, self).save())

    @overload
    def getBoundingBox(self, arg0: int, arg1: int, arg2: int, arg3: 'BlockProperties') -> 'util.BoundingBox':
        """public dev.ultreon.quantum.util.BoundingBox dev.ultreon.quantum.block.Block.getBoundingBox(int,int,int,dev.ultreon.quantum.block.state.BlockProperties)"""
        return 'util.BoundingBox'._wrap(super(_Block, self).getBoundingBox(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def canBeReplacedBy(self, arg0: 'UseItemContext', arg1: 'BlockProperties') -> bool:
        """public boolean dev.ultreon.quantum.block.Block.canBeReplacedBy(dev.ultreon.quantum.item.UseItemContext,dev.ultreon.quantum.block.state.BlockProperties)"""
        return bool._wrap(super(_Block, self).canBeReplacedBy(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shouldOcclude(self, arg0: 'CubicDirection', arg1: 'Chunk', arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldOcclude(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.world.Chunk,int,int,int)"""
        return bool._wrap(super(_Block, self).shouldOcclude(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def shouldGreedyMerge(self) -> bool:
        """public boolean dev.ultreon.quantum.block.Block.shouldGreedyMerge()"""
        return bool._wrap(super(Block, self).shouldGreedyMerge())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.block.ToolLevel
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.block.ToolLevel as _ToolLevel
_ToolLevel = _ToolLevel
import java.lang.Integer as _int
try:
    from pyquantum import tags
except ImportError:
    tags = _import_once("pyquantum.tags")

from builtins import bool
import dev.ultreon.quantum.tags.NamedTag as _NamedTag
_NamedTag = _NamedTag
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToolLevel():
    """dev.ultreon.quantum.block.ToolLevel"""
 
    @staticmethod
    def _wrap(java_value: _ToolLevel) -> 'ToolLevel':
        return ToolLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToolLevel):
        """
        Dynamic initializer for ToolLevel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToolLevel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToolLevel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tag(self) -> 'tags.NamedTag':
        """public dev.ultreon.quantum.tags.NamedTag<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.block.ToolLevel.tag()"""
        return 'tags.NamedTag'._wrap(super(ToolLevel, self).tag())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.block.ToolLevel.toString()"""
        return str._wrap(super(ToolLevel, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


ToolLevel.GOLD = ToolLevel._wrap(_GOLD.GOLD)

ToolLevel.PLATINUM = ToolLevel._wrap(_PLATINUM.PLATINUM)

ToolLevel.COBALT = ToolLevel._wrap(_COBALT.COBALT)

ToolLevel.IRON = ToolLevel._wrap(_IRON.IRON)

ToolLevel.DIAMOND = ToolLevel._wrap(_DIAMOND.DIAMOND)

ToolLevel.COPPER = ToolLevel._wrap(_COPPER.COPPER)

ToolLevel.STONE = ToolLevel._wrap(_STONE.STONE)

ToolLevel.ULTRINIUM = ToolLevel._wrap(_ULTRINIUM.ULTRINIUM)

ToolLevel.TITANIUM = ToolLevel._wrap(_TITANIUM.TITANIUM)

ToolLevel.CHUNK_STEEL = ToolLevel._wrap(_CHUNK_STEEL.CHUNK_STEEL)

ToolLevel.WOOD = ToolLevel._wrap(_WOOD.WOOD)